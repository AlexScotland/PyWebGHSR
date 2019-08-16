#!/usr/bin/env python3.4
import cgi, cgitb, psycopg2, time, sys
sys.path.append("/usr/share/pyshared/song_request/python-files/")
from database import db
sys.stderr = sys.stdout
cgitb.enable()
print("Content-type: text/html\n\n")
if __name__ == "__main__":
    form = cgi.FieldStorage()
    ff = False
    try:
        name=form["username"].value
        song_name=form["songId"].value
    except:
        print("<h1>Invalid Submission</h1>")
        ff = True
    if not ff:
        try:
            formDB = db()
            formDB.login()
            formDB.curr.execute("""INSERT INTO current (uid, requester) VALUES (%s, %s);""", (song_name, name))
        except Exception as msg:
            print(msg)
            link='http://dugdev.tk/oopsie.html'
        else:
            link='http://dugdev.tk/submission_complete.html'
        finally:
            formDB.logout()
    print("""<meta http-equiv="refresh" content="0; URL='"""+link+"""'" />""")
