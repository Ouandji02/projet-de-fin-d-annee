from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from components.Header.Header import Header


class AppLayout:
    def __init__(self) -> None:
        self.header = Header()

    def render(self):
        return dmc.MantineProvider(
            theme={
                "fontFamily": "'Poppins', sans-serif",
                "components": {
                    "Button": {
                        "styles": {
                            "root": {
                                "fontWeight": 400,
                            },
                        }
                    },
                    "Alert": {
                        "styles": {
                            "title": {"fontWeight": 500},
                        },
                    },
                    "AvatarGroup": {
                        "styles": {
                            "truncated": {"fontWeight": 500},
                        },
                    },
                },
            },
            withGlobalStyles=True,
            withNormalizeCSS=True,
            children=[
                self.header.render(),
                dmc.Button("Settings"),
            ],
        )
