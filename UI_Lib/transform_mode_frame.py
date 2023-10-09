import customtkinter as ctk
import tkinter as tk


class TransformModeFrame(ctk.CTkFrame):
    def __init__(self, parent, canvas):
        super().__init__(parent)
        self.parent = parent
        self.canvas = canvas
        self.mode = "Move"

        self.radio_var = tk.IntVar(value=1)

        move_mode = ctk.CTkRadioButton(self, text="Move mode",
                                       command=self.radiobutton_event, variable=self.radio_var, value=1)
        rotate_mode = ctk.CTkRadioButton(self, text="Rotate mode",
                                         command=self.radiobutton_event, variable=self.radio_var, value=2)
        resize_mode = ctk.CTkRadioButton(self, text="Resize mode",
                                         command=self.radiobutton_event, variable=self.radio_var, value=3)

        move_mode.pack(side=ctk.LEFT, padx=5, pady=10)
        rotate_mode.pack(side=ctk.LEFT, padx=5, pady=10)
        resize_mode.pack(side=ctk.LEFT, padx=5, pady=10)

    def radiobutton_event(self):
        if self.radio_var.get() == 1:  # Move mode
            self.canvas.mouse.unbind_mouse_events()
            self.canvas.mouse.bind_move_mouse_events()
            self.canvas.mode = "Move"
        elif self.radio_var.get() == 2:  # Rotate mode
            self.canvas.mode = "Rotate"
        elif self.radio_var.get() == 3:  # Resize mode
            self.canvas.mouse.unbind_mouse_events()
            self.canvas.mouse.bind_resize_mouse_events()
            self.canvas.mode = "Resize"
