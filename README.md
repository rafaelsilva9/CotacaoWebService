# CotacaoWebService
Trabalho acadêmico que consiste em uma aplicação console de cotação de moedas que consome um web service escrito em python utilizando o flask

- Passo a Passo -

1 - Leia o artigo abaixo:
	https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

2 - Instale o virtualenv e python
	https://pypi.python.org/pypi/virtualenv

3 - Clone o projeto em uma pasta desejada

4 - Execute o comando abaixo para criar um ambiente virtualenv
	$ virtualenv flask
	
5 - Execute o comando abaixo para atualizar a dependencia do requests
	$ source flask/bin/activate
	$ pip install requests

6 - Inicie o servidor do web service
	$ ./web-service.py
	
7 - Execute a aplicação que consome o web service
