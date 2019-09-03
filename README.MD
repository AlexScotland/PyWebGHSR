
# PYTHON-GHSR

**Developed by Alex Scotland**

## Project Info

DEMO:
http://dugdev.tk

Demo Of Dashboard:
http://dugdev.tk/cgi-bin/hub.py

Python GHSR is an open-sourced web-based guitarhero song request.

Using cgi and postgresql, it is simple to import your songs and have a fully functioning song request for what ever purpose you need :)

## Getting Started

* edit song_add.py to your song_list provided by CloneHero or GH3

* Run Database functions:

* CREATE DATABASE songs;

* CREATE TABLE songs (uid SERIAL UNIQUE,song_name TEXT,artist TEXT);

* CREATE TABLE current (uid TEXT, requester TEXT);

* run song_add.py to have the songs imported.

* Move respective folders to areas

* Name Databases appropriately.

Voila!  All done!

### Prerequisites

[Python 3.4+](https://www.python.org/downloads/)

Database:

[postgresql](https://www.postgresql.org/download/)

Libraries:

[pyscopg2](https://pynative.com/python-postgresql-tutorial/#genesis-content)

## Running the tests

edit song_add.py to your song_list provided by CloneHero or GH3

run song_add.py to have the songs imported.

## Built With

* [Centos 7](https://www.centos.org/download/) - OS on the server
* [Apache Httpd](https://httpd.apache.org/) - Webserver

## Head Programmers

* [Alex Scotland](https://github.com/AlexScotland)
