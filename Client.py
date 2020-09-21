#!/usr/bin/env python3

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

username = input("What is your username?\n")

if username != "":
    password = input("Password?\n")

print(s.user.getUsers('0', username, password))

print(s.system.listMethods())
