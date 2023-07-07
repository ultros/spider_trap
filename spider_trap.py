from http.server import HTTPServer, BaseHTTPRequestHandler
import Core.path_handler
import Core.webpage
import Core.settings


class Handler(BaseHTTPRequestHandler):
    '''https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET'''
    def do_GET(self):
        wp = Core.webpage.WebPage()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # wfile contains the output stream for writing a response back to the client.
        # Here we generate an HTML document string and provide it.
        self.wfile.write(wp.generate_html().encode())


def main():
    server = HTTPServer((Core.settings.Settings.HOST, Core.settings.Settings.PORT), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
