from flet import (
    Page, app, Container, Colors, alignment, padding, Border, 
    border_radius, BorderSide, Text, ImageFit, Blur, FontWeight
) 

def main(page: Page):
    page.title = "Glass Effect"
    page.padding=0
        
    layout=Container(
        image_src='https://4kwallpapers.com/images/walls/thumbs_3t/7114.jpg',
        image_fit=ImageFit.COVER,
        expand=True,
        alignment=alignment.center,
        content=Container(
            padding=padding.symmetric(vertical=30, horizontal=60),
            bgcolor=Colors.with_opacity(0.1, Colors.BLUE),
            border_radius=border_radius.all(5),
            border=Border(
                bottom=BorderSide(width=5, color=Colors.WHITE30),
                right=BorderSide(width=5, color=Colors.WHITE30),
            ),
            blur=Blur(sigma_x=10, sigma_y=10),
            ink=True,
            on_click=lambda e: page.launch_url("https://www.instagram.com/sidneyteodoroaraujo/"),
            content=Text(value="@sidneyteodoroaraujo / +55 (27) 99648-9123", size=25, color=Colors.WHITE, weight=FontWeight.BOLD)
        )
    )
    
    page.add(
        layout
    )
        
app(main)