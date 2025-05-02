import pickle
# Variabeis dos clientes

try:
    with open("dados.pkl", "rb") as arquivo:
        dados = pickle.load(arquivo)
        nome_cliente = dados["nome"]
        saldo = int(dados["saldo"])
except FileNotFoundError:
    nome_cliente = "Tadeo"
    saldo = 0
    with open("dados.pkl", "wb") as arquivo:
        pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)

# Variabeis dos Gerente

senha = "gato123"

# Codigo

# Bem-vindo

contador = True
while contador == True:
    print("\n\nBem-vindo ao Sistema Bancário!\n")
    print("Escolha uma opcao:")
    print("1. Acessar como Cliente")
    print("2. Acessar como Gerente")
    print("3. Sair")

    opcion1 = int(input("\nQual é sua escolha: "))

# Menu Cliente

    if opcion1 == 1:
        contador2 = True
        while contador2 == True:
            print("\n\nMenu Cliente: \n")
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Sacar/Pix")
            print("4. Simular Rendimiento")
            print("5. Voltar ao Menu Principal")
        
            opcion2 = int(input("\nQual é sua escolha: "))
        
            if opcion2 == 1: 
                contador3 = True
                while contador3 == True:
                    print(f"\nO seu saldo é {saldo}")
                    print("\n1. Se deseja sair do banco")
                    print("2. Se deseja voltar ao menu principal")
                    print("3. Se deseja saber seu saldo novamente")
                    opcion3 = int(input("\nQual é sua escolha: "))
                    if opcion3 == 1:
                        print("\nObrigado volte sempre :)")
                        contador3 = False
                        contador2 = False
                        contador = False
                    elif opcion3 == 2:
                        contador3 = False
                        contador2 = False
                    elif opcion3 == 3:
                        contador3 = True
                    else:
                        print("\nEscolha errada")
            elif opcion2 == 2: 
                contador3 = True
                while contador3 == True:
                    print(f"\nSeu saldo é: {saldo}")
                    deposito = int(input("\nQuanto deseja depositar: "))
                    saldo = saldo + deposito
                    print(f"\nSeu saldo é: {saldo}")
                    with open("dados.pkl", "wb") as arquivo:
                        pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)
                    print("\n1. Se deseja sair do banco")
                    print("2. Se deseja voltar ao menu principal")
                    print("3. Se deseja depositar novamente")
                    opcion3 = int(input("\nQual é sua escolha: "))
                    if opcion3 == 1:
                        print("\nObrigado volte sempre :)")
                        contador3 = False
                        contador2 = False
                        contador = False
                    elif opcion3 == 2:
                        contador3 = False
                        contador2 = False
                    elif opcion3 == 3:
                        contador3 = True
                    else:
                        print("\nEscolha errada")
            elif opcion2 == 3: 
                contador3 = True
                while contador3 == True:
                    print(f"\nSu saldo es: {saldo}")
                    print("\n1. Deseja sacar")
                    print("2. Enviar pix")
                    opcion4 = int(input("\nQual é sua escolha: "))
                    if opcion4 == 1:
                        saque = int(input("\nQuanto deseja sacar: "))
                        if saldo > saque:
                            saldo = saldo - saque
                            with open("dados.pkl", "wb") as arquivo:
                                pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)
                            print(f"\nSeu saldo é: {saldo}")
                        else:
                            print("\nSaldo insuficiente deseja um emprestimo?")
                    elif opcion4 == 2:
                        pix = int(input("\nQual é o pix ao qual deseja enviar? "))
                        saque = int(input("\nQuanto deseja enviar? "))
                        if saldo > saque:
                            saldo = saldo - saque
                            with open("dados.pkl", "wb") as arquivo:
                                pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)
                            print(f"\n{saque} foram eviados para o pix {pix}")
                            print(f"\nSeu saldo é: {saldo}")
                        else:
                            print("\nSaldo insuficiente deseja um emprestimo?")

                    print("\n1. Se deseja sair do banco")
                    print("2. Se deseja voltar ao menu principal")
                    print("3. Se deseja retirar novamente")
                    opcion3 = int(input("\nQual é sua escolha: "))
                    if opcion3 == 1:
                        print("\nObrigado volte sempre :)")
                        contador3 = False
                        contador2 = False
                        contador = False
                    elif opcion3 == 2:
                        contador3 = False
                        contador2 = False
                    elif opcion3 == 3:
                        contador3 = True
                    else:
                        print("\nEscolha errada")
            elif opcion2 == 4: 
                contador3 = True
                while contador3 == True:
                    print("\nSimulemos o seu Rendimento\n")
                    mes = 1
                    while mes <= 12:
                        rendimento = (saldo * ((1+0.011)**mes)) - saldo
                        #rendimento = round(rendimento, 2)
                        print(f"O rendimento do mes {mes} é {rendimento:.2f}\n")
                        mes += 1
                    print("\n1. Se deseja sair do banco")
                    print("2. Se deseja voltar ao menu principal")
                    print("3. Se deseja retirar novamente")
                    opcion3 = int(input("\nQual é sua escolha: "))
                    if opcion3 == 1:
                        print("\nObrigado volte sempre :)")
                        contador3 = False
                        contador2 = False
                        contador = False
                    elif opcion3 == 2:
                        contador3 = False
                        contador2 = False
                    elif opcion3 == 3:
                        contador3 = True
                    else:
                        print("\nEscolha errada")
            elif opcion2 == 5:
                contador = True
                contador2 = False
                contador3 = False
            else:
                print("\nEscolha errada")


