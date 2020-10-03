from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    #add your webhook logic here and return a response

if __name__=='__main__':
    app.run()