#!/usr/bin/env python3
#
# GrimTurn help
# Created By m0d

from core import wcolors
from time import sleep
def help():
    print ("\n")
    print (wcolors.color.BLUE + "Commands\t\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "---------------\t\t----------------" + wcolors.color.ENDC)
    print ("show modules\t\tShow Modules of Current Database")
    print ("show options\t\tShow Current Options Of Selected Module")
    print ("use \t\t\tSelect Module For Use")
    print ("set    \t\t\tSet Value Of Options To Modules")
    print ("run \t\t\tExecute Module")
    print ("os \t\t\tRun Linux Commands(ex : os ifconfig)")
    print ("generate_name\t\tGenerate a Name")
    print ("trusted_mac\t\tReturn a Trusted MAC Address")
    print ("about\t\t\tAbout Us")
    print ("exit\t\t\tExit Current Module or Program")
    print ("")
