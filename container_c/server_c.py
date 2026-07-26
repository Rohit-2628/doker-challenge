from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
import time

class RealVaultServer(BaseHTTPRequestHandler):
    def do_POST(self):
        time.sleep(0.5)  # Keeps connection alive for pspy
        
        length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        if self.path == '/api/vault/unlock':
            auth = params.get('auth', [''])[0]
            if auth == "4d61737465724b6579466f72436f6e7461696e657243":
                flag = os.environ.get('FLAG', 'flag{local_test_dynamic_flag_999}')
                
                banner = f"""
\033[32m
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗███████╗
 ██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██╔════╝
 ██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║███████╗
 ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║╚════██║
 ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝

                 VAULT UNLOCKED SUCCESSFULLY!
                 
         FLAG: {flag}
\033[0m
"""
                self.send_response(200)
                self.end_headers()
                self.wfile.write(banner.encode('utf-8'))
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"FAIL: Invalid Vault Key.\n")

HTTPServer(('127.0.0.1', 8080), RealVaultServer).serve_forever()
