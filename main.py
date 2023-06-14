import os
import dotenv
import openai
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

dotenv.load_dotenv(dotenv.find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")


def resposta(nome, idade, user_input):
    bot_context = f'Data e hora atual: {time.strftime("%d/%m/%Y %H:%M:%S")}\n'
    bot_context += "Dê respostas rápidas e objetivas e se possível use emojis para deixar a conversa mais amigável.\n"
    bot_context += f"O usuário se chama {nome} e tem {idade} anos.\n"
    bot_context += "Você se chama BrainyMoura e é um assistente virtual que irá falar sobre a empresa Baterias Moura com foco em sustentabilidade\n"
    bot_context += "Não envie links que não foram citados abaixo.\n"
    bot_context += "Tente falar mais sobre Sustentabilidade e principalmente na Moura\n"
    bot_context += "\nUse os dados abaixo para se atualizar: \n"
    bot_context += (
        "+80 centros de distribuições(Argentina, Brasil, Paraguai e Uruguai)\n"
    )
    bot_context += "Site de vagas: https://grupomoura.gupy.io\n"
    bot_context += "Link distribuidores: https://www.moura.com.br/distribuidores\n"
    bot_context += "Contato descarte de baterias: (81) 3411.1439\n"
    bot_context += "Você poderá usar dados da internet para responder as perguntas."
    bot_context += "Conceição Moura é esposa de Edson Mororó Moura e eles fundaram a empresa em 1957.\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": bot_context},
            {"role": "user", "content": user_input},
        ],
    )
    message = response.choices[0]["message"]["content"]
    return message


app = Flask(__name__)

CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    nome = data["nome"]
    idade = data["idade"]
    # Se tiver vazio retorna "oi"
    user_input = data["prompt"] if data["prompt"] else "oi"
    response = jsonify({"resposta": resposta(nome, idade, user_input)})
    return response


if __name__ == "__main__":
    app.run(debug=True)
