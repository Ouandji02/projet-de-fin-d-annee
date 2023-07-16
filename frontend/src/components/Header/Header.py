from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


class Header:
    """
    La classe du Header
    """

    def __init__(self) -> None:
        self.title = html.H2("Recognition.", style={"margin-top": 5})

    def render(self):
        # return dbc.Row(
        #     [
        #         dbc.Col(
        #             self.title,
        #             md=6,
        #             sm=6,
        #         ),
        #         # dbc.Col(self.title, md=6),
        #         dbc.Col(
        #             "Hello",
        #         ),
        #     ],
        #     style={"background-color": "red"},
        #     className="px-2",
        # )
        style = {
            "border": f"1px solid {dmc.theme.DEFAULT_COLORS['indigo'][4]}",
            "textAlign": "center",
        }
        return dmc.Stack(
            justify="center",
            style={"height": 70},
            children=dmc.Grid(
                children=[
                    dmc.Col(
                        [
                            dmc.Text("Bonjour"),
                        ],
                        span="content",
                        pt=12,
                    ),
                    dmc.Col(
                        [
                            dmc.Text("Bonjour"),
                        ],
                    ),
                ],
            ),
        )
