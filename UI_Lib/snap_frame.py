import customtkinter as ctk
from tktooltip import ToolTip
from PIL import Image


class SnapFrame(ctk.CTkFrame):
    def __init__(self, parent, canvas):
        super().__init__(parent)
        self.parent = parent
        self.canvas = canvas

        self.init_move_snap_control(self)
        self.init_rotate_snap_control(self)
        self.init_resize_snap_control(self)

    def init_move_snap_control(self, snap_frame):
        move_frame = ctk.CTkFrame(snap_frame, width=150)
        move_frame.configure(fg_color=("gray28", "gray28"))  # set frame color
        move_frame.pack(side=ctk.LEFT, padx=5, pady=5)

        my_image = ctk.CTkImage(light_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/grid.png"),
                                dark_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/grid.png"),
                                size=(24, 24))

        image_label = ctk.CTkLabel(move_frame, image=my_image, text="", corner_radius=10)
        image_label.pack(side=ctk.LEFT)

        # Add OptionMenu to top frame
        def option_menu_callback(choice):
            self.canvas.mouse.move_snap = int(choice)

        option_menu = ctk.CTkOptionMenu(move_frame, values=["5", "10", "20", "30"], width=32,
                                        command=option_menu_callback)
        option_menu.pack(side=ctk.LEFT)
        option_menu.set("10")

        ToolTip(option_menu, msg="Move snap")

    def init_rotate_snap_control(self, snap_frame):
        rotate_frame = ctk.CTkFrame(snap_frame, width=150)
        rotate_frame.configure(fg_color=("gray28", "gray28"))  # set frame color
        rotate_frame.pack(side=ctk.LEFT, padx=5, pady=5)

        my_image = ctk.CTkImage(light_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/angle.png"),
                                dark_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/angle.png"),
                                size=(24, 24))

        image_label = ctk.CTkLabel(rotate_frame, image=my_image, text="", corner_radius=10)
        image_label.pack(side=ctk.LEFT)

        # Add OptionMenu to top frame
        def option_menu_callback(choice):
            self.canvas.mouse.rotate_snap = int(choice)

        option_menu = ctk.CTkOptionMenu(rotate_frame, values=["90"], width=32,
                                        command=option_menu_callback)
        option_menu.pack(side=ctk.LEFT)
        option_menu.set("90")

        ToolTip(option_menu, msg="Rotate snap")

    def init_resize_snap_control(self, snap_frame):
        resize_frame = ctk.CTkFrame(snap_frame, width=150)
        resize_frame.configure(fg_color=("gray28", "gray28"))  # set frame color
        resize_frame.pack(side=ctk.LEFT, padx=5, pady=5)

        my_image = ctk.CTkImage(light_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/resize.png"),
                                dark_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/resize.png"),
                                size=(24, 24))

        image_label = ctk.CTkLabel(resize_frame, image=my_image, text="", corner_radius=10)
        image_label.pack(side=ctk.LEFT)

        # Add OptionMenu to top frame
        def option_menu_callback(choice):
            self.canvas.mouse.resize_snap = int(choice)

        option_menu = ctk.CTkOptionMenu(resize_frame, values=["5", "10", "20", "30"], width=32,
                                        command=option_menu_callback)
        option_menu.pack(side=ctk.LEFT)
        option_menu.set("10")

        ToolTip(option_menu, msg="Resize snap")
