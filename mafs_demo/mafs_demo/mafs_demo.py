"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx
from typing import List
from reflex_mafs import mafs, coordinates_cartesian, movable_point, vector, polygon

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    tail: List[float | int] = [0, 0]
    tip: List[float | int] = [1, 1]

    def move_point(self, point: list[float | int]) -> List[float | int]:
        self.tip = point

    pass


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to reflex-mafs!", size="9"),
            # rx.text(
            #     "Test your custom component by editing ", 
            #     rx.code(filename),
            #     font_size="2em",
            # ),
            rx.heading("Simple Mafs Demo with a Vector and Movable Point"),
            mafs(
                coordinates_cartesian(),
                vector(
                    tail=State.tail,
                    tip=State.tip,
                ),
                movable_point(
                    point=State.tip,
                    on_move=State.move_point,
                ),
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
