from flet import Page, app, ThemeMode, TextField, TextStyle, Icons
import asyncio


def main(page: Page):
    page.title = "Animated Text Field"
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    class Text_Field(TextField):
        def __init__(self, hint_text: str):
            super().__init__()
            self.width = 400
            self.hint_text = hint_text
            self.hint_style = TextStyle(
                size=15
            )
            self.text_style = TextStyle(
                size=15
            )
            self.prefix_icon = Icons.SEARCH
            self.autofocus = True

        async def placeholder_auto(self):
            placeholder: str = self.hint_text
            while True:
                # Simulate typing
                self.hint_text = ""
                for letter in placeholder:
                    self.hint_text += letter
                    page.update()
                    await asyncio.sleep(0.1)  

                await asyncio.sleep(1.5)  

                # Simulate deletion
                for i in range(len(placeholder)):
                    self.hint_text = placeholder[:-1 - i]
                    page.update()
                    await asyncio.sleep(0.1)  

                await asyncio.sleep(1.5)  # Pause before restarting the animation

    async def start_animation():
        textfield = Text_Field(hint_text="Do a search...")
        page.add(textfield)
        page.update()
        await textfield.placeholder_auto()

    
    asyncio.run(start_animation()) # Run the animation


if __name__ == "__main__":
    app(target=main)