import json
import requests
import hashlib

#funcao para salvar o json 
def salvar(lista):
    with open('answer.json', 'w') as f:
        json.dump(lista, f)

#abrir o arquivo json
def abrir(arquivo):
    with open('answer.json', 'r') as f:
            return json.load(f)
#requisicao http passando o token 
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=Your_Token')
if r.status_code == 200:
    resposta = json.loads(r.content)
    salvar(resposta)
    print("Answer.json gerado com sucesso!")


print (resposta['cifrado'])

#Algoritmo para descriptografar julio cesar

message=resposta['cifrado']
alphabet='abcdefghijklmnopqrstuvwxyz'
key=resposta['numero_casas']
decrypt=''

for i in message:
    pos=alphabet.find(i)
    newpos=(pos-key)%26
    decrypt+=alphabet[newpos]

#Mostrando mensagem descriptografa, inserindo resultado no json, salvando arquivo.    
print(decrypt)
resposta['decifrado'] = decrypt
salvar(resposta)
print("atualizado descriptografia json..")

#Gerando resumo sha1
with open('answer.json', 'r') as f:
            encoding = f.encoding

resumo = hashlib.sha1(resposta['decifrado'].encode(encoding)).hexdigest()
resposta['resumo_criptografico'] = resumo
#atualizando o arquivo
salvar(resposta)
print("arquivo pronto para envio...")
