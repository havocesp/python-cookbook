from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print("Got connection from", addr)
    with open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False) as client_in:
        with open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False) as client_out:

            # Echo lines back to the client using file I/O
            for line in client_in:
                client_out.write(line)
                client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

if __name__ == '__main__':
    print('Echo serving running on localhost:25000')
    echo_server(('', 25000))
