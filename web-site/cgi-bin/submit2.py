#!/usr/bin/env python3.4
import cgi, cgitb, psycopg2, time, sys
sys.path.append("/usr/share/pyshared/song_request/python-files/")
from database import db
from helper import *

sys.stderr = sys.stdout
cgitb.enable()
print("Content-type: text/html\n\n")
if __name__ == "__main__":
    printer = False
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
                song_id = formDB.curr.execute("""SELECT uid FROM songs WHERE song_name LIKE '%"""+song_name+"""%';""")
                resList=formDB.curr.fetchall()
                if len(resList)> 1:
                    printer = False
                    print("""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <!-- Required meta tags-->
                        <meta charset="UTF-8">
                        <link href="/css/styled.css" rel="stylesheet" media="all">
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">
                        <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/css?family=Titillium+Web:300,700,300italic'>
                        <!-- Title Page-->
                        <title>Select your song!</title>
                        <!-- Favicon-->
                        <link rel="icon" type="image/png" href="/images/icons/favicon.ico"/>
                    </head>""")
                    print("""
                    <h1>Select your song below</h1>
                    <body>
                    <ul>
                    """)
                    for i in resList:
                        count_query = formDB.curr.execute( """SELECT * FROM songs WHERE uid = %s;""",(i[0],))
                        result_list = formDB.curr.fetchall()
                        for i in range(len(result_list)):
                            try:
                                printJobHTML(formDB,result_list[i][0],name)
                            except:
                                pass


                    print("""
                    </ul>
                    </body>
                    </html>
                    """)
                else:
                    printer = True
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
    if printer:
        print("""<meta http-equiv="refresh" content="0; URL='"""+link+"""'" />""")
        print('movin')
