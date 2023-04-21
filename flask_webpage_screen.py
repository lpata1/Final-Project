from flask import Flask, render_template, request
# from python_stock_functions import
# Add to the imports when the functions are done

###
"""
Make sure to Hide all API keys
"""
###

app = Flask(__name__)

@app.route('/') #Re format the Screen so it looks presentable
def index():
    return render_template('index.html')

@app.route('/button1')
def button1():
    return render_template('button1.html')

@app.route('/button2')
def button2():
    return render_template('button2.html')

@app.route('/button3')
def button3():
    return render_template('button3.html')

@app.route('/button4')
def button4():
    return render_template('button4.html')

@app.route('/button5')
def button5():
    return render_template('button5.html')

@app.route('/button6')
def button6():
    return render_template('button6.html')

if __name__=='__main__':
    app.run(debug=True)

""""""
#Have THe Button Pathways ready
""""""