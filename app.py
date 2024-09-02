from flask import Flask, request, render_template_string, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form['content']
        new_message = Message(content=content)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('home'))

    messages = Message.query.all()
    return render_template_string('''
        <!doctype html>
        <title>Flask Uygulaması</title>
        <h1>Selam ! Burası Test Ortamıdır.</h1>
        <form method="POST">
            <label for="content">Mesaj:</label>
            <input type="text" id="content" name="content">
            <input type="submit" value="Gönder">
        </form>
        <ul>
            {% for message in messages %}
                <li>{{ message.content }}</li>
            {% endfor %}
        </ul>
    ''', messages=messages)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
