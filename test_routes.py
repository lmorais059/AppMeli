import requests

# URL da rota que você deseja verificar
url = 'http://localhost:5000/produto/1'

# Enviar uma solicitação GET para a rota
response = requests.get(url)

# Verificar o código de status da resposta
if response.status_code == 200:
    print('A rota está funcionando corretamente.')
    print('Resposta:', response.json())
else:
    print('Houve um erro ao acessar a rota.')
    print('Código de status:', response.status_code)
