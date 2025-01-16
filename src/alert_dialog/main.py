from flet import (
    Page, app, AlertDialog, Text, 
    TextButton, MainAxisAlignment, ElevatedButton
)


def main(page: Page):
    page.title = "AlertDialog examples"

    dlg = AlertDialog(
        title=Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete all those files?"),
        actions=[
            TextButton("Yes", on_click=close_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()


    page.add(
        ElevatedButton("Open dialog", on_click=open_dlg),
        ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )


app(target=main, assets_dir="assets")