
from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGeuss'

@app.route('/setuser/<user>')
def setuser(user:str)->str:
	session['user'] = user
	return 'User value from setuser is: ' + session['user']
	
@app.route('/getuser')
def getuser()->str:
	return 'User value from getuser is: ' + session['user']
	
if __name__=='__main__':
	app.run(debug=True)
	
	