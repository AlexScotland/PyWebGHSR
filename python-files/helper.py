import os

def getUserAndPass():
    with open('login.dug','r') as document:
        username = document.readlines()
        document.close()
    return username[0].rstrip(), username[1].rstrip()
