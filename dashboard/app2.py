from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)



@app.route("/")
def home():
    df = pd.read_csv('cereal.csv')


    # Menentukan Size
    fig = plt.figure(figsize=(8,3),dpi=300)
    fig.add_subplot()
    sns.catplot("mfr", data = df, kind = "count")

    plt.savefig('mfr.png',bbox_inches="tight") 


    # Mengubah Plot ke dalam base64 agar dapat ditampilkan di HTML
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())

    # memasukkan kedalam variabel
    result = str(figdata_png)[2:-1]

    ##################################### Beda Plot
    fig.add_subplot()
    sns.catplot("mfr", "rating", data = df)


    plt.savefig('rating.png',bbox_inches="tight") 


    # Mengubah Plot ke dalam base64 agar dapat ditampilkan di HTML
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())

    # memasukkan kedalam variabel
    result2 = str(figdata_png)[2:-1]



    return render_template('plot.html', plot=result, plot2= result2 )













if __name__ == "__main__": 
    app.run(debug=True)
