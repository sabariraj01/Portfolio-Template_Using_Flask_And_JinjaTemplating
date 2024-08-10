from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Sabari's Portfolio")

@app.route('/about')
def about():
    return render_template('about.html', title="About Sabari")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Sabari")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Sabari's Projects")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
