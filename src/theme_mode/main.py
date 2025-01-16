from flet import(
    Page, app, MainAxisAlignment, CrossAxisAlignment, 
    Theme, ThemeMode, Colors, Container, ElevatedButton, ColorScheme
)

def main(page: Page):
    page.title = "page theme"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.theme_mode=ThemeMode.DARK
    
    # Yellow page theme with SYSTEM (default) mode
    page.theme = Theme(
        color_scheme_seed=Colors.YELLOW
    )

    page.add(
        # Page theme
        Container(
            content=ElevatedButton("Page theme button", bgcolor=Colors.PRIMARY_CONTAINER),
            bgcolor=Colors.PRIMARY,  # Correction here
            padding=20,
            width=300,
        ),

        # Inherited theme with primary color overridden
        Container(
            theme=Theme(color_scheme=ColorScheme(primary=Colors.RED)),
            content=ElevatedButton("Inherited theme button"),
            bgcolor=Colors.ON_SURFACE_VARIANT,  # Correction here
            padding=20,
            width=300,
        ),

        # Unique always DARK theme
        Container(
            theme=Theme(color_scheme_seed=Colors.ORANGE_ACCENT),
            theme_mode=ThemeMode.LIGHT,
            content=ElevatedButton("Unique theme button"),
            bgcolor=Colors.ON_SURFACE_VARIANT,  # Correction here
            padding=20,
            width=300,
        ),
    )

app(main)