from flask import Flask, render_template

app = Flask(__name__)

#DEBUG mode
app.config["DEBUG"] = True

@app.route('/')
def homepage():
	return render_template("main.html")
	
if __name__ == "__main__":
	app.run()
