from flask import Flask, render_template, url_for
from functools import wraps

import random, os

app = Flask(__name__)

#DEBUG mode
app.config["DEBUG"] = True


# helper functions


def quote_generator():
        quote_dict =[["Some people care too much. I think it's called love.", "A.A. Milne, Winnie-the-Pooh"],
         ["You can't stay in your corner of the Forest waiting for others to come to you. You have to go to them sometimes.", "A.A. Milne, Winnie-the-Pooh"],
        ["I think we dream so we don’t have to be apart for so long. If we’re in each other’s dreams, we can be together all the time.", "A.A. Milne, Winnie-the-Pooh"],
          





        ]
        qotd_pair = random.choice(quote_dict)
        return qotd_pair

def iotd_generator():
        picOfTheDay = str(random.randint(1,3))+ ".jpg"
        iotd = os.path.join(r"images/iotd/", picOfTheDay)
        return iotd

# route decorators
@app.route('/')
def homepage():
        qotd_display = quote_generator()
        iotd = iotd_generator()
        return render_template("main.html", qotd_display = qotd_display,\
                               iotd = iotd)

@app.route('/about_me/')
def about_me():
        return render_template("about_me.html")

@app.route('/projects/')
def projects():
        return render_template("projects.html")

@app.route('/projects/SG_prop/')
def sg_prop():
        return render_template("sg_prop.html")




"""@app.route('/blog/')
def blog():
        return render_template("blog.html")
"""

if __name__ == "__main__":
	app.run()

