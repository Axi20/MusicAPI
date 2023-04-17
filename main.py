from flask import *
import json
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/view")
def view():
    con = sqlite3.connect("MusicDB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Music")
    rows = cur.fetchall()
    return json.dumps([dict(ix) for ix in rows])

@app.route("/savedetails/", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        data = request.get_json(force=True)
        print(data)
        Title = data["title"]
        Singer = data["singer"]
        Genre = data["genre"]
        Timeline = data["timeline"]
 
        with sqlite3.connect("MusicDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Music (Title, Singer, Genre, Timeline) values (?,?,?,?)", (Title, Singer, Genre, Timeline))
            con.commit()
            msg = "Music successfully Added"
    except:
        con.rollback()
        msg = "We can not add the music to the list"
    finally:
        return Title
        con.close()

@app.route("/deleterecord/", methods=["POST"])
def deleterecord():
    data = request.get_json(force=True)
    id = str(data["id"])
    print(id)
    with sqlite3.connect("MusicDB.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Music where id = ?", id)
            msg = "Record successfully deleted"
        except:
            msg = "Record can't be deleted"


@app.route("/updatedetails/", methods=["POST"])
def updaterecord():
    try:
        data = request.get_json(force=True)
        id = data["id"]
        Title = data["title"]
        Singer = data["singer"]
        Genre = data["genre"]
        Timeline = data["timeline"]

        with sqlite3.connect("MusicDB.db") as con:
            cur = con.cursor()
            cur.execute("UPDATE Music SET Title=?, Singer=?, Genre=?, TimeLine=? WHERE id=?", (Title, Singer, Genre, Timeline, id))
            con.commit()
            msg = "Music successfully updated"
    except:
        con.rollback()
        msg = "We can not update the music to the list"
    finally:
        return msg
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
