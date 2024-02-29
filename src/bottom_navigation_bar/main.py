from flet import *

def main(page: Page):

    page.padding = 0
    page.spacing = 0

    def changeposition(e):
        ids = e.control.data.controls[0].value
        print(f"You clicked button with ID: {ids}")

        # Update myContent based on the button clicked
        if ids == 0:
            myContent.content = Text("Home Content", size=30)
        elif ids == 1:
            myContent.content = Text("Bookmark Content", size=30)
        elif ids == 2:
            myContent.content = Text("Person Content", size=30)

        controls = [
            bottom_bar.content.controls[0],
            bottom_bar.content.controls[1],
            bottom_bar.content.controls[2],
        ]

        for i, control in enumerate(controls):
            control.content.controls[1].visible = (i == ids)
            control.bgcolor = e.control.data.controls[1].value if i == ids else "white"
            page.controls[0].bgcolor = e.control.data.controls[1].value

        page.update()

    bottom_bar = Container(
        bgcolor="white",
        margin=8,
        padding=3,
        left=10,
        right=10,
        width="100%",  # Alteração aqui
        border_radius=border_radius.all(30),
        content=Row([
            Container(
                bgcolor="red200",
                border_radius=30,
                padding=10,
                animate=animation.Animation(300, "cubic"),
                content=Row([
                    IconButton(icon="home",
                               icon_size=20,
                               icon_color="red300",
                               data=Row([Text(0), Text("red200")]),
                               on_click=changeposition
                    ),
                    Text("Home", size=15, visible=True)
                ])
            ),
            Container(
                bgcolor="white",
                border_radius=border_radius.all(30),
                padding=10,
                animate=animation.Animation(300, "cubic"),
                content=Row([
                    IconButton(icon="bookmark",
                               icon_size=20,
                               icon_color="blue400",
                               data=Row([Text(1), Text("blue200")]),
                               on_click=changeposition
                    ),
                    Text("Bookmark", size=15, visible=False)
                ])
            ),
            Container(
                bgcolor="white",
                border_radius=border_radius.all(30),
                padding=10,
                animate=animation.Animation(300, "cubic"),
                content=Row([
                    IconButton(icon="person",
                               icon_size=20,
                               icon_color="green300",
                               data=Row([Text(2), Text("green900")]),
                               on_click=changeposition
                    ),
                    Text("Person", size=15, visible=False)
                ])
            ),
        ], alignment="spaceBetween")
    )

    myContent = Container(
        padding=10,
        animate=animation.Animation(200, "easeIn"),
        alignment=alignment.center,
        content=Text("Welcome", size=30),
        col={"sm": 12, "md": 12, "xl": 12},
        width="100%",  # Alteração aqui
        height="100%"  # Alteração aqui
    )

    page.add(
        Container(
            width=page.window_width,
            height=page.window_height,
            animate=animation.Animation(200, "easeIn"),
            content=Stack([
                myContent,
                bottom_bar
            ]),
            col={"sm": 12, "md": 12, "xl": 12},
        )
    )

    page.update()
app(target=main)