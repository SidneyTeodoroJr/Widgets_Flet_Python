import flet as ft

def main(page: ft.Page):
    page.theme_mode= ft.ThemeMode.SYSTEM

    def runanimate(e):
        mycon.border_radius = 30 if mycon.border_radius == 0 else 0
        mycon.bgcolor = ft.colors.RED if mycon.bgcolor == ft.colors.BLUE else ft.colors.BLUE
        mycon.offset = ft.transform.Offset(0,3) if mycon.offset == ft.transform.Offset(0,0) else ft.transform.Offset(0,0)
        mycon.scale = ft.transform.Scale(scale=1) if mycon.scale == ft.transform.Scale(scale=0.5) else ft.transform.Scale(scale=0.5)
        page.update()

    mycon = ft.Container(
        bgcolor=ft.colors.RED,
        width=200,
        height=180,
        margin=ft.margin.only(top=50, left=20),
        offset= ft.transform.Offset(0,0),
        border_radius=ft.border_radius.all(30),
        animate_offset= ft.animation.Animation(duration=700, curve=ft.AnimationCurve.EASE_IN),
        scale=ft.transform.Scale(
            scale=0.5,
            alignment=ft.alignment.center
        ),
        animate_scale=ft.animation.Animation(duration=700, curve=ft.AnimationCurve.DECELERATE),
        on_click=runanimate,
    )

    page.add(
        mycon,
    )

    page.update()
ft.app(target=main)