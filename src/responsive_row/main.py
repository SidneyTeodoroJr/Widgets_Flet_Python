import flet as ft

def main(page: ft.Page):
    page.theme_mode= ft.ThemeMode.DARK
    page.title= "Responsive Row"

    def page_resize(e):
        pw.value = f"{page.width, page.height} px"
        pw.update()

    page.on_resize = page_resize

    pw = ft.Text(bottom=10, right=10, style="displaySmall")
    page.overlay.append(pw)
    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text("Column 1"),
                    padding=15,
                    bgcolor=ft.colors.PURPLE,
                    col={"sm": 12, "md": 6, "xl": 4}
                ),
                ft.Container(
                    ft.Text("Column 2"),
                    padding=15,
                    bgcolor=ft.colors.GREEN,
                    col={"sm": 12, "md": 6, "xl": 4}
                ),
                ft.Container(
                    ft.Text("Column 3"),
                    padding=15,
                    bgcolor=ft.colors.PINK_300,
                    tooltip="clicked!",
                    col={"sm": 12, "md": 12, "xl": 4}
                ),
            ],
        ),


        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text("column 4"),
                    padding=15,
                    bgcolor=ft.colors.AMBER_800,
                    alignment=ft.alignment.center,
                    col={"sm": 12, "md": 6, "xl": 6}
                ),
                ft.Container(
                    ft.Text("column 5"),
                    padding=15,
                    bgcolor=ft.colors.BROWN_800,
                    alignment=ft.alignment.center,
                    on_click=lambda e: print("Mouse clicked!"),
                    on_hover=lambda e: print("Mouse hover!"),
                    tooltip="Mouse hover and Mouse clicked",
                    col={"sm": 12, "md": 6}
                ),
                ft.Container(
                    ft.Text("column 6"),
                    padding=15,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_700,
                    width=150,
                    ink=True,
                    on_click=lambda e: print("Mouse clicked"),
                    tooltip="Mouse clicked",
                    col={"md": 12}
                )
            ],
        )
    )

    page_resize(None)
    page.update()
ft.app(target=main)
