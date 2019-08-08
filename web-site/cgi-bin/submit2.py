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
        name=form["name"].value
        song_name=form["song_name"].value
    except:
        print("<h1>Invalid Submission</h1>")
        ff = True
    if not ff:
        try:
            formDB = db()
            formDB.login()
            exact = formDB.findSongName(song_name)
            if exact != []:
                songs_id =exact[0][0]
                formDB.curr.execute("""INSERT INTO current (uid, requester) VALUES (%s, %s);""", (songs_id, name))
            else:
                song_name = song_name.lower()
                print(song_name)
                song_id = formDB.curr.execute("""SELECT uid FROM songs WHERE song_name LIKE '%"""+song_name+"""%' LIMIT 1;""")
                resList=formDB.curr.fetchmany(1)
                songs_id=resList[0][0]
                ### upload to table##
                formDB.curr.execute("""INSERT INTO current (uid, requester) VALUES (%s, %s);""", (songs_id, name))
        except Exception as msg:
            print(msg)
            link='http://dugdev.tk/oopsie.html'
        else:
            link='http://dugdev.tk/submission_complete.html'
        finally:
            formDB.logout()
    else:
        link='http://dugdev.tk/oopsie.html'
    print("""<meta http-equiv="refresh" content="0; URL='"""+link+"""'" />""")
