import Core.settings
import Core.path_handler


class WebPage:
    def __init__(self) -> None:
        ph = Core.path_handler.PathHandler()
        self._scheme = Core.settings.Settings.SCHEME
        self._host = Core.settings.Settings.HOST
        self.path_list = ph.generate_path_strings()

    def generate_html(self) -> str:
        html = "<html>\n<head>\n</head>\n<body>\n"
        for path in self.path_list:
            html += f'<a href="{self._scheme}{self._host}/{path}">{path}</a><br>\n'
        html += "</body>\n</html>"

        return html
