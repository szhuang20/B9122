# -*- coding: utf-8 -*-
import gmplot
from flask import Flask, session, render_template, url_for,request
import matplotlib.pyplot
from flask_wtf import FlaskForm
from datetime import date
from wtforms.fields.html5 import DateField
from flaskext.mysql import MySQL
from wtforms import SelectField




app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root' 
app.config['MYSQL_DATABASE_PASSWORD'] = 'lw2704' 
app.config['MYSQL_DATABASE_DB'] = 'citibike' 
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
mysql.init_app(app)
conn = mysql.connect() 
cursor = conn.cursor()

app.secret_key = '1234567890'

class DestinationsForm(FlaskForm):
    attributes = SelectField('Data Attributes', choices=[('Weekdays', 'Weekdays'), ('Weekends','Weekends'), ('Combined','Combined')])
"""
class AnalyticsForm(FlaskForm):
	attributes = SelectField('Data Attributes', choices=[('Agency', 'Agency'), ('Borough','Borough'), ('Complaint_Type', 'Complaint Type')])


class MapParamsForm(FlaskForm):
	dtfrom = DateField('DatePicker', format='%Y-%m-%d', default=date(2016,1,1)) 
	dtto = DateField('DatePicker', format='%Y-%m-%d', default=date(2016,1,2))
"""
def get_homepage_links():
	return [
			{"href": url_for('trips'), "label":"Trips Distribution in 2015"}, 
			{"href": url_for('gender'), "label":"Gender Distribution"},
			{"href": url_for('station'), "label":"Stations Growth"},
			{"href": url_for('destinations'), "label":"Most Popular Destinations"},
			{"href": url_for('age'), "label":"Age Distribution"},
			{"href": url_for('carto'), "label":"Close Look - Citibike Usage On 1/11/2016"},
			{"href": url_for('heatmap'), "label":"Heatmap"},
			]

@app.route("/")
def home():
    session["data_loaded"] = True
    return render_template('home.html',links=get_homepage_links())

@app.route("/station")#,methods=['GET','POST'])
def station():
	session["data_loaded"] = True
	return render_template('station.html')

@app.route("/trips")#,methods=['GET','POST'])
def trips():
	session["data_loaded"] = True
	return render_template('trips.html')

"""
@app.route("/destinations", methods=['GET','POST'])
def destinations():
	session["data_loaded"] = True
	return render_template('destinations.html',weekdayfile = 'weekday.html')
"""
@app.route("/destinations/", methods=['GET','POST'])#,methods=['GET','POST'])
def destinations():
    form = DestinationsForm()
    if form.validate_on_submit():
        #session["data_loaded"] = True
        if request.form['attributes'] == 'Weekdays':
            return render_template('weekdaybothpic.html')
        elif request.form['attributes'] == 'Weekends':
            return render_template('weekend_1bothpic.html')
        elif request.form['attributes'] == 'Combined':
            return render_template('weekday_weekend.html')
    return render_template('destinations.html', form=form)




@app.route("/growth")#,methods=['GET','POST'])
def growth():
	session["data_loaded"] = True
	return render_template('home.html')

@app.route("/carto")#,methods=['GET','POST'])
def carto():
	session["data_loaded"] = True
	return render_template('carto.html')

@app.route("/gender")#,methods=['GET','POST'])
def gender():
	session["data_loaded"] = True
	return render_template('gender.html')

@app.route("/heatmap")#,methods=['GET','POST'])
def heatmap():
	session["data_loaded"] = True
	return render_template('heatmap.html')

@app.route("/age")#,methods=['GET','POST'])
def age():
	session["data_loaded"] = True
	return render_template('age.html')

@app.route("/getstarted")#,methods=['GET','POST'])
def getstarted():
	session["data_loaded"] = True
	return render_template('getstarted.html')

@app.route("/references")#,methods=['GET','POST'])
def references():
	session["data_loaded"] = True
	return render_template('references.html')


if __name__ == "__main__":
    app.run(debug=True)



