from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import time

class DecoyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        time.sleep(0.5) 
        
        length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        # TRAP DOOR 1: The Login Endpoint (Port 8001)
        if self.server.server_port == 8001 and self.path == '/api/login':
            submitted_token = params.get('token', [''])[0]
            try:
                with open('/auth_sync/current_token.txt', 'r') as f:
                    live_token = f.read().strip()
            except:
                live_token = "error"

            if submitted_token == live_token and submitted_token != "":
                login_banner = """
\033[33m
 ███████╗██╗   ██╗███████╗    ███████╗██╗   ██╗████████╗██╗  ██╗
 ██╔════╝╚██╗ ██╔╝██╔════╝    ██╔════╝██║   ██║╚══██╔══╝██║  ██║
 ███████╗ ╚████╔╝ ███████╗    ███████╗██║   ██║   ██║   ███████║
 ╚════██║  ╚██╔╝  ╚════██║    ╚════██║██║   ██║   ██║   ██╔══██║
 ███████║   ██║   ███████║    ███████║╚██████╔╝   ██║   ██║  ██║
 ╚══════╝   ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
\033[0m
\033[36m
 [+] AUTHENTICATION ACCEPTED
 [+] DYNAMIC TOKEN VALIDATED
 [+] WARNING: You have compromised a Decoy Sub-System (Container A).
 [+] Fake SSH Credentials Generated -> user: decoy_admin / pass: trap123
 [+] (Hint: There is no SSH server running here. Check the Unix socket!)
\033[0m
"""
                self.send_response(200)
                self.end_headers()
                self.wfile.write(login_banner.encode('utf-8'))
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"\033[31m[!] FAIL: Token expired or invalid.\033[0m\n")

        # TRAP DOOR 2: The Vault Endpoint (Port 9000)
        elif self.server.server_port == 9000 and self.path == '/api/vault/unlock':
            auth = params.get('auth', [''])[0]
            if auth == "4465636f795661756c7450617373776f7264313233":
                troll_banner = """
\033[32m
010101010101010101010101010101010101010101010101010101010101010101
10                                                              01
01  111111111  11111110    0000000   11111110     00      00    10
10     011     011   011  011   011  011   011    11      11    01
01     110     11011110   110111110  11011110     00      00    10
10     011     011  011   011   011  011          11      11    01
01     110     110   110  110   110  110          000000  00000 10
10                                                              01
010101010101010101010101010101010101010101010101010101010101010101
\033[0m
\033[31m
 [!] ACCESS GRANTED TO DECOY ENVIRONMENT (CONTAINER A).
 [!] The Master Flag is not here. You have fallen into a honeyport.
 [!] The real offline vault is isolated behind a secure local Unix socket.
 [!] Check your pspy process monitor logs for the hidden socket path!
\033[0m
"""
                self.send_response(200)
                self.end_headers()
                self.wfile.write(troll_banner.encode('utf-8'))
            else:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"FAIL: Invalid Vault Key.\n")

def run_server(port):
    HTTPServer(('0.0.0.0', port), DecoyServer).serve_forever()

threading.Thread(target=run_server, args=(8001,)).start()
threading.Thread(target=run_server, args=(9000,)).start()
