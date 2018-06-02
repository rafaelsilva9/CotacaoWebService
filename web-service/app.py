import requests
import json
import os

def menu():
	again = 1
	os.system('clear')
	while(again == 1):
		print('Faca sua cotacao')
		chooseOption()
		print("1 - Nova cotacao")
		print("Outra tecla - Sair\n")
		again = input("Escolha uma opcao: ")
		os.system('clear')

def chooseOption():
	op = 0
	while(op != 1 and op != 2):
		print("1 - Converter real em dolar\n")
		print("2 - Converter dolar em real\n")
		op = input("Escolha uma opcao: ")
		os.system('clear')
		
		if (op != 1 and op != 2):
			print("Opcao invalida\n\n")
		else:
			getInput(op)
	
def getInput(op):
	value = -1.0
	while(not(value >= 0.0)):
		value = input("Digite o valor a ser convertido: ")		
		if (value >= 0.0):
			getQuoatation(op, value)
		else:
			print("Valor Invalido\n")
	
def getQuoatation(op, value):
	quotation = 0.0
	print("calculando ...")
	if (op == 1):
		response = requests.get('http://127.0.0.1:5000/cotacao/real/' + str(value))
		quotation = json.loads(response.text)
	elif (op == 2):
		response = requests.get('http://127.0.0.1:5000/cotacao/dollar/' + str(value))
		quotation = json.loads(response.text)
	os.system('clear')
	print("Resultado: " + str(quotation))
	
menu()