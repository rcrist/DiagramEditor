from Shape_Lib.shape import Shape


class Oval(Shape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)
        self.conns = []      # List of Tuples: (conn_loc, xc, yc)
        self.type = 'oval'

    def draw(self):
        if self.angle == 0 or self.angle == 180:
            self.points = [self.x1, self.y1, self.x2, self.y2]
        elif self.angle == 90 or self.angle == 270:
            center_x, center_y = self.x1 + self.w/2, self.y1 + self.h/2
            self.x1 = center_x - self.h/2
            self.y1 = center_y - self.w/2
            self.x2 = center_x + self.h/2
            self.y2 = center_y + self.w/2
            self.points = [self.x1, self.y1, self.x2, self.y2]

        self.canvas.create_oval(self.points, fill=self.fill_color, outline=self.border_color,
                                width=self.border_width)

        if self.is_selected:
            self.draw_conns()

    def draw_conns(self):
        self.update_conns()
        for a_conn in self.conns:
            rad = self.rad
            xc, yc = a_conn[1], a_conn[2]
            points = [xc-rad, yc-rad, xc+rad, yc+rad]
            self.canvas.create_oval(points, activefill="cyan", fill="red", outline="black", width=3)

    def update_conns(self):
        self.w = self.x2 - self.x1
        self.h = self.y2 - self.y1
        self.conns = [
            ("tc", self.x1 + self.w / 2, self.y1),  # Top center
            ("rc", self.x2, self.y1 + self.h / 2),  # Right center
            ("bc", self.x1 + self.w / 2, self.y2),  # Bottom center
            ("lc", self.x1, self.y1 + self.h / 2),  # Left center
            ("c", self.x1 + self.w / 2, self.y1 + self.h / 2)  # Shape center
        ]
