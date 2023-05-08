import os
import dotenv
import openai
import time

dotenv.load_dotenv(dotenv.find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = ""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

bot_context = f'Data e hora atual: {time.strftime("%d/%m/%Y %H:%M:%S")}\n'
bot_context += 'Dê respostas rápidas e objetivas e se possível use emojis para deixar a conversa mais amigável.\n'
bot_context += f'O usuário se chama {nome} e tem {idade} anos.\n'
bot_context += 'Você se chama BrainyMoura e é um assistente virtual que irá falar sobre a empresa Baterias Moura.\n'
bot_context += 'Não envie links que não foram citados abaixo.\n'
bot_context += '\nUse os dados abaixo para se atualizar: \n'
bot_context += '+80 centros de distribuições(Argentina, Brasil, Paraguai e Uruguai)\n'
bot_context += 'Site de vagas: https://grupomoura.gupy.io\n'
bot_context += 'Link distribuidores: https://www.moura.com.br/distribuidores\n'
bot_context += 'Contato descarte de baterias: (81) 3411.1439\n'
bot_context += 'Você poderá usar dados da internet para responder as perguntas.'

while user_input != 'sair':
    user_input = input("Digite sua dúvida: ")
    response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": bot_context},
        {"role": "user", "content": user_input},
    ])
    message = response.choices[0]['message']["content"]
    print(message)