import socket
import sys

def check_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} on {host} is open")
        else:
            print(f"Port {port} on {host} is closed")
        s.close()
    except socket.error:
        print("Socket error occurred")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python network_tool.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    if check_host(host):
        print(f"Host {host} is reachable")
    else:
        print(f"Host {host} is not reachable")
        sys.exit(1)
    scan_port(host, port)
