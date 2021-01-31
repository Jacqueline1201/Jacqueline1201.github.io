

#Flask App
from flask import Flask, request, render_template, url_for
#JSON Parsing
import json
#MondoDB
import pymongo
#Mongo Object 
from bson import json_util
import sys

#Create FLask App object
app = Flask(__name__,static_url_path='', static_folder='static')

#Each method is tied to a url, written using '@app.rout()'

@app.route('/', methods=["GET"])
def root():
    #Default HTML page
  
    return render_template('home.html')


#GET method (doesn't receive info, sends back info)
@app.route('/home', methods = ["GET"])
def viewItems():
    client = pymongo.MongoClient("mongodb+srv://hackuci:hackuci2021@cluster0.ddy87.mongodb.net/UCIConfessions?retryWrites=true&w=majority")
    db = client["UCIConfessions"]
    col = db["List of Confessions"]
    log = list(col.find({}))
    log.reverse()
    return render_template("home.html", confessions = log)

@app.route('/home2', methods = ["GET"])
def viewItemsReverse():
    client = pymongo.MongoClient("mongodb+srv://hackuci:hackuci2021@cluster0.ddy87.mongodb.net/UCIConfessions?retryWrites=true&w=majority")
    db = client["UCIConfessions"]
    col = db["List of Confessions"]
    log = list(col.find({}))
   
    return render_template("home.html", confessions = log)





#POST method(receives information, sends back information)
@app.route('/add', methods = ["GET","POST"])
def addItems():
    
    client = pymongo.MongoClient("mongodb+srv://hackuci:hackuci2021@cluster0.ddy87.mongodb.net/UCIConfessions?retryWrites=true&w=majority")
    db = client["UCIConfessions"]
    col = db["List of Confessions"]
    entry = {
        "title" : request.form['title'],
        "confession" :  request.form['confession']
    }

    col.insert_one(entry)
    log = list(col.find({}))
    log.reverse()
    
    return render_template("home.html", confessions = log)


# Runs Flask App
if __name__ == "__main__":
    app.run()    
    #log = list(col.find())
    #return json_util.dumps(log)

