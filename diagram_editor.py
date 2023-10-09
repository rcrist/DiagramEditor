import customtkinter as ctk

from UI_Lib.canvas import Canvas
from UI_Lib.right_frame import RightFrame
from UI_Lib.top_frame import TopFrame

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class DiagramEditorApp(ctk.CTk):
    """ctk.CTk is a CustomTkinter main window, similar to tk.Tk tkinter main window"""
    def __init__(self):
        super().__init__()
        self.geometry("1200x800x100x100")  # w, h, x, y
        self.title("Diagram Editor")

        # Create Canvas widget
        self.canvas = Canvas(self)

        top_frame = TopFrame(self, self.canvas, height=30)
        right_frame = RightFrame(self, self.canvas, width=150)

        top_frame.pack(side=ctk.TOP, fill=ctk.BOTH)
        right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH)
        self.canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.mouse.bind_draw_mouse_events()

        # Bind 'r' and 'e' keys for 90 deg rotation
        self.bind('<r>', self.canvas.rotate_shape_ccw)
        self.bind('<e>', self.canvas.rotate_shape_cw)

        self.canvas.bind('<Button-3>', self.canvas.edit_shape)
        self.bind('<Delete>', self.canvas.delete_shape)

        # Bindings for window resize - redraw grid and shapes
        self.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, _event):
        self.canvas.draw_shapes()


if __name__ == "__main__":
    """Instantiate the Line Editor application and run the main loop"""
    app = DiagramEditorApp()
    app.mainloop()
