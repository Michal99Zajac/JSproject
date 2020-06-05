import tkinter as tk
from apply import apply

class MultiListBox(tk.Frame):
    """
    expand the listbox class
    """
    def __init__(self, master, data):
        tk.Frame.__init__(self, master)
        self.lists = []

        for name, width in data:
            temp_frame = tk.Frame(self)
            temp_frame.pack(
                side=tk.LEFT,
                expand=tk.YES,
                fill=tk.BOTH
                )

            tk.Label(
                master=temp_frame,
                text=name,
                borderwidth=1,
                relief=tk.RAISED
            ).pack(fill=tk.X)

            lb = tk.Listbox(
                master=temp_frame,
                width=width,
                #height=45,
                borderwidth=0,
                selectborderwidth=0,
                relief=tk.FLAT,
                exportselection=tk.FALSE,
                selectmode=tk.SINGLE
            )
            lb.pack(expand=tk.YES, fill=tk.BOTH)

            self.lists.append(lb)
            
            lb.bind('<B1-Motion>',lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>',lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button(e.x, e.y))
            lb.bind('<Button-4>', lambda e, s=self: s._scroll(tk.SCROLL, -1, tk.PAGES))
            lb.bind('<Button-5>',lambda e, s=self: s._scroll(tk.SCROLL, -1, tk.PAGES))
            
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, fill=tk.Y)
        tk.Label(
            master=frame,
            borderwidth=1,
            relief=tk.RAISED
        ).pack(fill=tk.X)
        sb = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self._scroll)
        sb.pack(expand=tk.YES, fill=tk.Y)
        self.lists[0]['yscrollcommand'] = sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, tk.END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for li in self.lists:
            li.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for li in self.lists:
            li.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for li in self.lists:
            apply(l.yview, args)
        return 'break'


    def curselection(self):
        return self.lists[0].curselection()


    def get(self, first, last=None):
        result = []
        for li in self.lists:
            result.append(li.get(first, last))
        if last:
            return apply(map, [None] + result)
        return result


    def selection_set(self, first, last=None):
        for li in self.lists:
            li.selection_set(first, last)


    def selection_clear(self, first, last=None):
        for li in self.lists:
            li.selection_clear(first, last)


    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for li in self.lists:
                li.insert(index, e[i])
                i += 1


    def delete(self, first, last=None):
        for li in self.lists:
            li.delete(first, last)


    def index(self, index):
        return self.lists[0].index(index)


    def size(self):
        return self.lists[0].size()


    def see(self, index):
        for li in self.lists:
            li.see(index)

    def selection_anchor(self, index):
        for li in self.lists:
            li.selection_anchor(index)


    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)