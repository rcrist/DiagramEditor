import customtkinter as ctk


class RightFrame(ctk.CTkFrame):
    def __init__(self, parent, canvas, width):
        super().__init__(parent, width)
        self.parent = parent
        self.canvas = canvas

        self.rect_button = None
        self.circle_button = None
        self.tri_button = None
        self.text_button = None
        self.image_button = None
        self.line_button = None
        self.clear_button = None
        self.select_button = None
        self.move_button = None

        self.init_frame()

    def init_frame(self):
        self.rect_button = ctk.CTkButton(self, text="Rectangle", command=self.create_rectangle)
        self.circle_button = ctk.CTkButton(self, text="Oval", command=self.create_circle)
        self.tri_button = ctk.CTkButton(self, text="Triangle", command=self.create_triangle)
        self.text_button = ctk.CTkButton(self, text="Text", command=self.create_text)
        self.image_button = ctk.CTkButton(self, text="Image", command=self.create_image)
        self.line_button = ctk.CTkButton(self, text="Line", command=self.create_line)
        self.clear_button = ctk.CTkButton(self, text="Clear", command=self.clear_canvas)
        self.select_button = ctk.CTkButton(self, text="Select", command=self.canvas.select_shape)

        self.rect_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.circle_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.tri_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.text_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.image_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.line_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.clear_button.pack(side=ctk.TOP, padx=5, pady=5)
        self.select_button.pack(side=ctk.TOP, padx=5, pady=5)

    def create_rectangle(self):
        self.canvas.mouse.current_shape = "rectangle"
        self.canvas.mouse.bind_draw_mouse_events()

    def create_circle(self):
        self.canvas.mouse.current_shape = "oval"
        self.canvas.mouse.bind_draw_mouse_events()

    def create_triangle(self):
        self.canvas.mouse.current_shape = "triangle"
        self.canvas.mouse.bind_draw_mouse_events()

    def create_text(self):
        self.canvas.mouse.current_shape = "text"
        self.canvas.mouse.bind_draw_mouse_events()

    def create_image(self):
        self.canvas.mouse.current_shape = "image"
        self.canvas.mouse.bind_draw_mouse_events()

    def create_line(self):
        self.canvas.mouse.current_shape = "line"
        self.canvas.mouse.bind_draw_mouse_events()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.canvas.shape_list = []
