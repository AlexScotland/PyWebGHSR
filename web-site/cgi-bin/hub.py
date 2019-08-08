#!/usr/bin/env python3.4
import cgi, cgitb, psycopg2, time, sys
sys.path.append("/usr/share/pyshared/song_request/")
from database import db

def printJobHTML(db,song_id, username):
    user_list = db.getSongName(song_id)
    print("""
      <form method="POST" enctype="multipart/form-data" action="../cgi-bin/remove.py">
        <li><a onclick='' href = '#'>
        <button style='all: unset' name='songId' value='%s'>
            <h4><span> %s By %s | Requested by %s</span></h4>
        </button>
          </a>
        </li>
       </form>
    """%(song_id,user_list[0][0],user_list[0][1], username,))

sys.stderr = sys.stdout
cgitb.enable()
db = db()
print("Content-Type: text/html\n")
db.login()
count_query = db.curr.execute( """SELECT * FROM current;""")
result_list = db.curr.fetchall()
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
    <title>Hub</title>
    <!-- Favicon-->
    <link rel="icon" type="image/png" href="/images/icons/favicon.ico"/>
</head>""")
print("""
<body>
<ul>
""")


for i in range(len(result_list)):
    printJobHTML(db,result_list[i][0],result_list[i][1])


print("""
</ul>
</body>
</html>
""")
db.logout()
# print("""<meta http-equiv="refresh" content="0; URL='http://dugdev.tk/cgi-bin/hub.py'" />""")
