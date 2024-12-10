import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True

    # Gerenciar eventos de janela
    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window.prevent_close = True
    page.window.on_event = window_event

    # Funções do diálogo
    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    # Configuração do diálogo de confirmação
    confirm_dialog = ft.AlertDialog(
        bgcolor=ft.colors.BLACK,
        modal=True,
        title=ft.Text(
            "Por favor confirme",
            text_align=ft.TextAlign.CENTER,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.W_600,
        ),
        content=ft.Text(
            "Deseja realmente sair?",
            text_align=ft.TextAlign.CENTER,
            color=ft.colors.WHITE,
            size=15,
        ),
        actions=[
            ft.ElevatedButton("Yes", on_click=yes_click, bgcolor=ft.colors.WHITE),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    # Adicionar componentes na página
    page.add(
        ft.Row(
            [
                ft.WindowDragArea(
                    ft.Container(
                        ft.Text(
                            "Teste",
                            text_align=ft.TextAlign.CENTER,
                            color=ft.colors.OUTLINE_VARIANT,
                        ),
                        bgcolor=ft.colors.ON_SURFACE_VARIANT,
                        padding=10,
                    ),
                    expand=True,
                    maximizable=False,
                ),
                ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
            ]
        )
    )

    page.update()

ft.app(target=main)