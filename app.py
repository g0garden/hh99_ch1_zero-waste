from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from pymongo import MongoClient
import jwt
import datetime
from datetime import datetime, timedelta
import hashlib

app = Flask(__name__)
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://strong1133:tjrwls455@15.164.102.138', 27017)
db = client.dbhh99

SECRET_KEY = 'STRONG'


######### HTML RENDER ############
##################################

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload['id']})
        articles = list(db.db_zerowaste.find({}))
        for article in articles:
            article["_id"] = str(article["_id"])
            # print(payload['id'])

            tf = article["marking_by_me"] = bool(
                db.likes.find_one({"article_id": article["_id"], "type": "marking", "id": payload['id']}))
            if tf == True:
                marking_by_me = "fas"
            else:
                marking_by_me = "far"
            marking_by_me = marking_by_me

        likes = list(db.likes.find({"id": payload['id']}))
        # print(likes)

        return render_template('index.html', articles=articles, marking_by_me=marking_by_me, likes=likes,
                               user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간을 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/mypage/<id>')
def mypage(id):
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload['id']})
        # users = list(db.users.find({}))
        return render_template('mypage.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간을 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


############# 로그인 ###############
##################################

@app.route('/sign_in', methods=['POST'])
def sign_in():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=300)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/register/save', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    intro_receive = request.form['intro_give']

    # print(id_receive, name_receive)
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    db.users.insert_one({'id': id_receive, 'pw': pw_hash, 'name': name_receive, 'intro': intro_receive})

    return jsonify({'result': 'success'})


@app.route('/register/overlap_check', methods=['POST'])
def overlap_check():
    id_receive = request.form['id_give']
    # print(id_receive)
    exists = bool(db.users.find_one({'id': id_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route("/get_articles", methods=['GET'])
def get_articles():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        articles = list(db.db_zerowaste.find({}))
        for article in articles:
            article["_id"] = str(article["_id"])
            article["marking_by_me"] = bool(
                db.likes.find_one({"article_id": article["_id"], "type": "marking", "id": payload['id']}))
        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다.", "articles": article})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for(home))


@app.route('/update_marking', methods=['POST'])
def update_like():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload['id']})
        article_id_receive = request.form["article_id_give"]
        type_receive = request.form["type_give"]
        action_receive = request.form["action_give"]
        doc = {
            "article_id": article_id_receive,
            "id": user_info["id"],
            "type": type_receive,
            "memo": ''
        }
        if action_receive == "marking":
            db.likes.insert_one(doc)
        else:
            db.likes.delete_one({'article_id': article_id_receive})
        return jsonify({"result": "success", "msg": "update"})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for(home))


@app.route('/memo_edit', methods=['POST'])
def memo_edit():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"id": payload['id']})

        memo_receive = request.form['memo_give']
        id_receive = request.form['id_give']

        db.likes.update_one({"article_id": id_receive, "id": payload['id']}, {'$set': {'memo': memo_receive}})
        # print(id_receive)
        return jsonify({"result": "success"})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for(home))


@app.route('/update_profile', methods=['POST'])
def mypage_edit():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        id = payload['id']
        print(id)
        name_receive = request.form['name_give']
        intro_receive = request.form['intro_give']
        doc = {
            'name': name_receive,
            'intro': intro_receive
        }
        print(doc)
        db.users.update_one({'id': payload['id']}, {'$set': doc})
        return jsonify({"result": "success"})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for(home))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
