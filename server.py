from flask import Flask, render_template, request, redirect
from mysqlconn import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL('mydb')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    print(request.form)

    db = connectToMySQL("mydb")

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(ln)s, %(occup)s, NOW(), NOW());"
    data = {
        "ln": request.form["lname"],
        "occup": request.form["occ"]
        }

    db.query_db(query,data) 
    return redirect("/")

            
if __name__ == "__main__":
    app.run(debug=True)
    