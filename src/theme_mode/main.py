import flet as ft

def main(page: ft.Page):
    page.title = "page theme"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Yellow page theme with SYSTEM (default) mode
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.WHITE,
    )

    page.add(
        # Page theme
        ft.Container(
            content=ft.ElevatedButton("Page theme button"),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,  # Correção aqui
            padding=20,
            width=300,
        ),

        # Inherited theme with primary color overridden
        ft.Container(
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.BLUE)),
            content=ft.ElevatedButton("Inherited theme button"),
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # Correção aqui
            padding=20,
            width=300,
        ),

        # Unique always DARK theme
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Unique theme button"),
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,  # Correção aqui
            padding=20,
            width=300,
        ),
    )

ft.app(main)