from flask import Flask, render_template, url_for
from functools import wraps

import random

app = Flask(__name__)

#DEBUG mode
app.config["DEBUG"] = True


# helper functions


def quote_generator():
        quote_dict =[["a1", "q1"],
         ["a2", "q2"],
         ["a3", "q3"]
        ]
        qotd_pair = random.choice(quote_dict)
        return qotd_pair


# route decorators
@app.route('/')
def homepage():
        qotd_display = quote_generator()
        return render_template("main.html", qotd_display = qotd_display)

@app.route('/about_me/')
def about_me():
        return render_template("about_me.html")

if __name__ == "__main__":
	app.run()

