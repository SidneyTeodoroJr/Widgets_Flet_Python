import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window.always_on_top = True  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    sample_media = [
        ft.VideoMedia("example_video.mp4"), 
    ]

    page.add(
        ft.Video(
            expand=True,
            playlist=sample_media,  
            playlist_mode=ft.PlaylistMode.LOOP,
            fill_color=ft.Colors.BLACK,  
            aspect_ratio=16 / 9,
            volume=100,
            autoplay=False,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
        )
    )

    page.update()

ft.app(target=main)