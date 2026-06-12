import asyncio
import random

import flet as ft

from main import processCommand


def main(page: ft.Page):
    page.window.height = 500
    page.window.width = 380
    page.window.always_on_top = True
    page.window.alignment = ft.Alignment.BOTTOM_LEFT
    page.window.brightness = ft.Brightness.DARK
    page.padding = 0

    # --- THE TYPEWRITER EFFECT FUNCTION ---
    async def typewriter_effect(ui_text_control, full_text, delay=0.06):
        """Reveals text letter by letter in the GUI."""
        current_text = ""
        for letter in full_text:
            current_text += letter
            # print("log:::", letter)
            ui_text_control.value = current_text
            page.update()
            delay = random.random() * 0.09
            # print("time---", delay)
            await asyncio.sleep(delay)  # Yields control so Flet can render

    async def send_click(e):
        user_message = new_message.value.strip()
        if not user_message:
            return

        # Instantly display user message
        chat.controls.append(
            ft.Text(
                f"You: {user_message}",
                color=ft.Colors.BLUE_400,
                align=ft.Alignment.CENTER_RIGHT,
                text_align=ft.TextAlign.RIGHT,
                margin=ft.Margin(right=12),
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
        padding=8,
        adaptive=True,
    )

    # A new message entry form
    new_message = ft.TextField(
        hint_text="Give me a command...",
        autofocus=True,
        shift_enter=True,
        border_width=1.2,
        border_radius=30,
        expand=True,
        on_submit=send_click,
    )

    def toogle_chip_click(e):
        for chip in chip_list:
            if chip.selected:
                # print("chip clicked", chip.label.value)
                new_message.value = chip.label.value
                chip.selected = False
        page.update()

    chip_list: list[ft.Chip] = [
        ft.Chip(
            label=ft.Text(tag, color=ft.Colors.BLUE_GREY_300, size=13),
            shape=ft.RoundedRectangleBorder(radius=15),
            padding=0,
            selected=False,
            show_checkmark=False,
            on_select=toogle_chip_click,
        )
        for tag in [
            "tell me about flet in python",
            "What is the time",
            "tell me a joke",
            "play believer",
            "open desktop",
            "search youtube python tutorial",
            "open downloads folder",
            "today date",
            "today's news",
            "open pictures",
            "open documents",
            "Open gmail",
            "open whatsapp",
            "Open notepad",
            "open calculator",
            "open github",
        ]
    ]

    def toogle_chip_expand():
        if chips_row.wrap is False:
            chips_row.wrap = True
            chip_toogle_icon.content = ft.Icon(ft.Icons.EXPAND_MORE_OUTLINED)
        else:
            chip_toogle_icon.content = ft.Icon(ft.Icons.EXPAND_LESS_OUTLINED)
            chips_row.wrap = False

    chip_toogle_icon = ft.Container(
        content=ft.Icon(ft.Icons.EXPAND_LESS_OUTLINED),
        on_click=toogle_chip_expand,
    )

    page.add(
        chat,
        ft.Container(
            padding=12,
            border_radius=20,
            bgcolor=ft.Colors.BLACK_26,
            expand_loose=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                spacing=4,
                controls=[
                    ft.Row(
                        spacing=2,
                        controls=[
                            chip_toogle_icon,
                            ft.Text(
                                "Sample Commands ..",
                                size=11,
                                color=ft.Colors.BLUE_GREY_200,
                            ),
                        ],
                    ),
                    ft.Container(
                        chips_row := ft.Row(
                            controls=chip_list,
                            wrap=False,
                            tight=True,
                            spacing=5,
                            run_spacing=7,
                        ),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    ),
                    ft.Row(
                        margin=ft.Margin(top=8),
                        spacing=2,
                        controls=[
                            new_message,
                            ft.IconButton(
                                icon=ft.Icons.SEND_ROUNDED,
                                adaptive=True,
                                icon_size=35,
                                on_click=send_click,
                            ),
                        ],
                    ),
                ],
            ),
        ),
    )


ft.run(main)
