from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
        if request.method == 'POST':
            try:
                data = request.form.to_dict()
                write_to_csv(data)
                return redirect('/thankyou.html')
            except: return 'did not save to database'
        else:
            return 'something went wrong'

def write_to_file(data):
    with open('database.txt', mode='a') as my_database:
        text = my_database.write(f"{data.get('email')},{data.get('subject')},{data.get('message')}\n")

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as my_database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(my_database2, delimiter=',', quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])