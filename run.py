
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request
from flask import jsonify
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdadzxl"
app.config['UPLOAD_FOLDER'] = 'upload/'

filename = ""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mystring')
def mystring():
    return 'my string'


@app.route('/dataFromAjax')
def dataFromAjax():
    test = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'


@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    print('post')
    if request.method == 'POST':
        a = request.form['mydata']
        print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/name', methods=['POST'])
def getname():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    d = {'name': firstname + ' ' + lastname, 'age': 18}
    print(d)
    return jsonify(d)


@app.route('/myform', methods=['POST'])
def myform():
    print('post')
    a = request.form['FirstName']
    print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    print('mylist')
    return json.dumps(l)  


@app.route('/mytable')
def mytable():
    table = [['id', 'GC次数', '泄漏地址', '分配点信息','分配对象个数'],
        ['1', '1', '0x21213', '100','12'],
        ['2', '1', '0x433232', '100','22'],
        ['3', '2', '0x322323', filename,'444']]

    print('mytable')
    data = json.dumps(table)
    print(data)
    return data

@app.route('/myechart')
def myechart():
    print('post')
    if request.method == 'POST':
        a = request.form['mydata']
        print(a)
    d = {'value': [1,2,3,4], 'name': ["aasasdasadadadadadad","bzzzzzzzzz","fgfdfdfdfdfdfdfdfc","d阿飒飒飒飒飒"]}
    data = json.dumps(d)
    return data


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.data
      print(type(f))
      print(f)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      return 'file uploaded successfully'

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file :
            # filename = secure_filename(file.filename)
            globals()['filename'] = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return  '{"filename":"%s"}' % file.filename
    return ''

if __name__ == '__main__':
    app.run(debug = True,host = '127.0.0.1')
