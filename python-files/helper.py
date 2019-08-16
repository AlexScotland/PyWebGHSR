import os
from database import *

def getUserAndPass():
    with open('login.dug','r') as document:
        username = document.readlines()
        document.close()
    return username[0].rstrip(), username[1].rstrip()

def printJobHTML(db,song_id, username):
    user_list = db.getSongName(song_id)
    print("""
      <form method="POST" enctype="multipart/form-data" action="../cgi-bin/singSong.py">
        <li><a onclick='' href = '#'>
        <button style='all: unset' name='songId' value='%s'>
            <h4><span> %s By %s </span></h4>
        </button>
          </a>
          <input name='username' value= %s style='display:none;'/>
        </li>
       </form>
    """%(song_id,user_list[0][0],str(user_list[0][1]), username,))
