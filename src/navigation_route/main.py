import flet as ft

def main(page: ft.Page) -> None:
    page.title = "MoviesPY"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.HIDDEN
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Scrollbar
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.Colors.WHITE,)
    )

    nav_bar = ft.NavigationBar(
        on_change=lambda e: navigate_to_page(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME_ROUNDED,
                label="Home"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.HISTORY,
                selected_icon=ft.Icons.HISTORY_TOGGLE_OFF_OUTLINED,
                label="History"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="My list",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.INFO_OUTLINED,
                selected_icon=ft.Icons.INFO_ROUNDED,
                label="Info",
            )
        ]
    )

    def navigate_to_page(selected_index: int) -> None:
        """Função para navegação baseada na seleção do NavigationBar"""
        if selected_index == 0:
            page.go("/home")
        elif selected_index == 1:
            page.go("/history")
        elif selected_index == 2:
            page.go("/list")
        elif selected_index == 3:
            page.go("/info")


    def route_change(e) -> None:
        """Função chamada quando a rota muda"""
        page.views.clear()

        # Página inicial
        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Text("Bem Vindo!", size=30),
                        ft.ElevatedButton(text="Go to APP", on_click=lambda e: page.go("/home")),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=26,
                )
            )

        # Página Home
        elif page.route == "/home":
            page.views.append(
                ft.View(
                    route="/home",
                    controls=[
                        ft.Text("Home", size=30),
                        nav_bar,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # Página History
        elif page.route == "/history":
            page.views.append(
                ft.View(
                    route="/history",
                    controls=[
                        ft.Text("History", size=30),
                        nav_bar,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # Página My list
        elif page.route == "/list":
            page.views.append(
                ft.View(
                    route="/list",
                    controls=[
                        ft.Text("My list", size=30),
                        nav_bar,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # Página Info
        elif page.route == "/info":
            page.views.append(
                ft.View(
                    route="/info",
                    controls=[
                        ft.Text("Info", size=30),
                        nav_bar,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        page.update()

    def view_pop(e, ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)