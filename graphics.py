import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        # Create canvas to draw on
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Variables to track mouse movement
        self.start_x, self.start_y = None, None
        self.draw_type = None

        # Bind mouse events to canvas
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Create buttons to select drawing type
        self.line_button = tk.Button(root, text="Draw Line", command=self.select_line)
        self.rect_button = tk.Button(root, text="Draw Rectangle", command=self.select_rectangle)
        self.circle_button = tk.Button(root, text="Draw Circle", command=self.select_circle)
        self.line_button.pack(side=tk.LEFT)
        self.rect_button.pack(side=tk.LEFT)
        self.circle_button.pack(side=tk.LEFT)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.start_x is not None and self.start_y is not None:
            self.canvas.delete(self.draw_type)
            x, y = event.x, event.y
            if self.draw_type == "line":
                self.canvas.create_line(self.start_x, self.start_y, x, y, fill="black", width=2)
            elif self.draw_type == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, x, y, outline="black", width=2)
            elif self.draw_type == "circle":
                self.canvas.create_oval(self.start_x, self.start_y, x, y, outline="black", width=2)

    def on_release(self, event):
        self.start_x, self.start_y = None, None

    def select_line(self):
        self.draw_type = "line"

    def select_rectangle(self):
        self.draw_type = "rectangle"

    def select_circle(self):
        self.draw_type = "circle"

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
