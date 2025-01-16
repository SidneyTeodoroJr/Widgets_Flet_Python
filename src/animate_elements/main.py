import flet as ft
import asyncio

def main(page: ft.Page):
    #Initial page settings
    page.title = "Animate Elements"  
    page.theme_mode = ft.ThemeMode.LIGHT  
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  

    # Asynchronous function to perform the animation
    async def animate():
        while True:  # Infinite loop to switch animations
            # Fist state of animation
            image.rotate.angle = -6.5  
            image.opacity = 1  
            image.offset.y = -0.5  
            image.scale.scale = 2.5  
            image.update()  
            await asyncio.sleep(5)  

            # Second state of animation
            image.rotate.angle = 0  
            image.opacity = 0.2 
            image.offset.y = 0  
            image.scale.scale = 1  
            image.update()  
            await asyncio.sleep(5)  

    image = ft.Image(
        src="icon.png",   
        width=100,  
        height=100,  

        # Rotation setting and associated animation
        rotate=ft.Rotate(angle=0),
        animate_rotation=ft.animation.Animation(3000, ft.AnimationCurve.EASE_IN),

        # Opacity setting and associated animation
        opacity=0,
        animate_opacity=ft.animation.Animation(3000, ft.AnimationCurve.EASE_IN),

        # Displacement setting and associated animation
        offset=ft.Offset(x=0, y=0),
        animate_offset=ft.animation.Animation(3000, ft.AnimationCurve.EASE_IN),

        # Scale setting and associated animation
        scale=ft.Scale(scale=1),
        animate_scale=ft.animation.Animation(3000, ft.AnimationCurve.EASE_IN),
    )

    page.add(
        image
    )

    page.run_task(animate)
    page.update()
if __name__ == '__main__':
    ft.app(target=main)  