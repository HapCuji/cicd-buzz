import os
import signal

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/buzz')

from flask import Flask
#from buzz import generator
import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
	page = '<html><body><h1>'
	page += generator.generate_buzz()
	page += '</h1></body></html>'
	return page
	
if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = os.getenv('PORT')) #port 5000 is default