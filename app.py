
from flask import Flask,render_template,request
import pandas as pd

app=Flask(__name__)

@app.route('/')
def call():
    return render_template('dhaba.html')

@app.route('/details',methods=['GET','POST'])
def extract():
    if(request.method=='POST'):
        Price1=request.form['food1']
        Q1=request.form['qnty1']
        Price2=request.form['food2']
        Q2=request.form['qnty2']
        
        print("Price1 : ",Price1)
        print("Qnty1 : ",Q1)
        print("Price2 : ",Price2)
        print("Qnty2 : ",Q2)
        total=int(Price1)*int(Q1) + int(Price2)*int(Q2)
        print("Total Amount : ",total)
        return render_template('dhaba.html',Total=total)
app.run()



