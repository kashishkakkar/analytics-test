from flask import Flask, request, jsonify, render_template, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



