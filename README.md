Projeto que cria CRUD's em Python, utilizando o Django Rest Framework

Sistema Linux:

<details>
  <summary><strong>🛠 Executando o código do projeto </strong></summary>
    
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

4. Ajuste os dados de login do MySQL
    * Logue no MySQL com esses dados:
        user = 'root'
        password = '207455'
    OU
    * Modifique usuário e senha dos seguintes arquivos
        para os seus dados que estão logados no MySQL:
    * ./backend/main/setting.py
       * DATABASES
          * default.USER = 'seu_usuario'
          * default.PASSWORD = 'sua_senha'
    * ./backend/main/mysql_db.py
       * mydb
          * user = 'seu_usuario'
          * password = 'sua_senha'

5. Crie e popule o banco de dados
    * Acesse a pasta backend:
    * `cd backend/`
    * Rode o arquivo mysql_db.py:
    * `python main/mysql_db.py`
    * Popule rodando os seguintes comandos em sequência:
    * `python manage.py makemigrations`
    * `python manage.py migrate`
    * `python manage.py loaddata imovel anuncio reserva`

6. Inicie o servidor localmente
    * `python manage.py runserver 8000`

7. Acesse o backend pelo navegador
    * Utilizando os templates do rest_framework:
    * `http://localhost:8000/imoveis/`
    * Rotas possíveis no arquivo 'urls.py' dentro da pasta 'api'
<details>
