import warnings
# Ignore DeprecationWarnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import flet as ft
import pyrebase

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyCjqe_WnYvkMOcden9lyrRkMT0SNozhkpI",
    "authDomain": "test-f6c46.firebaseapp.com",
    "projectId": "test-f6c46",
    "storageBucket": "test-f6c46.firebasestorage.app",
    "databaseURL": "https:test.firebaseio.com",
    "messagingSenderId": "603688969277",
    "appId": "1:603688969277:web:96b781c3cea1a2fb327654",
    "measurementId": "G-00HNE9YVES"
}

# Firebase initialization
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def main(page: ft.Page):
    page.title = "Login Firebase"
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

    # Login function with validation
    def btn_login(e):
        if not user.value or not password.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please fill in all fields."),
                bgcolor=ft.colors.RED,
                action="OK",
                duration=3000
            )
            page.snack_bar.open = True
            page.update()
            return

        try:
            btn_login_access.disabled = True
            page.update()

            auth.sign_in_with_email_and_password(user.value, password.value)

            page.snack_bar = ft.SnackBar(
                content=ft.Text("User logged in successfully!"),
                bgcolor=ft.colors.GREEN,
                action="OK",
                duration=3000
            )
            user.value = ""
            password.value = ""
        except Exception as e:
            print(f"Login error: {e}"),
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Invalid username or password!"),
                bgcolor=ft.colors.RED,
                action="OK",
                duration=3000
            )
            user.value = ""
            password.value = ""
        finally:
            page.snack_bar.open = True
            btn_login_access.disabled = False
            page.update()

    # Registration function with validation
    def btn_register(e):
        if not user.value or not password.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Please fill in all fields."),
                bgcolor=ft.colors.RED,
                action="OK",
                duration=3000
            )
            page.snack_bar.open = True
            page.update()
            return

        try:
            btn_register_user.disabled = True
            page.update()

            auth.create_user_with_email_and_password(user.value, password.value)

            page.snack_bar = ft.SnackBar(
                content=ft.Text("User registered successfully!"),
                bgcolor=ft.colors.GREEN,
                action="OK",
                duration=3000
            )
            user.value = ""
            password.value = ""
        except Exception as e:
            print(f"Registration error: {e}"),
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Enter a valid email and password!"),
                bgcolor=ft.colors.RED,
                action="OK",
                duration=3000
            )
            user.value = ""
            password.value = ""
        finally:
            page.snack_bar.open = True
            btn_register_user.disabled = False
            page.update()

    # Input fields and buttons
    user = ft.TextField(
        label="Email",
        text_size=15,
        text_style=ft.TextStyle(color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(20),
        width=350,
        height=45,
        prefix=ft.Icon(ft.icons.EMAIL, size=20, color=ft.colors.BLACK87),
        tooltip="Email",
    )

    password = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        text_size=15,
        text_style=ft.TextStyle(color=ft.colors.BLACK),
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(20),
        width=350,
        height=45,
        prefix=ft.Icon(ft.icons.LOCK, size=20, color=ft.colors.BLACK87),
        tooltip="Password",
    )

    btn_login_access = ft.ElevatedButton("Login",
        bgcolor=ft.colors.PINK_ACCENT_100,
        color=ft.colors.WHITE,
        width=200,
        height=40,
        tooltip="Login",
        on_click=btn_login,
    )

    btn_register_user = ft.ElevatedButton("Register",
        color=ft.colors.BLACK,
        width=130,
        height=40,
        bgcolor=ft.colors.WHITE,
        tooltip="Register",
        on_click=btn_register,
    )

    # Interface layout
    background = ft.Container(
        width=1280,
        height=720,
        margin=ft.margin.all(-10),
        image_src="https://4kwallpapers.com/images/walls/thumbs_3t/18139.png",
        image_fit=ft.ImageFit.COVER,
        alignment=ft.alignment.top_center,
        content=ft.Column(
            [
                ft.Icon(
                    ft.icons.PERSON, size=100, color=ft.colors.WHITE, tooltip="User"
                ),
                user,
                password,
                ft.Row(
                    [btn_login_access, btn_register_user],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
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
ft.app(main)