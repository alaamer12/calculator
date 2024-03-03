"""The model module."""


class Model:
    """The model class."""

    def __init__(self):
        """Initialize the model."""
        self.value = ""

    def calculate(self, caption):
        if isinstance(caption, int):
            self.value += str(caption)
        else:
            actions = {
                "C": lambda: "",
                "+/-": lambda: self.value[1:] if self.value[0] == "-" else "-" + self.value,
                ".": lambda: self.value + "." if "." not in self.value else self.value,
                "%": lambda: self.value + "%" if "%" not in self.value else self.value,
                "/": lambda: self.value + "/" if "/" not in self.value else self.value,
                "*": lambda: self.value + "*" if "*" not in self.value else self.value,
                "-": lambda: self.value + "-" if "-" not in self.value else self.value,
                "+": lambda: self.value + "+" if "+" not in self.value else self.value,
                "=": lambda: str(round(eval(self.value), 3))
            }
            self.value = actions.get(caption, lambda: self.value)()
        return self.value
