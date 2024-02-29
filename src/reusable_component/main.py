import flet 
from flet import Page

from customText import CustomText

text="Variable text"

def main(page:Page):
    page.title="Reusable Component"
    page.theme_mode=flet.ThemeMode.SYSTEM

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
flet.app(target=main)