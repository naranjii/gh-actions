import os
import requests

# Acessando o segredo, que pode ser a URL do webhook
webhook_url = "https://webhook.site/9ea504d7-0312-4901-ba0e-39904f70d515"
message = os.envinron.get("SEGREDO")
# Enviando a mensagem para o webhook
response = requests.post(webhook_url, json={"content": message})

# Verificando a resposta
if response.status_code == 200:
    print("Mensagem enviada com sucesso!")
else:
    print(f"Erro ao enviar mensagem. Status code: {response.status_code}")
