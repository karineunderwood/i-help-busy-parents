from flask import (Flask, render_template, request, flash, session, 
                   redirect)

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/services')
def services():
    """View list of offered services."""

    return render_template('services.html')

@app.route('/how_it_works')
def how_it_works():
    """Show clients how to use service."""

    return render_template('how-it-works.html')

@app.route('/pricing')
def packages_price():
    """show price options."""

    return render_template('pricing.html')


@app.route('/about')
def about_me():
    """Show about me page."""

    return render_template('about.html')





















if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')