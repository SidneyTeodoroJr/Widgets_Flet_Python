from flet import Page, ThemeMode, app
from customText import CustomText  # Certifique-se de que o arquivo customText.py está no mesmo diretório ou no caminho correto

text = "Variable text"

def main(page: Page):
    page.title = "Reusable Component"
    page.theme_mode = ThemeMode.SYSTEM

    page.add(
        CustomText(
            value="Your text here"
        ),
        CustomText(
            value=text,
            size=15
        )
    )

    page.update()

if __name__ == "__main__":
    app(target=main)