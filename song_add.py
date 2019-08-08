import psycopg2, io
from database import *

database=db()
database.login()
with open('songs','r') as reader:
    for line in reader:
        current_song=line.split(',')
        if len(current_song) > 1:
            current_song[1]=current_song[1].rstrip()
            current_song[1]=current_song[1].lstrip()
            current_song[1]=current_song[1].lower()
            database.addSong(current_song[1],current_song[0])
        else:
            current_song[0]=current_song[0].rstrip()
            current_song[0]=current_song[0].lstrip()
            current_song[0]=current_song[0].lower()
database.logout()
