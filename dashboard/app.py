import joblib
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/iris')
def iris():
    return render_template('iris.html')

@app.route('/data-visualization')
def datavis():
    return render_template('data-visualization.html')

@app.route('/data-analysis')
def dataanalysis():
    return render_template('data-analysis.html')

@app.route('/classification')
def classification():
    return render_template('classification.html')



@app.route('/classification/result', methods = ['POST', 'GET'])
def hasil():
    if request.method =='POST':
        masukan = request.form
        
        nilai = masukan['optradio']

    return render_template('result.html', data=masukan)

if __name__ == "__main__":
    Model = joblib.load('model_exam')
app.run(debug=True)