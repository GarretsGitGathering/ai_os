from flask import Flask, request, jsonify
import socket
import threading

app = Flask(__name__)

def process_prediction(data):
    data = "placeholder for returned prediction!"
    return data

def tcp_listener():
    host = '0.0.0.0'
    port = 12345

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind((host, port))
    tcp_server.listen(5)

    print(f"TCP server listening on {host}:{port}")

    while True:
        client_socket, client_address = tcp_server.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024).decode("utf-8")
        print(f"Received data: {data}")

        processed_data = process_prediction(data)

        client_socket.send(processed_data.encode("utf-8"))

        client_socket.close()

def start_flask_server():
    print("Starting Flask server...")
    app.run(debug=True, use_reloader=False, threaded=True, host='0.0.0.0', port=5000)

def stop_flask_server():
    print("Stopping Flask server...")
    # Placeholder for actual server stop logic
    # For demonstration purposes, let's just print a message
    print("Flask server stopped.")

@app.route('/', methods=['POST'])
def handle_request():
    data = request.get_data(as_text=True)
    processed_data = process_prediction(data)
    return jsonify({'result': processed_data})

if __name__ == '__main__':
    flask_server_thread = threading.Thread(target=start_flask_server)
    flask_server_thread.start()

    tcp_thread = threading.Thread(target=tcp_listener)
    tcp_thread.start()
