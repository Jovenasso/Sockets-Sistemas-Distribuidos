#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def isPrime(n):
  start = 2

  while start <= math.sqrt(n):
    if n % start < 1:
      return False
    start += 1

  return n > 1


import socket
import time
import math
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind(("localhost", 50002))
  print(s)
  while True:
    s.listen()
    conexao, addr = s.accept()
    with conexao:
      print(f"Cliente conectado: {addr}")
      while True:
        dados = conexao.recv(1024)
        if not dados:
          break
        print(f"Mensagem recebida: {dados.decode()}")
        #conexao.sendall(b"Dados recebidos!")
        msg = dados.decode()
        msgs = msg.split("|",1)
        #print(msgs[0])
        #print(msgs[1])
        if int(msgs[0]) >= 1000000:
          if int(msgs[1]) <= 15000 and int(msgs[1]) >= 5000:
            contprimo = 0
            n = int(msgs[1])
            codigo = int(msgs[0])+1
            while contprimo < n:
              if isPrime(codigo) == True:
                contprimo += 1
              codigo += 1
            print(codigo-1)
            conexao.sendall(str(codigo-1).encode())
          else:
            conexao.sendall(b"N invalido")
        else:
          conexao.sendall(b"Codigo invalido")

