import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.theme_mode = ft.ThemeMode.DARK
    page.window_frameless = True
    page.window_min_height = 920
    page.window_min_width = 920
    page.window_max_height = 1080
    page.window_max_width = 2560
    page.spacing = 0
    page.padding = 0 

    widthscr = page.window_width

    # Função para alternar o tema
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()  # Atualiza a interface para aplicar o novo tema

    # Layout da barra superior
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
                                    icon=ft.icons.COLOR_LENS_OUTLINED, icon_color=ft.colors.WHITE,
                                    on_click=toggle_theme 
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