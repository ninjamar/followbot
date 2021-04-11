from flask import Flask
#import os
#os.system('pip install scratchapi') #auto install stuff
from code import main

app = Flask('app')
#513564818
@app.errorhandler(500)
def server_error(e):
  return 'Scratch could not log me in. Please try later'
@app.route('/')
def index():
  return main()

app.run(host='0.0.0.0', port=8080)
