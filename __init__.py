# __init__ file to run the server

from json import load  # to load secret.json

from flask import Flask, render_template, request, flash  # flask app
from flask_mail import Mail, Message  # flask mail

from forms import ContactForm  # import form data

# Flask class
app = Flask(__name__)

# load secret data
with open('secret.json') as data_file:
    secret = load(data_file)

app.secret_key = str(secret['SECRET_KEY'])

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=str(secret['USERNAME']),
    MAIL_PASSWORD=str(secret['PASSWORD']),
)

# Flask mail class
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    """Home page with form data"""

    form = ContactForm()
    if request.method == 'POST':

        if not form.validate():
            flash('All fields are required.')
            return render_template('index.html', form=form)

        else:
            msg = Message(form.subject.data,
                          sender=form.email.data,
                          recipients=[str(secret['USERNAME'])]
                          )

            msg.body = """
            Someone needs your talent!
            From: %s, %s
            %s
            """ % (form.name.data, form.email.data, form.message.data)

            mail.send(msg)

            return render_template('index.html', success=True)

    elif request.method == 'GET':
        return render_template('index.html', form=form)


@app.route('/portfolio')
def portfolio():
    """Portfolio page"""
    return render_template('multiverse.html')


# Errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
