import customtkinter as ctk
from UI_Lib.hamburger_frame import HamburgerFrame
from UI_Lib.settings_frame import SettingsFrame
from UI_Lib.shape_appearance_frame import ShapeAppearanceFrame
from UI_Lib.transform_mode_frame import TransformModeFrame
from UI_Lib.snap_frame import SnapFrame
from UI_Lib.help_frame import HelpFrame


class TopFrame(ctk.CTkFrame):
    def __init__(self, parent, canvas, height):
        super().__init__(parent, height)
        self.parent = parent
        self.canvas = canvas

        frame = HamburgerFrame(parent, self, self.canvas)
        frame.pack(side=ctk.LEFT, padx=5, pady=5)

        frame = SettingsFrame(parent, self, self.canvas)
        frame.pack(side=ctk.LEFT, padx=5, pady=5)

        frame = HelpFrame(parent, self, self.canvas)
        frame.pack(side=ctk.LEFT, padx=5, pady=5)

        frame = ShapeAppearanceFrame(self, self.canvas)
        frame.pack(side=ctk.LEFT, padx=5, pady=5)

        frame = TransformModeFrame(self, self.canvas)
        frame.pack(side=ctk.LEFT, padx=5, pady=5)

        frame = SnapFrame(self, self.canvas)
        frame.pack(side=ctk.LEFT, padx=5, pady=5)


