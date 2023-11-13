from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title='Sabari\'s PortFolio')

@app.route('/Contact', methods=['GET'])
def contact():
    return render_template('contact.html',title='Sabari\'s PortFolio')

@app.route('/About')
def about():
    return render_template('about.html',title='Sabari\'s PortFolio')

@app.route('/Projects')
def project():
    return render_template('projects.html',title='Sabari\'s PortFolio')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')