#
# Title: echo_server.py
# Description: 
# 
#
import socket

class Solution:
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    def server2(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
            ss.bind((self.HOST, self.PORT))
            ss.listen()
 
            conn, addr = ss.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    datum = conn.recv(1024)
                    if not datum:
                        break

                    conn.sendall(datum)
    
    def client2(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs:
            cs.connect((self.HOST, self.PORT))
            cs.sendall(b"Hello, world")
            data = cs.recv(1024)
    
        print("Received", repr(data))

if __name__ == '__main__':
    print("main")

    solution = Solution()
#    solution.server2()
    solution.client2()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
