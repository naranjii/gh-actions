import os
import requests

# Acessando o segredo, que pode ser a URL do webhook
webhook_url = os.getenv("SEGREDO")
message = "Aqui está a mensagem que eu quero enviar para o Webhook!"

# Enviando a mensagem para o webhook
response = requests.post(webhook_url, json={"content": message})

# Verificando a resposta
if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Erro ao enviar mensagem. Status code: {response.status_code}")
