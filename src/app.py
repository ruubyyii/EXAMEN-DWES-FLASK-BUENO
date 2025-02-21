from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from config import config
from models.entities.User import User
from forms import LoginForm, RegisterForm, ContactForm
from models.ModelUser import ModelUser

app = Flask(__name__)
db = MySQL(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def get_by_id(id):
    return ModelUser.get_by_id(db, id)

# LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User(0, email, password, '')
        logged_user =  ModelUser.login(db, user)

        if logged_user:

            print('Usuario encontrado!')
            if logged_user.password:
                print('Contraseña correcta')
                login_user(logged_user)
                return redirect(url_for('contacts'))
            else:
                print('Contraseña incorrecta.')
                return render_template('login.html', form=form)
        else:
            print('Usuario no encontrado')
            return render_template('login.html', form=form)
    else:
        # if current_user.is_authenticated:
        return render_template('login.html', form=form)
        # return redirect(url_for('contacts'))

# REGISTER todo lo comentado es para que una vez registrado me mande a contacts
@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        fullname = request.form.get('fullname')

        user = User(0, email, password, fullname)
        ModelUser.register(db, user)
        return render_template('register.html', form=form)
        # logged_user =  ModelUser.login(db, user)

        # if logged_user:
        #     if logged_user.password:
        #         login_user(logged_user)
        #         return redirect(url_for('contacts'))
        #     else:
        #         print('Contraseña incorrecta.')
        #         return render_template('login.html', form=form)
        # else:
        #     print('Usuario no encontrado')
        #     return render_template('login.html', form=form)
    else:
        # if current_user.is_authenticated:
        return render_template('register.html', form=form)

# CONTACTOS
@app.route('/contacts')
# @login_required
def contacts():

    form = ContactForm()
    
    return render_template('contacts.html', form=form)

# ADD CONTACTS
@app.route('/addContacts', methods=['POST'])
def addContacts():
    pass

@app.route('/editContact/<string:id>')
def editContact(id):
    pass

@app.route('/updateContact/<string:id>', methods=['POST'])
def updateContact():
    pass
@app.route('/deleteContact/<string:id>', methods=['POST'])
def deleteContact():
    pass

# LOGOUT
@app.route('/logout')
def logout():
    logout_user()
    print('Sesion cerrada.')
    return redirect(url_for('login'))

def error_404(error):

    return '<h1>ERROR 404❌/h1>'

def error_401(error):

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, error_404)
    app.register_error_handler(401, error_401)
    app.run()