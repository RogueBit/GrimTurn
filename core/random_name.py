#!/usr/bin/env python3
#
# GrimTurn Menu module
# Created By m0d

from time import sleep
from core import wcolors
from core import help
from peewee import SqliteDatabase, Model, TextField, fn
import os

options = ["res/NAMRES.sqlite"]
db = SqliteDatabase(options[0])

class WORDS(Model):
    WORD = TextField()
    TYPE = TextField()

    class Meta:
        database = db

db.connect()

def random_name():
	adjective = WORDS.select().where(WORDS.TYPE == 'A').order_by(fn.Random()).get()
	noun = WORDS.select().where(WORDS.TYPE == 'N').order_by(fn.Random()).get()
	return(str(adjective.WORD+noun.WORD))

db.close()
