import flet as ft
def main(page: ft.Page):
    lv = ft.ListView(
        expand=5,
        spacing=10,
        item_extent=50
    )

    page.add(
        lv
    )

    for i in range(7000):
        lv.controls.append(
            ft.Container(
                    ft.Text(f"Coluna {i}"),
                    padding=15,
                    alignment=ft.alignment.top_left,
                    bgcolor=ft.colors.OUTLINE_VARIANT,
            )
        )
        if i % 100 == 0:
            page.update

    page.update()
ft.app(target=main)