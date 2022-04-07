#!/usr/bin/env python3

from flask import Flask, render_template, request
import hashlib as hl

app = Flask(__name__)

database = r"./db/test.sqlite"

@app.route("/", methods=['post', 'get'])
def root():
    if request.method == 'POST':
        expr = request.form.get('text')
        err = False
        try: 
            txt = expr + ' = ' + str(eval(expr))
        except BaseException as exc:
            err = True
            txt = str(exc)
        page = render_template('index.html', text=txt, error=err, expr=expr)
    else:
        page = render_template('index.html')
    return page
