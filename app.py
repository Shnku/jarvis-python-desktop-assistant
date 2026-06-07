import flet as ft

from main import processCommand
from speech import speak


def main(page: ft.Page):
    page.window.height = 500
    page.window.width = 380
    page.window.always_on_top = True
    page.window.alignment = ft.Alignment.BOTTOM_LEFT
    page.window.brightness = ft.Brightness.DARK

    def send_click(e):
        chat.controls.append(
            ft.Text(
                f"You: {new_message.value}",
                color=ft.Colors.BLUE_400,
                align=ft.Alignment.CENTER_RIGHT,
                text_align=ft.TextAlign.RIGHT,
            )
        )
        data = new_message.value
        new_message.value = ""
        speak(data)
        response_data = processCommand(data)
        chat.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Text(response_data),
                    padding=10,
                )
            )
        )
        page.update()

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
        adaptive=True,
    )

    # A new message entry form
    new_message = ft.TextField(
        hint_text="Give me a command...",
        autofocus=True,
        shift_enter=True,
        border_width=1.5,
        border_radius=15,
        expand=True,
        on_submit=send_click,
    )

    page.add(
        chat,
        ft.Row(
            controls=[
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND,
                    adaptive=True,
                    icon_size=30,
                    on_click=send_click,
                ),
            ]
        ),
    )


ft.run(main)
