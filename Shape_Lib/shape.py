class Shape:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = self.x2 - self.x1
        self.h = self.y2 - self.y1
        self.is_selected = False

        self.fill_color = "white"
        self.border_color = "black"
        self.border_width = 3
        self.rad = 5
        self.angle = 0

        self.line_list = []  # List of Tuples: (conn_loc, line_obj, line_end)
        self.points = []
        