import flet as ft

class CustomText(UserControl):
    def __init__(self, value:str, color=ft.Colors.TEAL_400, size=30):
        super().__init__()

        self.value=value
        self.color=color
        self.size=size

    def build(self):
        return ft.Text(
            value=self.value,
            color=self.color,
            size=self.size
        )