Projeto que cria CRUD's em Python, utilizando o Django Rest Framework

Sistema Linux:

<details>
  <summary><strong>‼️ Para testar o código do projeto </strong></summary>
    
1. Clone o repositório
    * `git clone git@github.com:VictorMartinsDuarte/django_rest_api.git`.
    * Entre na pasta do repositório que você acabou de clonar:
    * `cd django_rest_api`

2. Configure o Ambiente Virtual
    * Crie o ambiente, rode dentro da pasta raiz do projeto:
    * `python3 -m venv venv`
    * Ative-o:
    * `source venv/bin/activate`

3. Instalando as dependências
    * `pip install -r requirements.txt`

4. Crie e popule o banco de dados
    * Credenciais user e senha ou env auto:
    * Acesse a pasta backend:
    * `cd backend/`
    * Rode o arquivo mysql_db.py:
    * `python main/mysql_db.py`
    * Popule rodando os seguintes comandos em sequência:
    * `python manage.py makemigrations`
    * `python manage.py migrate`
    * `python manage.py loaddata imovel anuncio reserva`

5. Inicie o servidor localmente
    * `python manage.py runserver 8000`

6. Acesse o backend pelo navegador
    * Utilizando os templates do rest_framework:
    * `http://localhost:8000/imoveis/`
    * Rotas possíveis no arquivo 'urls.py' dentro da pasta 'api'
<details>