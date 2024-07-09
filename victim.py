import socket
import cv2
import zlib
import struct
from mss import mss

def sendall(sock, data):
    sock.sendall(struct.pack('!I', len(data)) + data)

def start_server():
    host = 'SERVER_IP_ADDRESS'  # Server IP address (your IP)
    port = 8000  # Port on which the server is listening

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to {host}:{port}")

    try:
        with mss() as sct:
            monitor = sct.monitors[1]  # Change index if needed
            rect = {
                'top': monitor['top'],
                'left': monitor['left'],
                'width': 640,
                'height': 480
            }

            while True:
                # Capture screen
                img = sct.grab(rect)
                frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

                # Compress frame
                encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
                _, frame = cv2.imencode('.jpg', frame, encode_param)
                frame_data = frame.tobytes()

                # Send frame size and frame data
                sendall(client_socket, zlib.compress(frame_data))

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_server()
