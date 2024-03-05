import bdsim
import tkinter as tk	
from CanvasDnD import CanvasDnD, grid


root = tk.Tk()
sim = bdsim.BDSim()  # create simulator
root = tk.Tk()
root.title("bdsim editor")

bd = sim.blockdiagram()  # create an empty block diagram# define the blocks
demand = bd.STEP(T=1, name='demand')
sum = bd.SUM('+-')
gain = bd.GAIN(10)
plant = bd.LTI_SISO(0.5, [2, 1])
scope = bd.SCOPE(styles=['k', 'r--'])
# connect the blocks
bd.connect(demand, sum[0], scope[1])
bd.connect(plant, sum[1])
bd.connect(sum, gain)
bd.connect(gain, plant)
bd.connect(plant, scope[0])

canvas = tk.Canvas(
    root,
    bg="white",
    height=500,
    width=1000,
    relief=tk.RIDGE,
    background="white",
    borderwidth=1,
)
canvas.pack()
grid(canvas, 20, root)


CanvasDnD(root, canvas)
root.mainloop()