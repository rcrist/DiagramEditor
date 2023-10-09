import customtkinter as ctk
from tkinter import filedialog

from UI_Lib.mouse import Mouse
from Shape_Lib.grid import Grid


class Canvas(ctk.CTkCanvas):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.shape_list = []
        self.selected = None
        self.mode = None
        self.mouse = Mouse(self)

        self.grid_size = 20
        self.grid = Grid(self, self.grid_size)
        self.grid.draw_grid()

    def edit_shape(self, _event):
        if self.selected is not None:
            if self.gettags("current")[0] == "pics":
                filename = filedialog.askopenfilename(initialdir="../images", title="select a file",
                                                      filetypes=(("png files", "*.png"), ("all file", "*.*")))
                self.selected.filename = filename
                self.selected.draw()
            elif self.gettags("current")[0] == "texts":
                dialog = ctk.CTkInputDialog(text="Enter new text", title="Edit Text")
                self.selected.text = dialog.get_input()
                self.draw_shapes()

    def draw_shapes(self):
        self.delete('all')
        self.grid.draw_grid()
        for a_shape in self.shape_list:
            a_shape.draw()

    def select_shape(self):
        self.mouse.unbind_mouse_events()
        self.bind("<Button-1>", self.mouse.select_left_down)

    def rotate_shape_ccw(self, _event):
        if self.selected is not None and self.mode == "Rotate":
            self.selected.angle -= 90
            if self.selected.angle < 0:
                self.selected.angle = 270
            self.draw_shapes()

    def rotate_shape_cw(self, _event):
        if self.selected is not None and self.mode == "Rotate":
            self.selected.angle += 90
            if self.selected.angle > 270:
                self.selected.angle = 0
            self.draw_shapes()

    def delete_shape(self, _event):
        print("Delete shape called...")
        for item in self.shape_list:
            if item.is_selected:
                self.shape_list.remove(item)
                self.draw_shapes()
