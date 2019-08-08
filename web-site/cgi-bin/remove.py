#!/usr/bin/env python3.4
import cgi, cgitb, psycopg2, time, sys
sys.path.append("/usr/share/pyshared/song_request/")
from database import db
sys.stderr = sys.stdout
cgitb.enable()
print("Content-type: text/html\n\n")
if __name__ == "__main__":
    form = cgi.FieldStorage()
    ff = False
    try:
        song_ide=form["songId"].value
    except Exception as msg:
        print("<h1>Invalid Submission</h1>")
        ff = True
    if not ff:
        try:
            formDB = db()
            formDB.login()
            song_id = formDB.curr.execute("""DELETE FROM current WHERE uid = '"""+str(song_ide)+"""';""")
        except Exception as msg:
            link='http://dugdev.tk/oopsie.html'
        else:
            link='http://dugdev.tk/cgi-bin/hub.py'
        finally:
            formDB.logout()
    else:
        link='http://dugdev.tk/oopsie.html'
    print("""<meta http-equiv="refresh" content="0; URL='"""+link+"""'" />""")
