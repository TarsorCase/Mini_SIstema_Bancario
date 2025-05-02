# Sistema Bancário com Segurança 
# Cibersegurança - 1ºP - Turma U - PUCPR
# Gustavo Batista de Souza 

import pickle
senhaGerente = "Lulaladrãorouboumeucoração"

#Preciso que rode o sistema a partir de informaçoes
try:
    with open("dados.pkl", "rb") as informacoes:
        SistemaBanco = pickle.load(informacoes)  # Carrega o conteúdo serializado do arquivo
except FileNotFoundError:  # Caso o arquivo não exista
    SistemaBanco = {}

#MENU INICIAL - Mostra as opções disponíveis para oS usuários

print("--------------CYBERVAULT------------\n")
print("----Bem-Vindo ao Sistema Bancário---")
print("----------Escolha uma opção---------\n")
print("╔════════════════════════════════════╗")
print("║  ┌──────────────────────────────┐  ║")
print("║  │      C Y B E R V O U L T     │  ║")
print("║  │  Secure Digital Vault CLI    │  ║")
print("║  └──────────────────────────────┘  ║")
print("╚════════════════════════════════════╝\n\n")
print("1. Acessar como Cliente do CyberVault")
print("2. Acessar como Gerente do CyberVault")
print("3. Sair do Sistema\n")

opcao = input("Escolha uma opcao de 1 a 3: \n")
while opcao != "3":
    if opcao == "1":
        #MODO CLEINTE - MENU
        print("Menu Cliente:\n")
        print("1. Consultar o saldo da conta")
        print("2. Depositar")
        print("3. Sacar/Pix")
        print("4. Simular Rendimento\n" \
        "     OBS: Apresentar mês a mês os proximos doze menes com taxa de (1.19%) ao mês")
        print("5. Voltar ao menu inicial\n\n")

        opcao = input("Escolha uma opcao a cima: \n")

        if opcao == "1":
            saldo_conta = 53092.89
            print(f"O saldo da sua conta é de: {saldo_conta} reais\n")

        elif opcao =="2":
            valor_deposito = float(input("Qual valor você quer depositar em sua conta?: "))
            if valor_deposito > 0: # aqui fala se o valor for maior que zero, devera somar com a soma
                saldo_conta = saldo_conta + valor_deposito
                print(f"Deposito realizado!")
                print(f"Saldo atual:R$ {saldo_conta}")
            else:
                print("O valor não pode ser menor que zero. Tente novamente por favor")

        elif opcao == "3":
            saque_pix = float(input("Digite sacada ou enviado via PIX: R$ "))
            if saque_pix > 0 and saque_pix <= saldo_conta:
                saldo_conta = saldo_conta - saque_pix 
                print(f"Saque/Transação feita!\n \
                      Saldo atual:R$ {saldo_conta}")
            else: 
                print("Valor incorreto")

        elif opcao == "4": #simulação de rendimento de 1.19%/12m
            saldo_demo = float(inut("Digite o valor para simulação: "))
            juros = 1.19 / 100
            rendime = saldo_demo

            print("RESULTADO DA SUA SIMULÇÃO: \n")
            for mes in range(1,13):
                rendime = rendime * (1 + juros) #EXEMPLO: rendime= 1000 . (1 + 1.19) = rendime = 1000 . 2.19 = 2190
                print("Mes", mes, ": R$", round(rendime, 2))

        elif opcao == "5": # nessa opção o usuario volta ao menu inicial
            pass # Serve para indicar que um bloco de código está propositalmente vazio, evitando erro de sintaxe.

        else:
            print("Opção invalida! Tente novamente.")
        break

#MODO GERENTE
    elif opcao == "2":
        print("Confirmação de identidade necessaria\n" \
"    Digite sua senha de Gerente.     \n" \
"     OBS: Somente 3 tentativas          ")
        
        tentativas = 0
        while tentativas < 3: #aqui limita a quantidade de tentativas
            senhaGerente = input("Senha do Gerente: ")
            if senhaGerente == senhaGerente:
                print("Acesso concedido ao MENU DO GERENTE.") 
                break
            else: 
                tentativas = tentativas + 1 
                print("Senha Invalida! - ", tentativas," de 3")
            if tentativas == 3:
                print("Você excedeu a quantidade de tentativas. Acesso Bloqueado!")

#Se as informações do cliente ainda não existir...serão criadas aqui

                nome_cliente = ""
                cliente_saldo = 50000.00

                opcao_gerente = ""

                while opcao_gerente != "5":
                    print("\nMenu Gerente:")
                    print("1. Cadastrar ou Trocar Nome do Cliente")
                    print("2. Corrigir Saldo do Cliente")
                    print("3. Consultar Status do Cliente")
                    print("5. Voltar ao Menu Principal\n")

                    opcao_gerente = input("Escolha uma opção: \n")

                    if opcao_gerente == "1":
                        nome_cliente = input("Digite o nome do cliente: ")
                        print("O Nome do cliente foi atualizado e salvo!")

                    elif opcao_gerente == "2":
                        saldo_atualiz =  float(input("Digite o novo saldo para seu cliente: "))
                        saldo_conta = saldo_atualiz
                        print("Saldo Atualizado")

                    elif opcao_gerente == "3":
                        if nome_cliente != "":
                            print("Esse é o Status Atual do Cliente: \n")
                            print("Nome", nome_cliente)
                            print("Saldo Atual: R$", round(saldo_conta))
                        else:
                            print("Cliente inexistente!")
                break #sai do loop 
            else:
                tentativas = tentativas + 1
                print("Senha incorreta. Tentativa", tentativas, "de 3.")

        if tentativas == 3:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")

#MODO DE SAIDA
    elif opcao == "3":
        confirmação = input("Deseja mesmo sair do sistema? [S/N]")
        if confirmação == "S" or confirmação == "s":
            print("Saindo do Sistema - CyberVoult\n \
              Obrigado! Volte Sempre.")
        break
    else:
        print("Você retornou ao MENU INICIAL")
        opcao = "0"
        
