import asyncio
from concurrent.futures import ThreadPoolExecutor
import random

import flet as ft

from main import processCommand

# from speech import speak


def main(page: ft.Page):
    page.window.height = 500
    page.window.width = 380
    page.window.always_on_top = True
    page.window.alignment = ft.Alignment.BOTTOM_LEFT
    page.window.brightness = ft.Brightness.DARK

    # --- THE TYPEWRITER EFFECT FUNCTION ---
    async def typewriter_effect(ui_text_control, full_text, delay=0.06):
        """Reveals text letter by letter in the GUI."""
        current_text = ""
        for letter in full_text:
            current_text += letter
            print("log:::", letter)
            ui_text_control.value = current_text
            page.update()  # Use the async update method
            delay = random.random() * 0.09
            print("time---", delay)
            await asyncio.sleep(delay)  # Yields control so Flet can render

    # def send_click(e):
    #     chat.controls.append(ft.Text(new_message.value))
    #     data = new_message.value
    #     new_message.value = ""
    #     speak(data)
    #     response_data = processCommand(data)
    #     chat.controls.append(
    #         ft.Card(
    #             ft.Text(response_data or "no response"),
    #         )
    #     )
    #     page.update()

    async def send_click(e):
        user_message = new_message.value.strip()
        if not user_message:
            return

        # 1. Instantly display user message
        chat.controls.append(
            ft.Text(
                f"You: {user_message}",
                color=ft.Colors.BLUE_400,
                align=ft.Alignment.CENTER_RIGHT,
                text_align=ft.TextAlign.RIGHT,
            )
        )
        new_message.value = ""
        page.update()

        response_data = processCommand(user_message)
        if not response_data:
            response_data = "Command executed successfully."

        assistant_text = ft.Text("")
        chat.controls.append(
            ft.Card(
                content=ft.Container(
                    content=assistant_text,
                    padding=10,
                )
            )
        )
        page.update()
        await typewriter_effect(assistant_text, response_data)

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
