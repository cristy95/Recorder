# -*- coding: utf-8 -*-
"DOCSTRING"
from flask import Flask, render_template, request
from teamlist import TeamList

APP = Flask(__name__)
TEAMLIST = TeamList()

@APP.route('/')
def hello_world():
    """Gets the score of a Team"""
    name = request.args.get('name')
    score = request.args.get('score')
    TEAMLIST.add_score(name, score)

    score1 = TEAMLIST.get_score("Guinea")
    score2 = TEAMLIST.get_score("Pig")

    return render_template('index.html', score1 = score1, score2 = score2)

if __name__ == '__main__':
    APP.run(debug=True)
