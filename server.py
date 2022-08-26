from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = "cookies"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if len(request.form['person_name']) == 0: #validating to make sure they have put info in name section, if not will route back to main page
        return redirect('/')
    print(request.form) #this is grabbing the info(dictionary) that was entered
    session['name'] = request.form['person_name']
    session['dojo_location'] = request.form['location']
    session['fav_language'] = request.form['language']
    session['user_comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')







if __name__ == "__main__":
    app.run(debug=True)