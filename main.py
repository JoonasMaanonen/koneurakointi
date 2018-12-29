from flask import Flask, render_template
app = Flask(__name__)
# Disable caching while developing
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def etusivu():
    return render_template('etusivu.html', page='etusivu')

@app.route('/palvelut')
def palvelut():
    return render_template('palvelut.html', page='palvelut')

@app.route('/yritys')
def tietoa_meista():
    return render_template('yritys.html', page='yritys')

@app.route('/yhteystiedot')
def yhteystiedot():
    return render_template('yhteystiedot.html', page='yhteystiedot')
