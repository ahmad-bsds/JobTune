from flask import Flask, render_template
# from user import sign_up_user
from flask_login import LoginManager
from user_and_auth import User, RegistrationForm, LoginForm

jobease_app = Flask(__name__)
jobease_app.config['SECRET_KEY'] = '$JobEase$'

# login_manager = LoginManager()

# login_manager.init_app(jobease_app)

# Home
@jobease_app.route('/')
def index():
    """
    Home page to gets you tarter.
    """
    return render_template("user_page.html")

# Login and Signup
@jobease_app.route('/start', methods=['GET', 'POST'])
def start():
    """
    Login and Signup page
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template("user_page.html")
    return render_template("login_signup.html")

# Get Data
@jobease_app.route('/get_data')
def get_data():
    """
    Get Job description page.
    """
    return render_template("get_data.html")

@jobease_app.errorhandler(404)
def page_not_found(e):
    return "404"

if __name__ == '__main__':
    jobease_app.run(debug=True)