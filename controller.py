"""The controller module."""
from model import Model
from view import View


class Controller:
    """The controller class."""

    def __init__(self):
        """Initialize the model."""
        self.model = Model()
        self.view = View(self)

    def main(self):
        return self.view.main()

    def on_button_click(self, caption):
        result = self.model.calculate(caption)
        print(result)
        return self.view.var.set(result)
