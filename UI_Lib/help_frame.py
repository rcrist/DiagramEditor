import customtkinter as ctk
from tkinter import messagebox
from PIL import Image


class HelpFrame(ctk.CTkFrame):
    def __init__(self, window, parent, canvas):
        super().__init__(parent)
        self.window = window
        self.canvas = canvas

        self.menu_on = False

        self.menu_frame = ctk.CTkFrame(window, height=100, bg_color="white")

        about_button = ctk.CTkButton(self.menu_frame, text="About", command=self.show_about_dialog)
        about_button.pack(side=ctk.TOP,padx=5, pady=5)

        my_image = ctk.CTkImage(light_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/help.png"),
                                dark_image=Image.open
                                ("D:/EETools/DiagramEditor/icons/help.png"),
                                size=(24, 24))

        button = ctk.CTkButton(self, text="", image=my_image, width=30, command=self.show_menu)
        button.pack(side=ctk.LEFT, padx=5, pady=10)

    def show_menu(self):
        if not self.menu_on:
            self.menu_frame.place(x=100, y=60)
            self.menu_frame.tkraise()
            self.menu_on = True
        else:
            self.menu_frame.place_forget()
            self.menu_on = False

    def show_about_dialog(self):
        messagebox.showinfo("About Diagram Editor", "Diagram Editor v0.1\n" + "Author: Rick A. Crist\n" + "2023")
