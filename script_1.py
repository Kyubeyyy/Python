# Programa simples de entrada e saída de dados no Python

print("Olá!")
nome = input("Digite seu nome: ")
print("Seja bem vindo(a),",nome, "\nVamos lá!")

def obter_data_nascimento():
    print("Digite sua data de nascimento:")
    dia = input("Dia:")
    mês = input("Mês:")
    ano = input("Ano:")
    print("Sua data de nascimento é: ")
    print(dia,mês,ano,sep="/")

    confirma = input("Correto? Digite sim ou não: ")
    if confirma.capitalize() == "Sim":
        print("Prosseguindo...")
        print("Fim do programa")
    elif confirma.capitalize() == "Não":
        confirma2 = input("Voltar? Digite sim ou não: ")
        if confirma2.capitalize() == "Não":
            print("Prosseguindo...")
            print("Fim do programa")
        elif confirma2.capitalize() == "Sim":
            obter_data_nascimento()

obter_data_nascimento()
        
#Fim do programa 
