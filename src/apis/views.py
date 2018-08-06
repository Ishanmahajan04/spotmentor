import logging
from flask import Flask, flash, redirect, render_template, request, session, abort
import os


logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"

def index1():
    logger.info("Checking the flask scaffolding logger")
    return "demo link"

def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"
 
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
