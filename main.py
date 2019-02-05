from flask import Flask, render_template,request
import telegram

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
	if request.method=='POST':
		Q = request.form['Q']
		telegram.send_telegram(Q)
	return render_template('index.html')

		

	
if __name__ == '__main__':
    app.run()