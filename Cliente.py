# -*- coding: cp1252 -*-
import socket

var1 = str(input("Código Inicial:"))
var2 = str(input("N:"))
var3 = var1 + "|" + var2

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(("localhost", 50002))
  print(s)
  s.sendall(var3.encode())
  dados = s.recv(1024)
  print(f"Resposta do servidor: {dados.decode()}")
