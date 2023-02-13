import socket
from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def get_timestamp_and_hostname():
    host_name = socket.gethostname()
    timestamp = int(time.time())
    return jsonify({"timestamp": timestamp, "hostname": host_name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
