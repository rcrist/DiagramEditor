from Shape_Lib.shape import Shape


class Text(Shape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)
        self.is_selected = False
        self.selectors = None
        self.fill_color = "black"
        self.text = 'Hello World'
        self.shape_id = None
        self.bbox = None
        self.type = 'text'

    def draw(self):
        if self.is_selected:
            self.shape_id = self.canvas.create_text(self.x1, self.y1, text=self.text, fill='#d98eff',
                                    font='Helvetica 15 bold', angle=self.angle, tags="texts")
            self.bbox = self.canvas.bbox(self.shape_id)
        else:
            self.shape_id = self.canvas.create_text(self.x1, self.y1, text=self.text, fill=self.fill_color,
                                font='Helvetica 15 bold', angle=self.angle, tags="texts")
            self.bbox = self.canvas.bbox(self.shape_id)
