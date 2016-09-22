#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

import os

usuario = "seu_usuario"

print 'Defina o título do projeto: '
projectname = raw_input()

print 'Defina a descrição do projeto: '
description = raw_input()

comando = 'curl -u ' + usuario + ' https://api.github.com/user/repos ' + "'" + '-d' + '{"name":"' + projectname + '","description":"' + description + '"}' + "'"

print(comando)
os.system(comando)
