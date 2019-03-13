#!/usr/bin/env python3
#
# GrimTurn trusted mac address
# Created By m0d

from time import sleep
from core import wcolors
from core import help
from peewee import SqliteDatabase, Model, TextField, fn
import os

options = ["res/MACRES.sqlite"]
db = SqliteDatabase(options[0])

class CAM(Model):
    MAC = TextField()
    IP = TextField()

    class Meta:
        database = db

db.connect()

def trusted_mac():
    mac = CAM.select().order_by(fn.Random()).get()
    return str(mac.MAC)

db.close()
