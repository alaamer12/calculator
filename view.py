"""The View module."""
import tkinter as tk
from tkinter import ttk

app = tk.Tk


class View(app):
    """The view class."""
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    BUTTON_CAPTIONS = [
        "C", "+/-", "%", "/",
        7, 8, 9, "*",
        4, 5, 6, "-",
        1, 2, 3, "+",
        0, ".", "=",
    ]

    def __init__(self, controller):
        """Initialize the model."""
        super().__init__()
        self.title("Calculator")

        self.controller = controller

        self.var = tk.StringVar()

        self._main_frame()

        self._main_entry()

        self._make_buttons()

    def main(self):
        return self.mainloop()

    def _main_entry(self):
        self.entry = ttk.Entry(self.frame, textvariable=self.var,
                               justify="right", state="disabled", cursor="arrow")
        self.entry.pack(fill="x")

    def _main_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_buttons(self):
        outer_frame = ttk.Frame(self.frame)
        outer_frame.pack()

        frame = ttk.Frame(outer_frame)
        frame.pack()

        buttons_in_row = 0

        for caption in self.BUTTON_CAPTIONS:
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frame = ttk.Frame(outer_frame)
                frame.pack()
                buttons_in_row = 0
            buttons_in_row += 1
            button = ttk.Button(frame,
                                text=caption,
                                command=(lambda _x=caption:
                                         self.controller.on_button_click(_x)))
            button.pack(side="left")
