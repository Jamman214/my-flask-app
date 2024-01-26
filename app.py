from flask import Flask

app = Flask(__name__)

file_location = getenv("msg.txt", "msg.txt")

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        with open(file_location, "wb+") as f:
            f.write(request.get_data())
        return "Successfully updated message"
    elif request.method == "GET":
        try:
            with open(file_location, "rb") as f:
                return f.read()
        except FileNotFoundError:
            return "No message found"
