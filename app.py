import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.getenv("PORT", "8080"))
MESSAGE = os.getenv("DUMMY_MESSAGE", "Hello from the EDITO Generic container!")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"""
        <html>
            <head>
                <title>EDITO Generic Test</title>
            </head>
            <body>
                <h1>EDITO Generic works!</h1>
                <p>{MESSAGE}</p>
                <p>Container port: {PORT}</p>
            </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())


print(f"Starting server on 0.0.0.0:{PORT}")
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()