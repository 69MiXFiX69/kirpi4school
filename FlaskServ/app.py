from flask import Flask, render_template,  request

from kirpi4server import check_input, convert_input_to_array, four_digits

app = Flask(__name__)
random_num = None

@app.route('/', methods=['POST', 'GET'])
def check():
    global random_num
    if request.method == 'POST':
        num = request.form['num']
        if random_num is None:
            random_num = four_digits()
            print(random_num)
        final_num = check_input(convert_input_to_array(num), random_num)
        print(num)
        if (int(num) < 1000 or int(num) > 9999):
            return render_template('error_notification.html')
        elif(final_num == num):
            return render_template('congrats.html')
        else:
            return render_template('NumberChecking.html', num=final_num)
    return render_template('index.html')

app.run(debug=True)

# app.add_url_rule('/congrats/',
#                  view_func=****.as_view('remote'),

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     return render_template("index.html")