import cv2
import numpy as np
import torch
import os
from model.RIFE import Model

# --- Load model ---
model = Model()
model.load_model('train_log')  # path to weights
model.eval()

# --- Input video ---
cwd = os.getcwd()
cap = cv2.VideoCapture(cwd + "/A.mov")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output with double FPS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output_interp.mp4", fourcc, fps*2, (width, height))

ret, prev_frame = cap.read()
while True:
    ret, next_frame = cap.read()
    if not ret:
        break

    # OpenCV -> torch tensor
    I0 = torch.from_numpy(prev_frame).permute(2,0,1).unsqueeze(0).float()/255.
    I1 = torch.from_numpy(next_frame).permute(2,0,1).unsqueeze(0).float()/255.

    with torch.no_grad():
        mid = model.inference(I0, I1, 0.5)  # interpolate halfway frame

    # Torch -> numpy
    mid_frame = (mid[0].permute(1,2,0).cpu().numpy()*255).astype(np.uint8)

    # Write: prev -> mid -> next
    out.write(prev_frame)
    out.write(mid_frame)
    prev_frame = next_frame

# Flush last frame
out.write(prev_frame)

cap.release()
out.release()
print("Done: output_interp.mp4")