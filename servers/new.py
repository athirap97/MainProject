import sys
sys.path.append('/home/athira/Desktop/test16/DNN_chatbot/')
from engine import response
from flask import request
import chatbot_config as cfg

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html',result={})

@app.route('/process', methods=['POST'])
def process():
	if(request.method=='POST'):
		inp=request.form
		print(inp['user_input'])
		a=str(response(str(inp['user_input'])))
		print("SCT_bot: "+a)
		data={
			'user_input':inp['user_input'],
			'r':a
		}
		return render_template('home.html',result=data)
		
if __name__ == '__main__':
        app.run(debug=True)
