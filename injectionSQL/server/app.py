from flask import Flask, render_template, request
from database.database import create_tables

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')



if __name__ == "__main__":
    create_tables()
    app.run(debug=True)