# BrainyMoura - Backend
BrainyMoura é um assistente virtual que responde a qualquer pergunta relacionada a empresa Baterias Moura.

## Instalação
## Requisitos
- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Git](https://git-scm.com/downloads) (opcional)
- [Conta no OpenAI](https://beta.openai.com/)

### Clone o repositório
Baixe o repositório no terminal com o comando:
```bash
git clone https://github.com/misterioso013/BrainyMoura-backend.git
```
> ou baixe o [arquivo zip aqui](https://github.com/misterioso013/BrainyMoura-backend/archive/refs/heads/master.zip).

### Instale as dependências
```bash
pip install -r requirements.txt
```

### Crie um arquivo .env
Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API do OpenAI:
```
OPENAI_API_KEY="sk-..."
```
> Você pode encontrar sua chave de API [aqui](https://platform.openai.com/account/api-keys).

## Como usar
### Inicie o servidor
```bash
python main.py
```
