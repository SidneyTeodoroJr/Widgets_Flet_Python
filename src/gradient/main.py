import flet as ft


def main(page: ft.Page):
    page.title = "Gradient"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll=ft.ScrollMode.AUTO

    # Linear Gradient Text
    text1 = ft.Text(
        "Linear Gradient",
        text_align=ft.TextAlign.CENTER,  # Correção aqui
        selectable=True,
        size=45,
        weight=ft.FontWeight.BOLD,
        style=ft.TextStyle(
            foreground=ft.Paint(
                gradient=ft.LinearGradient(
                    begin=ft.Offset(x=0, y=0),
                    end=ft.Offset(x=400, y=0),
                    colors=[ft.Colors.DEEP_PURPLE, ft.Colors.PINK],
                )
            )
        ),
    )

    # Shader Mask Text
    text2 = ft.ShaderMask(
        content=ft.Text(  # Correção: content especificado
            value="Shader Mask",
            selectable=True,
            size=50,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
        ),
        shader=ft.LinearGradient(
            begin=ft.alignment.bottom_right,
            colors=[ft.Colors.WHITE, ft.Colors.BLUE_600],
        ),
    )

    text3= ft.Text(
        selectable=True,
        size=35,
        text_align=ft.TextAlign.CENTER,
        spans=[
            ft.TextSpan(
                text="Text with gradient ",
                style=ft.TextStyle(
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            begin=ft.Offset(x=0, y=0),
                            end=ft.Offset(x=500, y=0),
                            colors=[ft.Colors.GREEN, ft.Colors.YELLOW, ft.Colors.BLUE],
                            color_stops=[0, 0.5, 1]
                        )
                    )
                )
            ),

            ft.TextSpan(
                text="\n of various colors!",
                style=ft.TextStyle(
                    shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.WHITE),
                    size=25,
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            begin=ft.Offset(x=0, y=0),
                            end=ft.Offset(x=500, y=0),
                            colors=[ft.Colors.PURPLE_500, ft.Colors.WHITE],
                            color_stops=[0, 1]
                        )
                    )
                )
            )
        ]
    )

    # Shader Mask Image
    image = ft.ShaderMask(
        content=ft.Image(  # Correção: content especificado
            src="https://4kwallpapers.com/images/walls/thumbs_3t/20184.jpg",
            fit=ft.ImageFit.FILL,
            tooltip="Linear gradient in the image"
        ),
        shader=ft.LinearGradient(
            begin=ft.alignment.top_left,
            colors=[ft.Colors.LIGHT_BLUE_ACCENT_400, ft.Colors.PINK_300],  # Correção no uso de ft.Colors
            tile_mode=ft.GradientTileMode.CLAMP,
        ),
    )

    # Adicionando elementos à página
    page.add(
        text1,
        text2,
        text3,
        image,
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main)