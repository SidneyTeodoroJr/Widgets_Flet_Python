import time
import flet as ft 

def main(page:ft.Page):
    page.padding=0
    page.theme_mode=ft.ThemeMode.DARK
    page.title = "SideBar and GridView"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thumb_color=ft.Colors.ON_SURFACE,))
    page.update()

    # Function to switch the theme
    def toggle_theme(e):
        e.control.selected = not e.control.selected
        e.control.update()

        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()  # Update the interface to apply the new theme


    def animacao(e):
        menu.scale = 0.8
        page.update()
        time.sleep(0.05)
        menu.scale = 1
        page.update()

        if side_bar.content.width == 60:
            side_bar.content.width = 200
            divider.width = 200
            page.update()
        elif side_bar.content.width == 200:
            side_bar.content.width = 60
            divider.width = 60
            page.update()

    side_bar=ft.Container(
           content=ft.Container(
               width=60,
               padding=10,
               margin=3,
               border_radius=16,
               animate=ft.Animation(duration=400,curve=ft.AnimationCurve.LINEAR),
               bgcolor=ft.Colors.OUTLINE_VARIANT,
               content=ft.Column(
                   horizontal_alignment='center',
                   spacing=20,
                   controls=[
                       menu:=ft.Container(
                           ft.Icon(name=ft.Icons.MENU, color=ft.Colors.OUTLINE),
                           width=30,
                           height=30,
                           bgcolor=ft.Colors.WHITE,
                           border_radius=5,
                           scale=1,
                           alignment=ft.alignment.center,
                           animate_scale=ft.Animation(duration=50,curve=ft.AnimationCurve.BOUNCE_IN),
                           on_click=animacao,
                       ),
                       ft.Container(
                           ink=True,
                           on_click=lambda _: print("HOME"),
                           border_radius=16,
                           content=ft.Row(
                               controls=[
                                   ft.IconButton(
                                       icon=ft.Icons.HOME,
                                       icon_color=ft.Colors.WHITE,
                                       on_click=lambda _: print("HOME"),
                                   ),
                                   ft.Text(
                                       "Home",
                                       color=ft.Colors.WHITE
                                   )
                               ]
                           )
                       ),
                       ft.Container(
                           ink=True,
                           on_click=lambda _: print("SEARCH"),
                           border_radius=16,
                           content=ft.Row(
                               controls=[
                                   ft.IconButton(
                                       icon=ft.Icons.SEARCH,
                                       icon_color=ft.Colors.WHITE,
                                       on_click=lambda _: print("SEARCH"),
                                   ),
                                   ft.Text(
                                       "Search",
                                       color=ft.Colors.WHITE
                                   )
                               ]
                           )
                       ),
                       ft.Container(
                           border_radius=16,
                           content=ft.Row(
                               controls=[
                                   ft.IconButton(
                                       icon=ft.Icons.DARK_MODE,
                                       selected_icon=ft.Icons.LIGHT_MODE,
                                       icon_color=ft.Colors.WHITE,
                                       selected_icon_color=ft.Colors.WHITE,
                                       on_click=toggle_theme,
                                   ),
                                   ft.Text(
                                       "Theme Mode",
                                       color=ft.Colors.WHITE
                                   )
                               ]
                           )
                       ),
                       
                       divider:=ft.Container(
                           width=60,
                           height=1,
                           animate=ft.Animation(curve=ft.AnimationCurve.LINEAR,duration=1000),
                           bgcolor=ft.Colors.WHITE
                       ),

                       ft.Container(
                           ink=True,
                           on_click=lambda e: page.window_close(),
                           border_radius=16,
                           content=ft.Row(
                               controls=[
                                   ft.IconButton(
                                       icon='LOGOUT',
                                       icon_color=ft.Colors.WHITE,
                                       on_click=lambda e: page.window_close()
                                   ),
                                   ft.Text(
                                       "Logout",
                                       color=ft.Colors.WHITE
                                   )
                               ]
                           )
                       ),
                   ]
               )
           )
       )
    

    img = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    for i in range(347):
        img.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/300?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                filter_quality=ft.FilterQuality.LOW,
                border_radius=ft.border_radius.all(10),
            )
        )

    row=ft.Row(
        expand=True,
        spacing=0,
        wrap=False,
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            side_bar,
            ft.Container(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            img
                        ], 
                        scroll=ft.ScrollMode.AUTO,
                    )
                ),
                
                width=1260 ,
                margin=5,
                padding=5,
                bgcolor=ft.Colors.OUTLINE_VARIANT,
                border_radius=16,
                alignment=ft.alignment.top_center,
            )
        ]
    )  

    page.add(
        row,
        
    )
    page.update()
if __name__ == '__main__':
    ft.app(target=main)