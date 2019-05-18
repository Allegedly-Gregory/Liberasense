#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session, flash
import json
import os
import glob
from renderer import getfiles, concat

contents = []
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_dir_name = "./json"
json_pattern = os.path.join(json_dir_name, "*.json")
jsonpath = glob.glob(json_pattern)
for file in jsonpath:
    contents.append(file)
# jsonpath = os.path.join(BASE_DIR, "sentiment_frankenstein.json")

# Read JSON data into the datastore variable
if jsonpath:
    with open(jsonpath[0], "r") as f:
        datastore = json.load(f)

if jsonpath:
    with open(jsonpath[1], "r") as r:
        datastore1 = json.load(r)

app = Flask(__name__)

BOOKS = {
    'frankenstein': 'Frankenstein',
    'huckleberry': 'Huckleberry Finn',
    'twocities': 'A Tale of Two Cities'
}

def nchaps(book):
    GLOB = glob.glob('books/frankenstein/Chap*par_1.txt.html')
    return len(GLOB)

def nextchap(book, chap):
    nchap = chap + 1
    print(nchaps(book))
    if chap >= nchaps(book):
        return None
    return "/chap/{}/{}".format(book, nchap)

def prevchap(book, chap):
    nchap = chap - 1
    if chap <= 1:
        return None
    return "/chap/{}/{}".format(book, nchap)

def booklink(book):
    return "/book/{}".format(book)

def chaplink(book, chap):
    return "/chap/{}/{}".format(book, chap)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chap/<book>/<int:chapnum>')
def chap(book, chapnum):
    html = concat(getfiles(book, chapnum))
    clinks = chaplinks(book, 'list-group-item')
    return render_template('chap.html', chaplinks=clinks, chapnum=chapnum, html=html, nlink=nextchap(book, chapnum), plink=prevchap(book, chapnum), booklink=booklink(book), booktitle=BOOKS[book])

def chaplinks(book, cssclass=''):
    return ["<a href='{}' class='{}'>Chapter {}</a>".format(chaplink(book, n), cssclass, n) 
        for n in range(1, nchaps(book)+1)]

@app.route('/book/<book>')
def titlepage(book):
    clinks = chaplinks(book)
    return render_template('book.html', title=BOOKS[book], chaplinks=clinks)

@app.route("/", methods=["GET"])
def index():
    return render_template("base.html")

"""
@app.route("/frankenstein", methods=["GET"])
def book1():
    return render_template(
        "sentireader.html", datastore=datastore1, title="Frankenstein",
    )


@app.route("/huckleberryfinn", methods=["GET"])
def book2():
    return render_template(
        "sentireader.html",
        datastore=datastore,
        title="The Adventures of Huckleberry Finn",
    )
"""

if __name__ == "__main__":
    app.debug = True
    app.run(port=8080)
