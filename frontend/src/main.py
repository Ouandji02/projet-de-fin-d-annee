from dash import Dash, html
from layout.app_layout import AppLayout


class Main:
    def __init__(self) -> None:
        self.app = Dash(
            __name__,
            suppress_callback_exceptions=True,
            title="PROJET DE FIN D'ANNEE",
        )
        self.layout = AppLayout()

    def run_app(self):
        self.app.layout = self.layout.render()
        self.app.run_server(debug=True, port=8080)


if __name__ == "__main__":
    print("APP START")
    Main().run_app()
