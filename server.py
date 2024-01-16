from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/sendDesiredHumidity/<int:humidity>', methods=['POST'])
def send_desired_humidity(humidity):
    f = open('desiredHumidity.txt', 'w')
    f.write(str(humidity))
    f.close()
    return jsonify({'result': True})

@app.route('/getCurrentHumidity/', methods=['GET'])
def get_current_humidity():
    f = open('currentHumidity.txt', 'r')
    current_humidity = f.read()
    f.close()
    return jsonify({'humidity': current_humidity})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")