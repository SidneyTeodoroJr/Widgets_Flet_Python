import flet as ft
def main(page: ft.Page):
    page.title= "Carousel"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Scrollbar
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.Colors.WHITE,)
    )

    # Floating Action Button
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        bgcolor=ft.Colors.WHITE,
        foreground_color=ft.Colors.PURPLE_300,
        highlight_elevation=16,
        shape=ft.RoundedRectangleBorder(radius=30),
        tooltip="ADD",
        on_click=lambda e: print("ADD clicked!"),
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar = ft.AppBar(
        title=ft.Text("Modern AppBar", color=ft.Colors.WHITE),
        center_title=True,
        bgcolor=ft.Colors.PURPLE_400,
        automatically_imply_leading=False,
    )
    
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.Colors.PURPLE_400,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE, tooltip= "Menu", on_click=lambda e: print("Menu clicked!"),),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE, tooltip= "search", on_click=lambda e: print("search clicked!"),),
                ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE, tooltip= "Favorite", on_click=lambda e: print("Favorite clicked!"),),
            ]
        ),
    )

    # Card Carousel
    card = ft.Row(
        expand=False,
        wrap=False,
        scroll="AUTO",
        controls=[
                ft.Container(
                    content=ft.Text(f"Card {i}", color=ft.Colors.WHITE, size=25),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.Colors.PURPLE_900,
                    width=415,
                    height=200,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Card clicked!"),
                )for i in range(1,5)
        ]
    )

    image = ft.Row(
        expand = False,
        wrap = False,
        scroll="AUTO",
        controls = [
            ft.Image(
                src = f"https://picsum.photos/200/200?{i}",
                width = 200,
                height = 200,
                fit = ft.ImageFit.NONE,
                repeat = ft.ImageRepeat.NO_REPEAT,
                filter_quality= ft.FilterQuality.LOW,
                border_radius = ft.border_radius.all(10)
            ) for i in range(50)
        ]
    )

    image_container = ft.Row(
        expand = False,
        wrap = False,
        scroll="AUTO",
        controls = [
                ft.Stack([
                    ft.Image(
                        src=f"https://picsum.photos/300/300?{i}",
                        fit=ft.ImageFit.CONTAIN,
                        repeat = ft.ImageRepeat.NO_REPEAT,
                        border_radius=10,
                        filter_quality= ft.FilterQuality.LOW
                    ),
                    ft.Column([
                        ft.IconButton(
                            icon=ft.icons.PLAY_CIRCLE_FILL_ROUNDED,
                            icon_color= ft.colors.WHITE,
                            icon_size= 40,
                            tooltip= "Play",
                            on_click=lambda e: print("Play")
                        ),
                    ],alignment=ft.MainAxisAlignment.END,),
                ],
                width=310,
                height=300,
            ) for i in range(1,5)
        ]
    )

    page.add(
        card, 
        image,
        image_container,
    )

    page.update()
ft.app(main)