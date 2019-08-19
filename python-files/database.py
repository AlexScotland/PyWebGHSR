import psycopg2
from helper import *
class db:
    #class helper functions
    def __init__(self):
        self.dbname = "songdb"
        with open('/usr/share/pyshared/song_request/python-files/login.dug','r') as creds:
            lines = creds.readlines()
            self.user =lines[0]
            self.user=self.user.strip()
            self.password=lines[1]
            self.password=self.password.strip()
        self.host="localhost"

    def login(self):
        try:
            self.conn = psycopg2.connect(dbname = self.dbname, user = self.user, password = self.password, host = self.host)
            self.conn.autocommit=True
            self.curr = self.conn.cursor()
            return self.conn

        except Exception as msg:
            print(msg)
            return False

    def logout(self):
        try:
            self.curr.close()
            self.conn.close()
        except Exception as msg:
            print('\033[1;37;40m')
            return False

    def addSong(self,song_name,artist):
        try:
            res=self.curr.execute("""INSERT INTO songs (song_name, artist) VALUES (%s, %s);""",(song_name,artist,))
        except Exception as msg:
            print('There was an error with song:  '+song_name)
        else:
            return True

    def getSongName(self,id):
        try:
            res=self.curr.execute("""SELECT song_name, artist FROM songs WHERE uid = '"""+str(id)+"""';""")
            resultList=self.curr.fetchmany()
        except Exception as msg:
            print(msg)
            print('There was an error with song:  '+str(id))
        else:
            return resultList
    def findSongName(self, song_name):
        try:
            res=self.curr.execute("""SELECT uid FROM songs WHERE song_name = %s;""",(song_name,))
            resultList=self.curr.fetchmany(1)
        except Exception as msg:
            print(msg)
            print('There was an error with song:  '+str(song_name))
        else:
            return resultList
