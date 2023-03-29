from flask import Flask, request

app = Flask(__name__)


@app.route('/payload_length', methods=['POST'])
def payload_length():
    # Get the payload from the request body
    payload = request.get_data(as_text=True)

    # Calculate the length of the payload
    length = len(payload)

    # Return the length as a response
    return str(length)


@app.route('/', methods=['GET'])
def check_health():
    return 'Good'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
