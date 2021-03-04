from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template,request,redirect, url_for,request,flash,session,g
from acab import eat_the_rich
from flask_wtf import FlaskForm 
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user



# Create an instance of Flask
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def blackLivesMatter():
    print(request.method)
    if request.method == "POST":
        #Passing user inputs from HTML to python variable
        first = request.form['first_name']
        last = request.form['last_name']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        state_abbreviation = request.form['state_abbreviation']
        country = request.form['country']
        zipcode = request.form['zipcode']
        email = request.form['email']
        phone = request.form['phone']
        prefix = request.form['prefix']

        #Function to call data from acab and return data
        results = eat_the_rich(first, last, street, city, state, state_abbreviation, country, zipcode, email, phone, prefix)        
        
        return redirect(url_for("thanks"))
        
    return render_template('index.html', data=results)

@app.route('/thanks')
def thanks():
    print("Thanks for making history with us!")

    return render_template

if __name__ == "__main__":
    app.run(debug=True)