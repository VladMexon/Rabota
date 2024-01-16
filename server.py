from flask import Flask

app = Flask(__name__)

@app.route('/getCurrentHumidity/', methods=['GET'])
def get_current_humidity():
    f = open('currentHumidity.txt', 'r')
    current_humidity = f.read()
    f.close()
    return current_humidity

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")