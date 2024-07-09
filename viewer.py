import socket
import cv2
import numpy as np
import zlib
import struct

def recvall(sock, count):
    buf = b''
    while count:
        new_buf = sock.recv(count)
        if not new_buf:
            return None
        buf += new_buf
        count -= len(new_buf)
    return buf

def start_viewer():
    host = '0.0.0.0'  # Server IP address (your IP)
    port = 8000  # Port to listen on
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for a single connection

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            while True:
                # Receive length of the payload
                len_str = recvall(client_socket, 4)
                if not len_str:
                    break
                length = struct.unpack('!I', len_str)[0]

                # Receive the compressed frame data
                frame_data = recvall(client_socket, length)
                if not frame_data:
                    break

                # Decompress the frame
                frame_data = zlib.decompress(frame_data)
                frame = np.frombuffer(frame_data, dtype=np.uint8)

                # Reshape the array to the original frame size
                frame = frame.reshape((480, 640, 3))

                # Display the frame
                cv2.imshow('Remote Desktop Viewer', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            cv2.destroyAllWindows()
            client_socket.close()

if __name__ == "__main__":
    start_viewer()
