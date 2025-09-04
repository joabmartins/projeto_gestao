# projeto_gestao

## 1. gitignore
Os arquivos e pastas definidos nesse arquivo não serão enviados para o repositório remoto (github), ficarão apenas no computador local.
## 2. docker-compose
Arquivo de configuração das imagens, containers e volumes do docker. Só precisa executar o comando abaixo uma vez no terminal.
```
docker-compose up -d
```
## 3. ambiente virtual
Para que as bibliotecas instaladas não afetem o ambiente de outras pessoas ou outro projetos, é recomendado usar um ambiente virtual. Com isso, se você importar o pandas 1.0 ele só vai estar no seu ambiente virtual, após sair dele é possível entrar em outro e importar o pandas 2.0 e um não interfere no outro.
```
# para criar o ambiente virtual digite em um terminal:
python -m venv <um nome qualquer para o ambiente virtual>

# para acessar o ambiente virtual digite em um terminal:
.\<nome dado ao ambiente>\Scripts\activate
```