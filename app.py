from flask import Flask , render_template , request , jsonify
import os
from model_py_files.main import final_answer
app = Flask(__name__)


@app.route('/')

def hello():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def recuperer():  
    s=request.args.get('langage')
    s=final_answer(s)
    return jsonify(s)

if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True,port=5001)  