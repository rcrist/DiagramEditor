from Shape_Lib.oval import Oval
from Shape_Lib.rectangle import Rectangle
from Shape_Lib.triangle import Triangle
from Shape_Lib.line import Line
from Shape_Lib.text import Text
from Shape_Lib.pic import Pic


class Mouse:
    def __init__(self, canvas):
        self.canvas = canvas
        self.current_shape = None
        self.current_shape_obj = None

        self.start_x, self.start_y = 0, 0
        self.offset_x1, self.offset_y1 = 0, 0
        self.offset_x2, self.offset_y2 = 0, 0

        self.mouse_x, self.mouse_y = 0, 0

        self.move_snap = 10
        self.rotate_snap = 10
        self.resize_snap = 10

    def unbind_mouse_events(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

    def bind_draw_mouse_events(self):
        self.canvas.bind("<Button-1>", self.draw_left_down)
        self.canvas.bind("<B1-Motion>", self.draw_left_drag)
        self.canvas.bind("<ButtonRelease-1>", self.draw_left_up)

    def bind_move_mouse_events(self):
        self.canvas.bind("<Button-1>", self.move_left_down)
        self.canvas.bind("<B1-Motion>", self.move_left_drag)
        self.canvas.bind("<ButtonRelease-1>", self.move_left_up)

    def bind_resize_mouse_events(self):
        self.canvas.bind("<Button-1>", self.resize_left_down)
        self.canvas.bind("<B1-Motion>", self.resize_left_drag)
        self.canvas.bind("<ButtonRelease-1>", self.resize_left_up)

    def select_left_down(self, event):
        x, y = event.x, event.y
        for item in self.canvas.shape_list:
            item.is_selected = False
        self.check_bbox_hit(x, y)
        self.canvas.draw_shapes()

    def draw_left_down(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Snap the shape to the move snap
        self.start_x = round(self.start_x / self.move_snap) * self.move_snap
        self.start_y = round(self.start_y / self.move_snap) * self.move_snap
        if self.current_shape == "rectangle":
            self.current_shape_obj = Rectangle(
                self.canvas, self.start_x, self.start_y, self.start_x, self.start_y
            )
        elif self.current_shape == "oval":
            self.current_shape_obj = Oval(
                self.canvas, self.start_x, self.start_y, self.start_x, self.start_y
            )
        elif self.current_shape == "triangle":
            self.current_shape_obj = Triangle(
                self.canvas, self.start_x, self.start_y, self.start_x + 100, self.start_y + 100
            )
        elif self.current_shape == "text":
            self.current_shape_obj = Text(
                self.canvas, self.start_x, self.start_y, self.start_x, self.start_y
            )
        elif self.current_shape == "image":
            self.current_shape_obj = Pic(
                self.canvas, self.start_x, self.start_y, self.start_x, self.start_y
            )
            self.current_shape_obj.filename = "D:/Project_Engineering_Tools/engineering_tools/images/hamburger.png"
        elif self.current_shape == "line":
            self.current_shape_obj = Line(
                self.canvas, self.start_x, self.start_y, self.start_x, self.start_y
            )
            self.snap_to_shape("start", self.start_x, self.start_y)

        if self.current_shape_obj is not None:
            self.canvas.shape_list.append(self.current_shape_obj)
            self.canvas.draw_shapes()

    def draw_left_drag(self, event):
        if self.current_shape_obj:
            x, y = event.x, event.y
            # Snap the shape to the move snap
            x = round(x / self.move_snap) * self.move_snap
            y = round(y / self.move_snap) * self.move_snap
            self.current_shape_obj.x1, self.current_shape_obj.y1 = self.start_x, self.start_y
            self.current_shape_obj.x2, self.current_shape_obj.y2 = x, y
            self.canvas.draw_shapes()

    def draw_left_up(self, _event):
        if self.current_shape == "line":
            self.snap_to_shape("end", self.current_shape_obj.x2, self.current_shape_obj.y2)
        self.current_shape = None
        self.current_shape_obj = None

    def move_left_down(self, event):
        if self.canvas.selected:
            x1, y1 = self.canvas.selected.x1, self.canvas.selected.y1
            x2, y2 = self.canvas.selected.x2, self.canvas.selected.y2
            self.offset_x1 = event.x - x1
            self.offset_y1 = event.y - y1
            self.offset_x2 = event.x - x2
            self.offset_y2 = event.y - y2
            # Snap the shape to the move snap
            self.offset_x1 = round(self.offset_x1 / self.move_snap) * self.move_snap
            self.offset_y1 = round(self.offset_y1 / self.move_snap) * self.move_snap
            self.offset_x2 = round(self.offset_x2 / self.move_snap) * self.move_snap
            self.offset_y2 = round(self.offset_y2 / self.move_snap) * self.move_snap
            self.canvas.draw_shapes()

    def move_left_drag(self, event):
        if self.canvas.selected:
            if isinstance(self.canvas.selected, Text):
                x1 = event.x - self.offset_x1
                y1 = event.y - self.offset_y1
                # Snap the shape to the move snap
                x1 = round(x1 / self.move_snap) * self.move_snap
                y1 = round(y1 / self.move_snap) * self.move_snap
                self.canvas.selected.x1, self.canvas.selected.y1 = x1, y1
            else:
                x1 = event.x - self.offset_x1
                y1 = event.y - self.offset_y1
                # Snap the shape to the move snap
                x1 = round(x1 / self.move_snap) * self.move_snap
                y1 = round(y1 / self.move_snap) * self.move_snap
                self.canvas.selected.x1, self.canvas.selected.y1 = x1, y1
                x2 = event.x - self.offset_x2
                y2 = event.y - self.offset_y2
                # Snap the shape to the move snap
                x2 = round(x2 / self.move_snap) * self.move_snap
                y2 = round(y2 / self.move_snap) * self.move_snap
                self.canvas.selected.x2, self.canvas.selected.y2 = x2, y2

            if not isinstance(self.canvas.selected, Line):
                self.move_connected_lines()
            self.canvas.draw_shapes()

    def move_left_up(self, _event):
        self.offset_x1, self.offset_y1 = 0, 0
        self.offset_x2, self.offset_y2 = 0, 0

    def move_connected_lines(self):
        for line in self.canvas.selected.line_list:  # List of Tuples: (conn_loc, line_obj, line_end)
            # print("Selected shape: ", self.selected, " Line: ", line)
            conn_loc = line[0]
            if line[2] == "start":
                if conn_loc == "tc":
                    line[1].x1 = self.canvas.selected.conns[0][1]
                    line[1].y1 = self.canvas.selected.conns[0][2]
                elif conn_loc == "rc":
                    line[1].x1 = self.canvas.selected.conns[1][1]
                    line[1].y1 = self.canvas.selected.conns[1][2]
                elif conn_loc == "bc":
                    line[1].x1 = self.canvas.selected.conns[2][1]
                    line[1].y1 = self.canvas.selected.conns[2][2]
                elif conn_loc == "lc":
                    line[1].x1 = self.canvas.selected.conns[3][1]
                    line[1].y1 = self.canvas.selected.conns[3][2]
                elif conn_loc == "c":
                    line[1].x1 = self.canvas.selected.conns[4][1]
                    line[1].y1 = self.canvas.selected.conns[4][2]
            elif line[2] == "end":
                if conn_loc == "tc":
                    line[1].x2 = self.canvas.selected.conns[0][1]
                    line[1].y2 = self.canvas.selected.conns[0][2]
                elif conn_loc == "rc":
                    line[1].x2 = self.canvas.selected.conns[1][1]
                    line[1].y2 = self.canvas.selected.conns[1][2]
                elif conn_loc == "bc":
                    line[1].x2 = self.canvas.selected.conns[2][1]
                    line[1].y2 = self.canvas.selected.conns[2][2]
                elif conn_loc == "lc":
                    line[1].x2 = self.canvas.selected.conns[3][1]
                    line[1].y2 = self.canvas.selected.conns[3][2]
                elif conn_loc == "c":
                    line[1].x2 = self.canvas.selected.conns[4][1]
                    line[1].y2 = self.canvas.selected.conns[4][2]

    def resize_left_down(self, event):
        if self.canvas.selected:
            x1, y1 = self.canvas.selected.x1, self.canvas.selected.y1
            x2, y2 = self.canvas.selected.x2, self.canvas.selected.y2
            self.offset_x1 = event.x - x1
            self.offset_y1 = event.y - y1
            self.offset_x2 = event.x - x2
            self.offset_y2 = event.y - y2
            # Snap the shape to the move snap
            self.offset_x1 = round(self.offset_x1 / self.move_snap) * self.move_snap
            self.offset_y1 = round(self.offset_y1 / self.move_snap) * self.move_snap
            self.offset_x2 = round(self.offset_x2 / self.move_snap) * self.move_snap
            self.offset_y2 = round(self.offset_y2 / self.move_snap) * self.move_snap
            self.canvas.draw_shapes()

    def resize_left_drag(self, event):
        if self.canvas.selected:
            if isinstance(self.canvas.selected, Text) or isinstance(self.canvas.selected, Pic):
                pass
            else:
                x2 = event.x - self.offset_x2
                y2 = event.y - self.offset_y2
                # Snap the shape to the move snap
                x2 = round(x2 / self.move_snap) * self.move_snap
                y2 = round(y2 / self.move_snap) * self.move_snap
                self.canvas.selected.x2, self.canvas.selected.y2 = x2, y2

            if not isinstance(self.canvas.selected, Line):
                self.move_connected_lines()
            self.canvas.draw_shapes()

    def resize_left_up(self, _event):
        self.offset_x1, self.offset_y1 = 0, 0
        self.offset_x2, self.offset_y2 = 0, 0

    def check_bbox_hit(self, x, y):
        """Check to see if the mouse has clicked on a shape object"""
        for item in self.canvas.shape_list:
            if isinstance(item, Text) or isinstance(item, Pic):
                if (
                    item.bbox[0] <= x <= item.bbox[2]
                    and item.bbox[1] <= y <= item.bbox[3]
                ):
                    self.canvas.selected = item

                    if self.canvas.selected.is_selected:
                        self.canvas.selected.is_selected = False
                    else:
                        self.canvas.selected.is_selected = True
            else:
                if (
                        item.x1 <= x <= item.x2
                        and item.y1 <= y <= item.y2
                ):
                    self.canvas.selected = item

                    if self.canvas.selected.is_selected:
                        self.canvas.selected.is_selected = False
                    else:
                        self.canvas.selected.is_selected = True

    def snap_to_shape(self, line_end, x, y):
        for item in self.canvas.shape_list:
            if not isinstance(item, Line) and not isinstance(item, Text) and not isinstance(item, Pic):
                for a_conn in item.conns:
                    conn_loc, xc, yc = a_conn
                    rad = item.rad
                    x1, y1, x2, y2 = [xc - rad, yc - rad, xc + rad, yc + rad]
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        # List of Tuples: (conn_loc, line_obj, line_end)
                        item.line_list.append((conn_loc, self.current_shape_obj, line_end))
