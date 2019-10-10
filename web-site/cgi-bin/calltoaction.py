#!/usr/bin/env python3.4
import cgi, cgitb, psycopg2, time, sys
sys.path.append("/usr/share/pyshared/song_request/python-files/")
from database import db
sys.stderr = sys.stdout
cgitb.enable()
print("Content-type: text/html\n\n")
if __name__ == "__main__":
    printer = False
    form = cgi.FieldStorage()
    ff = False
    try:
        song=form["song_name"].value
        artist=form["artist_name"].value
        requester=form["requester"].value
    except:
        print("<h1>Invalid Submission</h1>")
        ff = True
    if not ff:
        try:
            req_db = db()
            req_db.login()
        except Exception as msg:
            print(msg)
            link='http://dugdev.tk/oopsie.html'
        else:
            req_db.insertRequest(song,artist,requester)
            link='http://dugdev.tk/submission_complete.html'
        finally:
            printer = True
            req_db.logout()
    else:
        link='http://dugdev.tk/oopsie.html'
    if printer:
        print("""<meta http-equiv="refresh" content="0; URL='"""+link+"""'" />""")
        print('movin')
