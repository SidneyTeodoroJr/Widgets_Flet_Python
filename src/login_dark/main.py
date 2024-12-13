import warnings

# Ignorar DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import flet as ft

def main(page: ft.Page):
    page.title = "Login Dark" 
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window.bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT

    page.window.maximizable = False
    page.window.minimizable = True

    page.window.width = 1280
    page.window.height = 720

    page.window.max_width = 1280
    page.window.max_height = 720
    
    page.window.min_width = 1280
    page.window.min_height = 720

    background = ft.Container(
        width=1280,
        height=720,
        margin=ft.margin.all(-10),
        image_src=os.path.join("bg-2.png"),

        image_fit=ft.ImageFit.COVER,
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                ft.Text("User", 
                        size=75, 
                        offset=ft.Offset(x=0, y=-0.2),
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                ),

               ft.TextField(label="Email", hover_color=ft.colors.BLACK26, text_size=15,
                            bgcolor=ft.colors.WHITE,
                            border_radius=ft.border_radius.all(20),
                            width=300, 
                            prefix=ft.Icon(ft.icons.EMAIL, size=20, color=ft.colors.BLACK87),
                            tooltip="Email"

               ),

               ft.TextField(label="Password", password=True, can_reveal_password=True, text_size=15,
                            hover_color=ft.colors.BLACK26,
                            bgcolor=ft.colors.WHITE,
                            border_radius=ft.border_radius.all(20),
                            width=300, 
                            prefix=ft.Icon(ft.icons.LOCK, size=20, color=ft.colors.BLACK87),
                            tooltip="password"
               ),

               ft.Switch(label="Lembrar senha", value=True,
                         label_style=ft.TextStyle(color=ft.colors.WHITE, size=15),
                         active_color=ft.colors.BLACK,
                         track_color=ft.colors.WHITE,
                         width=50,
                         offset=ft.Offset(x=-2, y=0.3)
                ),

                ft.ElevatedButton("Acessar",
                                  style=ft.ButtonStyle(
                                      text_style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD),
                                      side=ft.BorderSide(width=2, color=ft.colors.WHITE),
                                      overlay_color=ft.colors.WHITE12
                                  ),
                                  
                                  offset=ft.Offset(x=0, y=1), 
                                  bgcolor=ft.colors.BLACK, 
                                  color=ft.colors.WHITE,
                                  width=250,
                                  height=50,
                                  tooltip= "Acessar",
                                  on_click=lambda e: print("Botão clicado"),
                                  
                ),
                
                ft.Text("Não tenho conta",
                        color=ft.colors.WHITE60,
                        offset=ft.Offset(x=0, y=3.5),
                        size=15
                ),
                
                ft.Icon(name=ft.icons.ARROW_RIGHT_ALT, color=ft.colors.WHITE, size=30,
                        offset=ft.Offset(x=2.5, y=1.3),),
                
            ],
            alignment="center", 
            horizontal_alignment="center",  
        )
    )

    page.add(
        ft.Container(
            content=background,
        )
    )
    
    page.update()
ft.app(main, assets_dir=os.path.join("my-app", "assets"),)
