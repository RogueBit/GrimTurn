#!/usr/bin/env python3
#
#            --------------------------------------------------
#                            GrimTurn
#            --------------------------------------------------
#        Copyright (C) <2017>  <m0d>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os
import readline, rlcompleter
from time import sleep
from core import wcolors
from core import menu
from core import header
from core import modules_database
from core import help
from core import upgrade
from core import update
from core import about
from core import random_name
from core import trusted_mac
from modules import casper

def main():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "GrimTurn" + wcolors.color.ENDC
        line_1 += " > "
        terminal = input(line_1)
        if terminal[0:3] =='use':
            if terminal[4:15] =='host/casper':
                casper.casper()
                main()
            else:
                print("Wrong Command =>", terminal)
                main()
        elif terminal[0:12] == 'show modules':
            modules_database.modules_database()
            main()
        elif terminal[0:4] =='help':
            help.help()
            main()
        elif terminal[0:2] =='os':
            os.system(terminal[3:])
            main()
        elif terminal[0:7] =='upgrade':
            upgrade.upgrade()
            main()
        elif terminal[0:6] =='update':
            update.update()
        elif terminal[0:5] =='about':
            about.about()
            main()
        elif terminal[0:13] =='generate_name':
            print(random_name.random_name())
            main()
        elif terminal[0:11] =='trusted_mac':
            print(trusted_mac.trusted_mac())
            main()
        elif terminal[0:4] =='exit':
            print(wcolors.color.YELLOW + "[*] Thank You For Using GrimTurn =)" + wcolors.color.ENDC)
            exit()
        else:
            print("Wrong Command =>", terminal)
            main()
    except(KeyboardInterrupt):
        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Trying To Exit ..." + wcolors.color.ENDC)
        print(wcolors.color.YELLOW + "[*] Thank You For Using GrimTurn =)" + wcolors.color.ENDC)
def start():
    header.main_header()
    menu.main_info()
    main()
if __name__=='__main__':
    start()
