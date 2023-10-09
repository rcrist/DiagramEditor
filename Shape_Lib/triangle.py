import math
from Shape_Lib.shape import Shape


class Triangle(Shape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)
        self.w = self.x2 - self.x1
        self.conns = []      # List of Tuples: (conn_loc, xc, yc)
        self.rotation_center = (0, 0)
        self.radian_angle = 0
        self.type = 'triangle'

    def draw(self):
        self.rotation_center = (self.x1 + self.w / 2, self.y1 + self.h / 2)
        self.radian_angle = math.radians(self.angle)
        # Calculate the rotated coordinates of the four corners
        x1, y1 = self.rotate_point(self.x1 + self.w/2, self.y1, self.radian_angle)
        x2, y2 = self.rotate_point(self.x1, self.y2, self.radian_angle)
        x3, y3 = self.rotate_point(self.x2, self.y2, self.radian_angle)

        self.points = [x1, y1, x2, y2, x3, y3]
        self.canvas.create_polygon(self.points, fill=self.fill_color, outline=self.border_color,
                                   width=self.border_width)

        if self.is_selected:
            self.draw_conns()

    def rotate_point(self, x, y, angle):
        # Rotate a point (x, y) by a given angle around the rotation center
        x -= self.rotation_center[0]
        y -= self.rotation_center[1]
        new_x = x * math.cos(angle) - y * math.sin(angle) + self.rotation_center[0]
        new_y = x * math.sin(angle) + y * math.cos(angle) + self.rotation_center[1]
        return new_x, new_y

    def draw_conns(self):
        self.update_conns()
        for a_conn in self.conns:
            rad = self.rad
            xc, yc = a_conn[1], a_conn[2]
            points = [xc - rad, yc - rad, xc + rad, yc + rad]
            self.canvas.create_oval(points, activefill="cyan", fill="red", outline="black", width=3)

    def update_conns(self):
        self.w = self.x2 - self.x1
        self.h = self.y2 - self.y1
        tc_x, tc_y = self.rotate_point(self.x1 + self.w / 2, self.y1, self.radian_angle)
        rc_x, rc_y = self.rotate_point(self.x2 - self.w / 4, self.y1 + self.h / 2, self.radian_angle)
        bc_x, bc_y = self.rotate_point(self.x1 + self.w / 2, self.y2, self.radian_angle)
        lc_x, lc_y = self.rotate_point(self.x1 + self.w / 4, self.y1 + self.h / 2, self.radian_angle)
        c_x, c_y = self.rotate_point(self.x1 + self.w / 2, self.y1 + self.h / 2, self.radian_angle)
        self.conns = [
            ("tc", tc_x, tc_y),  # Top center
            ("rc", rc_x, rc_y),  # Right center
            ("bc", bc_x, bc_y),  # Bottom center
            ("lc", lc_x, lc_y),  # Left center
            ("c", c_x, c_y)  # Shape center
        ]
