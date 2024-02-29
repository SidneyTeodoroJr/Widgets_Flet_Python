import flet as ft

def main(page: ft.Page):
    page.theme_mode=ft.ThemeMode.SYSTEM
    page.window_frameless = True
    page.window_min_height = 920
    page.window_min_width = 920

    page.window_max_height = 1080
    page.window_max_width = 2560

    page.spacing = 0
    page.padding = 0 


    widthscr = page.window_width


    page.add(
        ft.ResponsiveRow([
            ft.WindowDragArea(
                ft.Container(
                    width=widthscr,
                    bgcolor=ft.colors.GREY_800,
                    padding=5,
                    content=ft.Row([
                        ft.Text(
                            "You Home", size=20, color=ft.colors.WHITE, weight=ft.FontWeight.W_600,
                            offset=(0.3, 0),
                        ),
                        ft.Container(
                            content=ft.Row([
                                ft.IconButton(
                                    icon=ft.icons.FORMAT_ALIGN_CENTER, icon_color=ft.colors.WHITE,
                                    on_click=lambda e: page.window_center()
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CLOSE, icon_color=ft.colors.WHITE,
                                    on_click=lambda e: page.window_close()
                                )
                            ])
                        )
                    ], alignment="spaceBetween")
                )
            )
        ])
    )


    page.update()
ft.app(target=main)