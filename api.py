from flask import Flask, jsonify, request
import openai
from main import Transactions
from datetime import date

app = Flask(__name__)

Z = Transactions()

# ----------------- Use ChatGPT API ----------------- #
# https://beta.openai.com/docs/api-reference/chat

openai.api_key = "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"


@app.route('/api/v1.0/audio', methods=['POST'])
def speech_to_text():
    audio_data = request.data
    with open("temp.mp3", "wb") as audio_file:
        audio_file.write(audio_data)
    audio = open("temp.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio)
    audio.close()
    print(transcript)
    try:
        data = text_formatting(transcript)
        Z.write_to_db(date=data[0], type=data[2],
                  amount=data[1], detail=data[3])
        return "Added your transaction history."
    except:
        ...


def text_formatting(sentence):
    today = date.today()
    info = """
    I'll give you a paragraph describing my spending or income, and you'll need to extract from the information I've given you the amount of spending which is simply a number without dollar sign but should have a negative sign if it is a kind of expense. If it's an income, it should be positive.
    the type of spending, which you should summarize which category it belongs to, and 
    the details of the spending, if I've given it to you, leave it empty if no. And reply me with the formatted string:
    date | amount | type | detail 
    The format of date is YYYY-MM-DD. Unless it's told, the date would be {today}
    Just tell me the results, don't explain.
    {sentence}"""
    # fixed GPT to real date.

    try:
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": info.format(
                    sentence=sentence, today=today)},
            ]
        )
        rsp = rsp.get("choices")[0]["message"]["content"]
        rsp = [i.strip() for i in rsp.split("|")]
        return rsp
    except:
        raise Exception("Sorry, I didn't understand you. Please try again.")
# ----------------- SEPARATOR ----------------- #


def get_all():
    data = []
    ids = [j[0] for j in Z.read_from_db("id")]
    dates = [j[0] for j in Z.read_from_db("date")]
    types = [j[0] for j in Z.read_from_db("type")]
    amounts = [j[0] for j in Z.read_from_db("amount")]
    details = [j[0] for j in Z.read_from_db("detail")]

    for id, date, type, amount, detail in zip(ids, dates, types, amounts, details):
        item = {
            "id": "",
            "date": "",
            "type": "",
            "amount": "",
            "detail": ""
        }
        item["id"] = id
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
    try:
        data = text_formatting(data["sentence"])
        assert len(data) == 4
    except:
        return jsonify(get_all())
    Z.write_to_db(date=data[0], type=data[2],
                  amount=data[1], detail=data[3])
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

@app.route('/api/v1.0/transactions/clear', methods=['GET'])
def clear():
    Z.clear_all()
    return jsonify(get_all())


app.run(host="0.0.0.0", debug=True, port=5000)
