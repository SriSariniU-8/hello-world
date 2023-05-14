from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db= SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Todo(db.Model):
    sno= db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.no} - {self.title}"


@app.route("/")
def hello_world():
    todo= Todo(title= 'First Todo', desc= 'start investing in stock market')
    db.session.add(todo)
    db.session.commit()
    text = "Hello, World!"
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