# Menu gerente

    elif opcion1 == 2:
        tentativas = 3
        entrar = False
        while entrar != True:
            senha2 = input("\nDigite a senha para acessar o modo gerente: ")
            if (senha == senha2) and (tentativas > 0):
                entrar = True
                contador2 = True
                while contador2 == True:
                    print("\n\nMenu Gerente: \n")
                    print("1. Cadastrar ou Trocar Nome do Cliente")
                    print("2. Corrigir Saldo do Cliente")
                    print("3. Consultar Status do Cliente")
                    print("4. Voltar ao Menu Principal")
        
                    opcion2 = int(input("\nQual é sua escolha: "))
            
                    if opcion2 == 1:
                        contador3 = True
                        while contador3 == True:
                            print(f"\nNome atual do cliente: {nome_cliente}")
                            novo_nome_cliente = input("\nQual vai ser o novo nome do cliente: ")
                            nome_cliente = novo_nome_cliente
                            print(f"\nNome atualizado do cliente: {nome_cliente}\n")
                            with open("dados.pkl", "wb") as arquivo:
                                pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)
                            print("\n1. Se deseja sair do banco")
                            print("2. Se deseja voltar ao menu principal")
                            print("3. Se deseja mudar o nome do cliente novamente")
                            opcion3 = int(input("\nQual é sua escolha: "))
                            if opcion3 == 1:
                                print("\nObrigado volte sempre :)")
                                contador3 = False
                                contador2 = False
                                contador = False
                            elif opcion3 == 2:
                                contador3 = False
                                contador2 = False
                            elif opcion3 == 3:
                                contador3 = True
                            else:
                                print("\nEscolha errada")
                    elif opcion2 == 2: 
                        contador3 = True
                        while contador3 == True:
                            print(f"\nSaldo atual do cliente {nome_cliente}: {saldo}")
                            novo_saldo = int(input(f"\nCorrigir saldo do cliente {nome_cliente}: "))
                            saldo = novo_saldo
                            print(f"\nSaldo atualizado do cliente {nome_cliente}: {saldo}\n")
                            with open("dados.pkl", "wb") as arquivo:
                                pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)
                            print("\n1. Se deseja sair do banco")
                            print("2. Se deseja voltar ao menu principal")
                            print("3. Se deseja mudar o saldo do cliente novamente")
                            opcion3 = int(input("\nQual é sua escolha: "))
                            if opcion3 == 1:
                                print("\nObrigado volte sempre :)")
                                contador3 = False
                                contador2 = False
                                contador = False
                            elif opcion3 == 2:
                                contador3 = False
                                contador2 = False
                            elif opcion3 == 3:
                                contador3 = True
                            else:
                                print("\nEscolha errada")
                    elif opcion2 == 3: 
                        contador3 = True
                        while contador3 == True:
                            print(f"\nO cliente {nome_cliente} tem : {saldo} um bom cliente sem duvida alguma")
                            print("\n1. Se deseja sair do banco")
                            print("2. Se deseja voltar ao menu principal")
                            print("3. Se deseja consultar o status do cliente novamente")
                            opcion3 = int(input("\nQual é sua escolha: "))
                            if opcion3 == 1:
                                print("\nObrigado volte sempre :)")
                                contador3 = False
                                contador2 = False
                                contador = False
                            elif opcion3 == 2:
                                contador3 = False
                                contador2 = False
                            elif opcion3 == 3:
                                contador3 = True
                            else:
                                print("\nEscolha errada")
                    elif opcion2 == 4: 
                        contador = True
                        contador2 = False
                        contador3 = False
                    else:
                        print("\nEscolha errada")

            elif tentativas == 1:
                break
            else:
                tentativas -= 1
                print(f"\nSenha errada tem {tentativas} tentativas mais") 

# Sair

    elif opcion1 == 3:
        print("\nObrigado volte sempre :)")
        with open("dados.pkl", "wb") as arquivo:
            pickle.dump({"nome": nome_cliente, "saldo": saldo}, arquivo)
        contador = False
    else:
        print("\nEscolha errada")

