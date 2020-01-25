#!/usr/bin/python3


import socketserver
import threading
import hashlib
import base64
from helper import decrypt


expected = "267373db136a3009cc4d5e9c5bebdaf784a7b6417f395867f62f1a17409c11de406afcd8f90999b6e0eab87e76cf1dfb9c19e80d2ef4c53436bc7242f60afa0f"
not_really_expected = "8729a835b911bb3b8e75e2d2f204ec1e0f47ca1ae297a68f346f2c42035ebeb60da714407f4661bee7f87a64c4108da6ffc05f6d37e5756fa9eef053ad13ea42"
hint = "MjE4MDk4NDIxOTA4NDIxMCVi0z6Jb6xB6hIM6tbMV5OQeEyRLt6AW+m309j1nbrfBeJ2bBazgjnlalHbRHE0Q0H5JYAb/7xT7p8yD7vk6M+Ko3JtsBN9xXHQwCiIrnlv"
success = "MjE4MDk4NDIxOTA4NDIxMFGMCXTHTjD75KIaRhIh7puYhbQBnl1m2OjF3TFWwwrp"

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f'Connected {self.client_address[0]}')
        self.print_logo()
        self.my_print("Enter your password :")
        while not self.test_pwd(str(self.request.recv(1024), "ascii").rstrip("\n")):
            self.my_print("Enter your password :")

    def test_pwd(self, pwd):
            hashed_pwd = self.hash(pwd)
            print(f'hash : {hashed_pwd}')
            if hashed_pwd == expected:
                self.my_print(decrypt(success, pwd))
                return True
            elif hashed_pwd == not_really_expected:
                self.my_print(decrypt(hint, pwd))
            return False

    def hash(self, s):
        stripped = str(s).encode("utf-8")
        print(f'Testing password : {stripped}')
        return hashlib.sha512(stripped).hexdigest()

    def print_logo(self):
        self.my_print("")
        self.my_print("***************************************************")
        self.my_print("   Welcome to the enrollment administration panel")
        self.my_print("***************************************************")
        self.my_print("")
        self.my_print("          _______\)%%%%%%%%._               ")
        self.my_print("         `''''-'-;   % % % % %'-._          ")
        self.my_print("                 :b) \            '-.       ")
        self.my_print("                 : :__)'    .'    .'        ")
        self.my_print("                 :.::/  '.'   .'            ")
        self.my_print("                 o_i/   :    ;              ")
        self.my_print("                        :   .'              ")
        self.my_print("                         ''`                ")
        self.my_print("")

    def my_print(self, s):
      self.request.sendall((f'{s}\r\n').encode())


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 27777

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    # Create the server, binding to outside on port 27777
    with server:
        server_thread = threading.Thread(target=server.serve_forever)

        server_thread.daemon = True
        server_thread.start()

        while not input("\nPress q to stop server") == "q":
            pass

        server.server_close()
