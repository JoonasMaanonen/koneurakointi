from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def etusivu():
    return render_template('etusivu.html', page='etusivu')

@app.route('/palvelut')
def palvelut():
    return render_template('palvelut.html', page='palvelut')

@app.route('/referenssit')
def tietoa_meista():
    return render_template('referenssit.html', page='referenssit')

@app.route('/yhteystiedot')
def yhteystiedot():
    return render_template('yhteystiedot.html', page='yhteystiedot')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
