#!/usr/bin/env python3

import os

usuario = "seu_usuario"

projectname = input("Defina o título do projeto: ")

description = input("Defina a descrição do projeto: ")

comando = 'curl -u ' + usuario + ' https://api.github.com/user/repos ' + "'" + '-d' + '{"name":"' + projectname + '","description":"' + description + '"}' + "'"

print(comando)
os.system(comando)
