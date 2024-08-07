"""Aqui eu coloco o que o meu módulo faz"""
from os import system

def clear():
    try:
        system('cls')   # Windows
    except:
        system('clear') # Linux

var = 'valor'
