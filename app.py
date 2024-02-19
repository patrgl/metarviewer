from flask import Flask, request, render_template
from PythonMETAR import *

app = Flask(__name__)

def metar_Search(airport_code):
    try:
        metar_result = Metar(airport_code.upper())
    except:
        if len(airport_code) != 4:
            metar_result = 'Type a four-letter ICAO code'
        else:
            metar_result = 'No METAR Found'
    return metar_result

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        icao_code = request.form.get('icao_code')
        metar = str(metar_Search(icao_code))
        return render_template('home.html', value=metar)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
