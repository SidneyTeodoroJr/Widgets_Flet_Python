from flet import UserControl, Text, colors

class CustomText(UserControl):
    def __init__(self, value:str, color=ft.colors.TEAL_400, size=30):
        super().__init__()

        self.value=value
        self.color=color
        self.size=size

    def build(self):
        return Text(
            value=self.value,
            color=self.color,
            size=self.size
        )