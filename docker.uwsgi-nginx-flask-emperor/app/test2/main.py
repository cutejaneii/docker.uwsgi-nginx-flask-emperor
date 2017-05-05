# encoding=UTF-8
#!flask/bin/python

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index2():
	return "Hello, this is test 2 ~"
      
if __name__ ==  '__main__':
	app.run(debug=True)      
        
