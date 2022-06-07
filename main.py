import flask
from flask import render_template, request, jsonify, make_response, url_for
from mongo_methods import check_device, get_device, check_signup, update_password


app = flask.Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/setlogin', methods=['POST'])
def connect():
    data1 = request.get_json()
    ip = data1['ip']
    password = data1['password']


    correct = check_device(ip, password)
  
    return correct

@app.route('/dashboard')
def dashboard():
  if 'ip' in request.cookies and 'password' in request.cookies:
    ip = request.cookies.get('ip')
    password = request.cookies.get('password')
    data = get_device(ip, password)
    print(data)
    return render_template('dashboard.html', data=data)
  else:
    return render_template('login.html')
    


@app.route('/signupcheck', methods=['POST'])
def signup1():
  data = request.get_json() 
  ip = data['ip']
  password = data['password']

  correct = check_signup(ip)
  if correct == 'true':
    update_password(ip, password)
  return correct

@app.route('/signup')
def signup():
  return render_template('signup.html')
  

@app.route('/login')
def login_page():
  return render_template("login.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)