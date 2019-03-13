#!/usr/bin/env python3
#
# GrimTurn casper module
# Created By m0d

import os
import subprocess
from core import wcolors
from core import help
from core import random_name
from core import trusted_mac
from time import sleep
options = ["eth0", "y"]
def casper():
        try:
                line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "GrimTurn" + wcolors.color.ENDC
                line_1 += ":"
                line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "casper" + wcolors.color.ENDC
                line_1 += " > "
                com = input(line_1)
                com = com.lower()
                if com[0:13] =='set interface':
                        options[0] = com[14:20]
                        print("INTERFACE => ", options[0])
                        casper()
                elif com[0:12] =='set hostname':
                        options[1] = com[13:14]
                        print ("Hostname => ", options[1])
                        casper()
                elif com[0:12] =='show options':
                        print ("")
                        print ("Options\t\t Value\t\t\t RQ\t Description")
                        print ("---------\t--------------\t\t----\t--------------")
                        print ("Interface\t"+options[0]+"\t\t\tyes\tNetwork Interface Name")
                        print ("Hostname\t"+options[1]+"\t\t\tyes\tRandomize hostname")
                        print ("")
                        casper()
                elif com[0:2] =='os':
                        os.system(com[3:])
                        casper()
                elif com[0:4] =='help':
                        help.help()
                        casper()
                elif com[0:4] =='exit':
                        pass
                elif com[0:3] =='run':
                        sleep(1)
                        trumac = trusted_mac.trusted_mac()
                        raname = random_name.random_name()
                        if options[1] == "y":
                            cmd = 'sed -i \'s/send host-name = ".*";/send host-name = "{}";/g\' /etc/dhcp/dhclient.conf'.format(raname)
                            print(wcolors.color.GREEN + "Setting hostname => " + cmd)
                            retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                            cmd = "hostname {}".format(raname)
                            print(wcolors.color.GREEN + "Setting hostname => " + cmd)
                            retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                            cmd = 'echo {} >/etc/hostname'.format(raname)
                            retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                            print(wcolors.color.GREEN + "Setting hostname => " + cmd)
                        cmd = "ip link set down " + options[0] + " && macchanger --mac=" + trumac + " " + options[0] + " && ip link set up " + options[0]
                        print(wcolors.color.GREEN + "Setting MAC => " + cmd)
                        retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                        cmd = "dhclient -r " + options[0]
                        print(wcolors.color.GREEN + "DHCP => " +cmd)
                        retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                        cmd = "dhclient -v " + options[0]
                        print(wcolors.color.GREEN + "DHCP => " + cmd)
                        retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                        cmd = "ip link set down {nic} && ip link set up {nic}".format(nic=options[0])
                        print(wcolors.color.GREEN + "Bouncing NIC => " + cmd)
                        retVal = subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=True, timeout=None)
                        casper()
                else:
                        print ("Wrong Command => ", com)
        except(KeyboardInterrupt,OSError):
                        print(wcolors.color.RED + "\n[*] (Ctrl + C ) Detected, Module Exit" + wcolors.color.ENDC)
