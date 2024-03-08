import requests
import base64

class ManipulaRepositorios:
    # Inicializa o Objeto ManipulaRepositorios
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token='xxx'
        self.headers = {'Authorization':"Bearer " + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}

    def cria_repo(self, nome_repo):
        '''
        Cria um repositório no HGitHub utilizando api

        Recebe a api base, header e o nome do repositório

        Retorna o Status da requisição, 2xx para requisições com sucesso
        '''
        data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": False
        }
        response = requests.post(f"{self.api_base_url}/user/repos", 
                                 json=data, headers=self.headers)

        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        '''
        Realiza o upload dos arquivos no repositório criado no GitHub

        Recebe o nome do repositório, nome do arquivo e caminho do arquivo

        Retorna o Status da requisição, 2xx para requisições com sucesso
        '''
        # Codificando o arquivo
        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": "Adicionando um novo arquivo",
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')

# instanciando um objeto
novo_repo = ManipulaRepositorios('marceloregys')

# Criando o repositório
nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'data_processed/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'data_processed/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'data_processed/linguagens_spotify.csv')