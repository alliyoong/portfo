from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/#thankyou')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again.'




