from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
from bson.json_util import dumps
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.6lhevqc.mongodb.net/Cluster0?retryWrites=true&w=majority' )
db = client.theater

# 화면 보여주는 부분
@app.route('/')
def home():
    return render_template('fullstack2.html')
#기능 부분
@app.route('/art', methods=['GET'])
def art_get():
    art_list = list(db.theater_list.find({}, {'_id': False}))

    return jsonify({'arts':art_list})
#검색 부분
@app.route('/search', methods=['GET'])
def search_input():
    search_receive = request.args.get('search_give')

    question_result = list(db.theater_list.find({'TITLE': {'$regex': search_receive}}))
    print(question_result)
    return jsonify({'result': 'success', 'question_result': dumps(question_result)})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)