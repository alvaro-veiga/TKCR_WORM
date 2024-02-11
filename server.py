#!/usr/bin/python

from Crypto.Cipher import AES
import socket, base64, os, time, sys, select


# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# one-liners to encrypt/encode and decrypt/decode a string(criptografa/codifica e descriptografa/decodifica uma string)
# encrypt with AES, encode with base64(criptografa com AES, codifica com base64)
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))
