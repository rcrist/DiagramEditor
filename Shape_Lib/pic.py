from Shape_Lib.shape import Shape
from PIL import Image, ImageTk
import tkinter as tk


class Pic(Shape):
    def __init__(self, canvas, x, y, w, h):
        super().__init__(canvas, x, y, w, h)  # x, y, width, height, angle
        self.a_image = None
        self.ph_image = None
        self.filename = None
        self.shape_id = None
        self.bbox = None
        self.type = 'pic'

    def draw(self):
        self.a_image = Image.open(self.filename)
        self.a_image = self.a_image.rotate(self.angle)
        self.ph_image = ImageTk.PhotoImage(self.a_image)
        self.shape_id = self.canvas.create_image(self.x1, self.y1, anchor=tk.CENTER, image=self.ph_image, tags="pics")
        self.bbox = self.canvas.bbox(self.shape_id)
        self.canvas.ph_image = self.ph_image
        self.canvas.a_image = self.a_image

        if self.is_selected:
            self.canvas.create_rectangle(self.bbox, fill=None, outline="red", width=3)
