import time
import tkinter as tk

class CanvasDnD(tk.Frame):
    # see http://www.bitflipper.ca/Documentation/dnd_barebones.txt
    def __init__(self, master, canvas):
        self.master = master
        self.loc = self.dragged = 0
        tk.Frame.__init__(self, master)

        canvas.tag_bind("DnD", "<ButtonPress-1>", self.down)
        canvas.tag_bind("DnD", "<ButtonRelease-1>", self.chkup)
        canvas.tag_bind("DnD", "<Enter>", self.enter)
        canvas.tag_bind("DnD", "<Leave>", self.leave)
        canvas.bind("<Key-f>", self.flip)

    # mouse button down, start drag
    def down(self, event):
        self.loc = 1
        self.dragged = 0
        cnv = event.widget
        self.x, self.y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        self.color = cnv.itemcget(tk.CURRENT, "fill")
        event.widget.bind("<Motion>", self.motion)

    # mouse is dragging
    def motion(self, event):
        root.config(cursor="exchange")
        cnv = event.widget
        cnv.itemconfigure(tk.CURRENT, fill="white", outline="grey", dash=(5, 5))
        x, y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        dx = x - self.x
        dy = y - self.y
        self.x = x
        self.y = y
        # got = event.widget.coords(tk.CURRENT, x, y)
        event.widget.move(tk.CURRENT, dx, dy)

    def leave(self, event):
        print("leave")
        canvas.itemconfigure(tk.CURRENT, outline="")
        self.loc = 0

    def enter(self, event):
        print("enter", event)
        canvas.itemconfigure(tk.CURRENT, outline="darkred", width=2)
        self.loc = 1
        if self.dragged == event.time:
            self.up(event)
        canvas.focus_set()

    # mouse button released
    def chkup(self, event):
        event.widget.unbind("<Motion>")
        root.config(cursor="")
        self.target = event.widget.find_withtag(tk.CURRENT)
        event.widget.itemconfigure(tk.CURRENT, fill=self.color, dash=())
        if self.loc:  # is button released in same widget as pressed?
            self.up(event)
        else:
            self.dragged = event.time
        redraw_wires()

    def up(self, event):
        event.widget.unbind("<Motion>")
        if self.target == event.widget.find_withtag(tk.CURRENT):
            pass
            # print("Select %s" % event.widget.itemcget(tk.CURRENT, "text"))
        else:
            event.widget.itemconfigure(tk.CURRENT, fill="blue")
            self.master.update()
            time.sleep(0.1)
            # print("%s Drag-N-Dropped onto %s"
            #       % (event.widget.itemcget(self.target, "text"),
            #          event.widget.itemcget(tk.CURRENT, "text")))
            event.widget.itemconfigure(tk.CURRENT, fill=self.defaultcolor)

    def flip(self, event):
        print("flip")
        b4.flip()

def grid(canvas, line_distance, root):
    root.update()
    print(canvas.winfo_width())
    canvas_width = 1000
    canvas_height = 500
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#f0f0f0")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#f0f0f0")