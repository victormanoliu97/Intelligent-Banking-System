from flask import Flask, request
import control.service.objectiveService as objectiveService
import control.service.financialInstrumentsService as instrumentService
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/predict-objective', methods=['POST'])
def predict_objective():
    data = request.get_json()
    objectiveService.insert_objective(data['customerId'], data['income'], data['objectiveName'], data['objectiveValue'], data['years'])

    return "Success"

@app.route('/get-stocks', methods=['GET'])
def return_stocks():
    return jsonify(instrumentService.returnStocks())

@app.route('/get-forex', methods=['GET'])
def return_forex():
    return jsonify(instrumentService.returnForex())


if __name__ == '__main__':
    app.run()
