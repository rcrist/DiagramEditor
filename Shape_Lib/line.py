from Shape_Lib.shape import Shape


class Line(Shape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)
        self.fill_color = "black"
        self.type = 'line'

    def draw(self):
        points = [self.x1, self.y1, self.x2, self.y2]
        self.canvas.create_line(points, fill=self.fill_color, width=self.border_width)

        if self.is_selected:
            # Draw selectors
            self.canvas.create_oval(self.x1-5, self.y1-5, self.x1+5, self.y1+5, fill='#d98eff',
                                    width=1)
            self.canvas.create_oval(self.x2 - 5, self.y2 - 5, self.x2 + 5, self.y2 + 5, fill='#d98eff',
                                    width=1)
