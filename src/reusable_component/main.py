import flet as ft

from customText import CustomText

text="Variable text"

def main(page:ft.Page):
    page.title="Reusable Component"
    page.theme_mode=ft.ThemeMode.LIGHT

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
ft.app(target=main)