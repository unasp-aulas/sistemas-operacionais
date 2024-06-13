import os
import json

tamanho, _ = os.get_terminal_size()

with open("questions.json", "r") as f:
    questions = json.load(f)

corretas = 0
incorretas = 0
for i in questions:
    print(f"#{i['id']} {i['question']} \n")
    for j in 'ABCD':
        print(f"({j}) {i['options'][j]}")
    print("\n")
    resposta = input("Resposta: ")
    if resposta.upper() == i['answer']:
        corretas += 1
        print("Correta")
    else:
        print("Incorreta")
    n = i['id']
    bar = f"{n}/{31} {chr(9608) * int(n * (tamanho - 6)/31)}"
    print(f"Total de corretas: {corretas}")
    print(bar)
    print(tamanho * "-")
