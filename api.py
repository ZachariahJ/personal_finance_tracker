from flask import Flask, jsonify, request
import openai
from main import Transactions
from datetime import date

openai.api_key = "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"
app = Flask(__name__)

Z = Transactions()

# ----------------- Use ChatGPT API ----------------- #
# https://beta.openai.com/docs/api-reference/chat

@app.route('/api/v1.0/audio', methods=['POST'])

def audio():
    # audio_data = request.files['audio'].read()
    transcript = openai.Audio.transcribe("whisper-1", 'audio')
    return "Added your transaction history."


# ----------------- SEPARATOR ----------------- #
def get_all():
    data = []

    dates = [j[0] for j in Z.read_from_db("date")]
    types = [j[0] for j in Z.read_from_db("type")]
    amounts = [j[0] for j in Z.read_from_db("amount")]
    details = [j[0] for j in Z.read_from_db("detail")]

    for date, type, amount, detail in zip(dates, types, amounts, details):
        item = {
            "date": "",
            "type": "",
            "amount": "",
            "detail": ""
        }
        item["date"] = date
        item["type"] = type
        item["amount"] = amount
        item["detail"] = detail
        data.append(item)
    return data


@app.route('/api/v1.0/transactions', methods=['GET'])
def get_transactions():
    return jsonify(get_all())


@app.route('/api/v1.0/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    Z.write_to_db(date=data["date"], type=data["type"],
                  amount=data["amount"], detail=data["detail"])
    return jsonify(get_all())


@app.route('/api/v1.0/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    Z.delete_from_db(id)
    return jsonify(get_all())


@app.route('/api/v1.0/transactions/<int:id>', methods=['PUT'])
def update_transaction(id):
    data = request.get_json()
    Z.update_db(id, data["date"], data["type"],
                data["amount"], data["detail"])
    return jsonify(get_all())


@app.route('/api/v1.0/transactions/sum', methods=['GET'])
def sum():
    result = Z.sum_of_amount()
    return str(result)


@app.route('/api/v1.0/transactions/sum/<string:type>', methods=['GET'])
def sum_by_type(type):
    result = Z.sum_of_amount_by_type(type)
    return str(result)


app.run()
