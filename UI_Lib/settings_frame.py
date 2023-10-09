import customtkinter as ctk
from PIL import Image


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, window, parent, canvas):
        super().__init__(parent)
        self.canvas = canvas

        self.menu_on = False

        self.menu_frame = ctk.CTkFrame(window, height=100, bg_color="white")

        def grid_switch_event():
            if canvas.grid.grid_visible:
                canvas.grid.grid_visible = False
                self.canvas.mouse.move_snap = 1
                self.canvas.mouse.resize_snap = 1
                self.canvas.mouse.rotate_snap = 90
            else:
                canvas.grid.grid_visible = True
                self.canvas.mouse.move_snap = 10
                self.canvas.mouse.resize_snap = 10
                self.canvas.mouse.rotate_snap = 90
            self.canvas.draw_shapes()

        switch_var = ctk.StringVar(value="off")
        switch = ctk.CTkSwitch(self.menu_frame, text="Grid", command=grid_switch_event,
                                         variable=switch_var, onvalue="on", offvalue="off")
        switch.pack(padx=5, pady=5)

        def optionmenu_callback(choice):
            self.canvas.grid.grid_size = int(choice)
            self.canvas.draw_shapes()

        optionmenu = ctk.CTkOptionMenu(self.menu_frame, values=["5", "10", "20", "30", "40", "50"],
                                                 command=optionmenu_callback)
        optionmenu.pack(padx=5, pady=5)
        optionmenu.set("20")

        self.appearance_mode_label = ctk.CTkLabel(self.menu_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.pack(padx=5, pady=5)
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.menu_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(padx=5, pady=5)

        my_image = ctk.CTkImage(light_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/settings.png"),
                                dark_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/settings.png"),
                                size=(24, 24))

        button = ctk.CTkButton(self, text="", image=my_image, width=30, command=self.show_menu)
        button.pack(side=ctk.LEFT, padx=5, pady=10)

    def show_menu(self):
        if not self.menu_on:
            self.menu_frame.place(x=15, y=60)
            self.menu_frame.tkraise()
            self.menu_on = True
        else:
            self.menu_frame.place_forget()
            self.menu_on = False

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
