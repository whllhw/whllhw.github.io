# coding=utf-8
from flask import Flask,g,session,redirect,jsonify
from flask import render_template,abort
from flask import request,Response,url_for
import json,MySQLdb,time,hashlib

app = Flask(__name__)

def init_db():
    conn = MySQLdb.connect('118.89.41.105','lhw','123456','app',3306,'/tmp/mysql.sock',charset='utf8')
    conn.autocommit(1)
    return conn.cursor()

@app.before_request
def before_request():
    try:
        g.db = init_db()
    except :
        abort(503, "No database connection could be established.")

@app.teardown_request
def teardown_request(exception):
    try:
        g.db.close()
    except AttributeError:
        pass

@app.route('/<shorturl>')
def get(shorturl=None):
    # 不一定是网址缩短，还可以是加密文字
    if shorturl:
        if g.db.execute('select * from t_shorturl where inurl="{}"'.format(shorturl)):
            result = g.db.fetchall()[0]
            times = result[4]+1
            g.db.execute('UPDATE t_shorturl SET times={} WHERE inurl="{}"'.format(times,shorturl))
            if 'http://' in result[2][:7] or 'https://' in result[2][:8]:
                return redirect(result[2])
            else:
                return render_template('hello.html',text=result[2])
        else:
            return render_template('hello.html',error=503)# 查询出错
    return render_template('hello.html',error=404)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def generate():
    if request.json:
        url = request.json['url'].encode('utf-8')
        inurl = []
        for url in url.split('\n'):
            inurl.append(hashlib.md5(url).hexdigest()[:4].decode('utf-8'))
            g.db.execute('insert into t_shorturl(date , url, inurl, times) values ("{}","{}","{}","{}")'.\
            format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),url,inurl[-1],0))
    else:
        return jsonify({'status':-1,'err_msg':'提供的数据有误，请重试'}) # 无参数报错
    #return Response(json.dumps({'url':inurl,'status':0}),mimetype='application/json')
    return jsonify({'list':''.join([request.url_root+ i + '\n' for i in inurl]),'msg':'生成链接成功'})
if __name__ == '__main__':
    app.run()
