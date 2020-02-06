import tkinter as tk
import time

class CanvasDnD(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.loc = self.dragged = self.held = 0
        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=256, height=256,
                           relief=tk.RIDGE, background="white", borderwidth=1)
        self.defaultcolor = canvas.itemcget(
            canvas.create_text(30, 25, font=("Helvetica", 14), text="Item 1", tags="DnD"), "fill")

        self.dictionary = {"Item 1": {"State": "Initial Item"}}

        canvas.pack(expand=1, fill=tk.BOTH)
        canvas.tag_bind("DnD", "<ButtonPress-1>", self.down)
        canvas.tag_bind("DnD", "<ButtonRelease-1>", self.chkup)

        canvas.tag_bind("DnD", "<Double-Button-1>", self.define)

        canvas.tag_bind("DnD", "<Enter>", self.enter)
        canvas.tag_bind("DnD", "<Leave>", self.leave)

        self.canvas = canvas
        master.bind("<Return>", self.submit)

        tk.Label(master, text="Name", width=50, anchor='w').pack(side='top')
        self.name_entry = tk.Entry(master, width=50)
        self.name_entry.pack(side='top')
        tk.Label(master, text="Definition Name", width=50, anchor='w').pack(side='top')
        self.def_name_entry = tk.Entry(master, width=50)
        self.def_name_entry.pack(side='top')
        tk.Label(master, text="Definition", width=50, anchor='w').pack(side='top')
        self.def_entry = tk.Text(master, width=50, height=5)
        self.def_entry.pack(side='top')

        tk.Button(master, text='Enter', command=self.submit, anchor='w').pack(side='top')

    def down(self, event):
        print(
        "Click on %s" % event.widget.itemcget(tk.CURRENT, "text"))
        self.loc = 1
        self.dragged = 0
        event.widget.bind("<Motion>", self.motion)

    def motion(self, event):
        root.config(cursor="exchange")
        cnv = event.widget
        cnv.itemconfigure(tk.CURRENT, fill="blue")
        x, y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        got = event.widget.coords(tk.CURRENT, x, y)

    def leave(self, event):
        self.loc = 0

    def enter(self, event):
        self.loc = 1
        if self.dragged == event.time:
            self.up(event)

    def chkup(self, event):
        event.widget.unbind("<Motion>")
        root.config(cursor="")
        self.target = event.widget.find_withtag(tk.CURRENT)
        event.widget.itemconfigure(tk.CURRENT, fill=self.defaultcolor)
        if self.loc:  # is button released in same widget as pressed?
            self.up(event)
        else:
            self.dragged = event.time

    def up(self, event):
        event.widget.unbind("<Motion>")
        if (self.target == event.widget.find_withtag(tk.CURRENT)):
            print("Select %s" % event.widget.itemcget(tk.CURRENT, "text"))
        else:
            event.widget.itemconfigure(tk.CURRENT, fill="blue")
            self.master.update()
            time.sleep(.1)
            print(
            "%s Drag-N-Dropped onto %s" \
            % (event.widget.itemcget(self.target, "text"),
               event.widget.itemcget(tk.CURRENT, "text")))
            event.widget.itemconfigure(tk.CURRENT, fill=self.defaultcolor)

    def submit(self, *args):
        name = self.name_entry.get()
        def_name_entry = self.def_name_entry.get()
        def_entry = self.def_entry.get("1.0", "end-1c")
        self.dictionary.update({name: dict})
        self.dictionary[name].update({def_name_entry: def_entry})
        self.canvas.create_text(75, 75, font=("Helvetica", 14), text=name, tags="DnD")
        self.name_entry.delete(0, tk.END)
        self.def_name_entry.delete(0, tk.END)
        self.def_entry.delete('1.0', tk.END)

    def define(self, event):
        self.name_entry.delete(0, tk.END)
        self.def_name_entry.delete(0, tk.END)
        self.def_entry.delete('1.0', tk.END)
        item = event.widget.itemcget(tk.CURRENT, "text")
        self.name_entry.insert(0, item)


root = tk.Tk()
root.title("Drag-N-Drop Demo")
CanvasDnD(root).pack()
root.mainloop()


# Phlip phlip_cpp at yahoo.com
# Mon Jun 3 19:18:31 EDT 2002