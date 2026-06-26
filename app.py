from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient(
    "mongodb://admin:QWERTY@mongo:27017/?authSource=admin"
)

db = client["university"]
collection = db["users"]


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Add User
@app.route("/addUser", methods=["POST"])
def add_user():

    user_data = {
        "email": request.form["email"],
        "username": request.form["username"],
        "password": request.form["password"]
    }

    collection.insert_one(user_data)

    print("User saved in MongoDB")

    return "User saved in MongoDB successfully"


# View All Users
@app.route("/users")
def users():

    data = list(
        collection.find({}, {"_id": 0})
    )

    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)