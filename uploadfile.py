#coding='utf-8'

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/uploadfile', methods=['POST'])
def uploadfile():
    if request.method == 'POST':
        f = request.files['file']
        #f.save("./static/"+f.filename)
        f.save("./static/" + "test.jpg")
        return 'file uploaded successfully'

@app.route('/get', methods=['GET'])
def get():
    if request.method == 'GET':
        pw=request.args.get('pw')
        if pw=='xyyy':
           return render_template('index.html')
        else:
            return 'please provide right value'

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
