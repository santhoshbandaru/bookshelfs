import os
import flask
import pandas as pd
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        temp=""
        ai = [x for x in request.form.values()]
        a=ai[0]
        print(a)
        df=pd.read_csv("file1.csv",index_col="index")
        s=a[0].upper()
        i=ord(s)-ord("A")
        col=list(df.columns)
        c=0
        for k in range(0,len(col)):
            j=col[k]
            try:
                st=int(df.loc[s,j])
            except:
                continue
            if(st==0):
                df.loc[s, j] = a
                temp="shelf="+j[0]+"row="+j[1]+"book"+j[-1]
                c=1
                break
        if(c==0):
            temp="no space"
        df.to_csv('file1.csv')
        return render_template("index.html", result='{}'.format(temp))
if __name__=="__main__":
    app.run()
