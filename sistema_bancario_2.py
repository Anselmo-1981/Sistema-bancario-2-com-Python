import random
from datetime import datetime, timedelta




def abrir_conta():
    print("\t\t##################################################  Banco Monetizar  ##################################################\n")
    print("\t\t\tABERTURA DE CONTA CORRENTE")
    cpf = int(input("\t\t\tInforme agora o número completo do seu CPF sem pontos ou traços: "))
    cadastrar_usuario(cpf=cpf) ### PARAMETRO NECESSARIO CPF

def cadastrar_usuario(cpf): ### PARAMETRO NECESSARIO CPF
    print("\t\t\tPor favor, preencha agora seus dados cadastrais:")
    nome = input("\t\t\tInforme seu nome completo: ")
    data_nascimento = input("\t\t\tInforme sua data de nascimento no formato DD/MM/AAAA: ")
    logradouro = input("\t\t\tInforme seu endereço (rua/número): ")
    bairro = input("\t\t\tInforme o bairro: ")
    cidade = input("\t\t\tInforme a cidade: ")
    estado = input("\t\t\tInforme o estado(sigla): ")
    conta_corrente = random.randint(11111, 99999)
    saldo = 0.00
    conta_logada = False
    cliente_pf[cpf] = dict()
    cliente_pf_aux1[conta_corrente] = dict()
    cliente_pf[cpf].update({'cpf':cpf, 'nome':nome, 'data_nascimento':data_nascimento, 'logradouro':logradouro, 'bairro':bairro, 'cidade':cidade, 'estado':estado, 'saldo':saldo, 'conta_corrente':conta_corrente, 'extrato_valor_saque_deposito':valor_saque_deposito, 'extrato_tipo_movimentacao':tipo_movimentacao, 'extrato_data_movimentacao':data_movimentacao, 'num_saques':num_saques, 'op_saque':op_saque, 'conta_logada':conta_logada, 'saldo_extrato':saldo_extrato})
    cliente_pf_aux1[conta_corrente] = {'cpf':cpf}
    print("\t\t##################################################  Banco Monetizar  ##################################################")
    print(f"\n\t\t\tABERTURA DA CONTA EFETUADA COM SUCESSO!\n")
    print(f"\t\t\tDADOS DO CLIENTE:")
    print(f"\t\t\tAgência: 0001 / Conta Corrente {cliente_pf[cpf].get('conta_corrente')}-{dig}")
    print(f"\t\t\tNome: {cliente_pf[cpf].get('nome')} / CPF: {cliente_pf[cpf].get('cpf')} / Data de Nascimento: {cliente_pf[cpf].get('data_nascimento')}")
    print(f"\t\t\tEndereço: {cliente_pf[cpf].get('logradouro')} / Bairro: {cliente_pf[cpf].get('bairro')} / Cidade: {cliente_pf[cpf].get('cidade')} / Estado: {cliente_pf[cpf].get('estado')}")
    print(f"\t\t\tSaldo da conta: R$ {cliente_pf[cpf].get('saldo'):.2f}")




def acessar_conta_op1(cpf, conta_logada):
    if cpf == cliente_pf[cpf].get('cpf'):
        print("\t\t##################################################  Banco Monetizar  ##################################################")
        cliente_pf[cpf].update({'conta_logada': conta_logada})  ### ATUALIZA NO DICIONARIO O VALOR BOOLEANO P 'TRUE'
        print(f"\n\t\t\tBem-vindo {cliente_pf[cpf].get('nome')}, é um prazer ter você como cliente.")
        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")

def acessar_conta_op2(cpf, conta, conta_logada):
    if conta == cliente_pf[cpf].get('conta_corrente'):
        print("\t\t##################################################  Banco Monetizar  ##################################################")
        cliente_pf[cpf].update({'conta_logada': conta_logada})  ### ATUALIZA NO DICIONARIO O VALOR BOOLEANO P 'TRUE'
        print(f"\n\t\t\tBem-vindo {cliente_pf[cpf].get('nome')}, é um prazer ter você como cliente.")
        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")




def depositar(cpf, tipo, data):  # CUMPRE REQUISITO PASSAGEM DE ARGUMENTOS POSICIONAIS APENAS!
    print("\t\t##################################################  Banco Monetizar  ##################################################\n")
    lista_aux_valor_saque_deposito = cliente_pf[cpf].get('extrato_valor_saque_deposito')
    lista_aux_extrato_tipo_movimentacao = cliente_pf[cpf].get('extrato_tipo_movimentacao')
    lista_aux_saldo_extrato = cliente_pf[cpf].get('saldo_extrato')
    valor_saque_deposito = lista_aux_valor_saque_deposito
    tipo_movimentacao = lista_aux_extrato_tipo_movimentacao
    saldo_extrato = lista_aux_saldo_extrato
    aux_saldo = cliente_pf[cpf].get('saldo')
    aux_conta_logada = cliente_pf[cpf].get('conta_logada')
    valor = float(input("\t\t\tValor do depósito R$: "))
    if valor > 0 and aux_conta_logada == True: ## DEPÓSITO VALOR POSITIVO
        print(f"\t\t\tDepósito de R$ {valor:.2f} efetuado com sucesso.")
        valor_saque_deposito.append(valor)
        tipo_movimentacao.append(tipo)
        saldo = valor + aux_saldo
        saldo_extrato.append(saldo)
        data = data.strftime('%d/%m/%Y')
        data_movimentacao.append(data)
        cliente_pf[cpf].update({'extrato_valor_saque_deposito':valor_saque_deposito})
        cliente_pf[cpf].update({'extrato_tipo_movimentacao':tipo_movimentacao})
        cliente_pf[cpf].update({'saldo':saldo})
        cliente_pf[cpf].update({'extrato_data_movimentacao':data_movimentacao})
        cliente_pf[cpf].update({'saldo_extrato':saldo_extrato})
    elif valor <= 0 and aux_conta_logada == True: ## O SISTEMA NÃO ACEITA DEPÓSITOS DE VALORES NEGATIVOS
        print(f"\t\t\tDepósito não efetuado.")
        print(f"\t\t\tO sistema não recebe valores negativos. Tente outra vez.")
    else:
        pass




def sair_da_conta(cpf):
    print("\t\t##################################################  Banco Monetizar  ##################################################\n")
    conta_logada = False
    cliente_pf[cpf].update({'conta_logada':conta_logada})
    print(f"\t\t\tConta Logada: {cliente_pf[cpf].get('conta_logada')}")
    print(f"\t\t\tConta {cliente_pf[cpf].get('conta_corrente')}-{1} deslogada com sucesso.")
    print(f"\t\t\t{cliente_pf[cpf].get('nome')}, volte sempre!")
    print(f"\t\t\tO Banco monetizar agradece pela confiança.")




def extrato(cpf, n, saldo):
    print("\t\t##################################################  Banco Monetizar  ##################################################\n")
    print("\t\t\tExtrato bancário para simples conferência.\n")
    lista_aux_valor_saque_deposito = cliente_pf[cpf].get('extrato_valor_saque_deposito')
    lista_aux_extrato_tipo_movimentacao = cliente_pf[cpf].get('extrato_tipo_movimentacao')
    lista_aux_data_movimentacao = cliente_pf[cpf].get('extrato_data_movimentacao')
    lista_aux_saldo_extrato = cliente_pf[cpf].get('saldo_extrato')
    print(f"\t\t\t\tSaldo inicial R$ {saldo:.2f}.")
    while len(lista_aux_valor_saque_deposito) > n:
        print(f"\t\t\t\t{n+1}  Data {lista_aux_data_movimentacao[n]}      Tipo: {lista_aux_extrato_tipo_movimentacao[n]}      Valor R$ {lista_aux_valor_saque_deposito[n]:.2f}          Saldo R$ {lista_aux_saldo_extrato[n]:.2f}")
        n += 1
    aux_saldo = cliente_pf[cpf].get('saldo')
    print(f"\n\t\t\t\tSaldo atualizado R$ {aux_saldo:.2f}.")




def saque(tipo, data, cpf, data2):
    print(apresentacao_2, "\n")
    lista_aux_valor_saque_deposito = cliente_pf[cpf].get('extrato_valor_saque_deposito')
    lista_aux_extrato_tipo_movimentacao = cliente_pf[cpf].get('extrato_tipo_movimentacao')
    lista_aux_saldo_extrato = cliente_pf[cpf].get('saldo_extrato')
    valor_saque_deposito = lista_aux_valor_saque_deposito
    tipo_movimentacao = lista_aux_extrato_tipo_movimentacao
    saldo_extrato = lista_aux_saldo_extrato
    aux_saldo = cliente_pf[cpf].get('saldo')
    aux_num_saques = cliente_pf[cpf].get('num_saques')
    aux_op_saque = cliente_pf[cpf].get('op_saque')
    aux_conta_logada = cliente_pf[cpf].get('conta_logada')
    num_saques = aux_num_saques
    op_saque = aux_op_saque
    valor = float(input("\t\t\tValor do saque R$: "))
    if 0 <= valor <= 500 and valor <= aux_saldo and num_saques == 0 and aux_conta_logada == True:
        if num_saques == 0 and num_saques < 1 and op_saque == 1:
            print(f"\t\t\tSaque de R$ {valor:.2f} efetuado com sucesso.")
            print(f"\t\t\tVocê pode efetuar hoje, {data}, mais duas operações de até R$ 500,00.")
            valor_saque_deposito.append(valor)
            tipo_movimentacao.append(tipo)
            saldo = aux_saldo - valor
            saldo_extrato.append(saldo)
            data_movimentacao.append(data)
            num_saques += 1
            op_saque += 1
            cliente_pf[cpf].update({'extrato_valor_saque_deposito': valor_saque_deposito})
            cliente_pf[cpf].update({'extrato_tipo_movimentacao': tipo_movimentacao})
            cliente_pf[cpf].update({'saldo': saldo})
            cliente_pf[cpf].update({'extrato_data_movimentacao': data_movimentacao})
            cliente_pf[cpf].update({'saldo_extrato': saldo_extrato})
            cliente_pf[cpf].update({'num_saques':num_saques})
            cliente_pf[cpf].update({'op_saque':op_saque})
    elif 0 <= valor <= 500 and valor <= aux_saldo and num_saques == 1 and aux_conta_logada == True:
        if num_saques == 1 and num_saques < 2 and op_saque == 2:
            print(f"\t\t\tSaque de R$ {valor:.2f} efetuado com sucesso.")
            print(f"\t\t\tVocê pode efetuar hoje, {data}, mais uma operação de até R$ 500,00.")
            valor_saque_deposito.append(valor)
            tipo_movimentacao.append(tipo)
            saldo = aux_saldo - valor
            saldo_extrato.append(saldo)
            data_movimentacao.append(data)
            num_saques += 1
            op_saque += 1
            cliente_pf[cpf].update({'extrato_valor_saque_deposito': valor_saque_deposito})
            cliente_pf[cpf].update({'extrato_tipo_movimentacao': tipo_movimentacao})
            cliente_pf[cpf].update({'saldo': saldo})
            cliente_pf[cpf].update({'extrato_data_movimentacao': data_movimentacao})
            cliente_pf[cpf].update({'saldo_extrato': saldo_extrato})
            cliente_pf[cpf].update({'num_saques': num_saques})
            cliente_pf[cpf].update({'op_saque': op_saque})
    elif 0 <= valor <= 500 and valor <= aux_saldo and num_saques == 2 and aux_conta_logada == True:
        if num_saques == 2 and num_saques < 3 and op_saque == 3:
            print(f"\t\t\tSaque de R$ {valor:.2f} efetuado com sucesso.")
            print(f"\t\t\tVocê não pode efetuar mais saques hoje. Seu limite será renovado em {data2}.")
            valor_saque_deposito.append(valor)
            tipo_movimentacao.append(tipo)
            saldo = aux_saldo - valor
            saldo_extrato.append(saldo)
            data_movimentacao.append(data)
            num_saques += 1
            op_saque += 1
            cliente_pf[cpf].update({'extrato_valor_saque_deposito': valor_saque_deposito})
            cliente_pf[cpf].update({'extrato_tipo_movimentacao': tipo_movimentacao})
            cliente_pf[cpf].update({'saldo': saldo})
            cliente_pf[cpf].update({'extrato_data_movimentacao': data_movimentacao})
            cliente_pf[cpf].update({'saldo_extrato': saldo_extrato})
            cliente_pf[cpf].update({'num_saques': num_saques})
            cliente_pf[cpf].update({'op_saque': op_saque})
    elif num_saques == 3 and op_saque == 4 and aux_conta_logada == True:
            print(f"\t\t\tO limite de saques diários foi atingido.")
            print(f"\t\t\tVocê não pode efetuar mais saques hoje. Seu limite será renovado em {data2}.")
    elif valor > aux_saldo:
            print(f"\t\t\tSaque não efetuado.")
            print(f"\t\t\tSaldo Insuficiente.")
    elif valor > 0:
            print(f"\t\t\tSaque não efetuado.")
            print(f"\t\t\tNão é permitido o saque de valores negativos.")
    else:
        pass




apresentacao_1 = """\t\t##################################################  Banco Monetizar  ##################################################

\t\t\tBem-vindo ao Banco Monetizar, é um prazer tê-lo como cliente.

\t\t\tDigite:
\t\t\t[1] ABRIR NOVA CONTA                          
\t\t\t[2] ACESSAR UMA CONTA EXISTENTE (PARA ENTRAR NAS OPÇÕES: SAQUE; DEPÓSITO, E EXTRATO.)                
\t\t\t[3] SAIR DO SISTEMA"""

apresentacao_2 = "\t\t##################################################  Banco Monetizar  ##################################################"
cliente_pf = dict()
cliente_pf_aux1 = dict()
cliente_pf_aux2 = dict()
dig = 1
valor_saque_deposito = []
tipo_movimentacao = []
data_movimentacao = []
saldo_extrato = []
n = 0
num_saques = 0
op_saque = 1
saldo = 0.00

system_on = True
while system_on == True:

    print("\n\n", apresentacao_1)
    opcao = int(input("\t\t\tDigite agora a opção escolhida: "))

    while (opcao == 1) or (opcao == 2) or (opcao == 3):

        if opcao == 1:
            abrir_conta()
            print(apresentacao_1)
            opcao = int(input("\t\t\tDigite agora a opção escolhida: "))

        elif opcao == 2:
            print("\t\t##################################################  Banco Monetizar  ##################################################\n")
            print("\t\t\tDigite:")
            print("\t\t\t[1] Para acessar o Banco Monetizar pelo número de seu CPF;")
            print("\t\t\t[2] Para acessar o Banco Monetizar pelo número de sua Conta Corrente.")
            op = int(input("\t\t\tDigite agora a opção escolhida: "))
            ### ACESSAR A CONTA PELO CPF
            if op == 1:
                cpf = int(input("\t\t\tInforme o número completo do seu CPF sem pontos ou traços: "))
                login = True
                conta_logada = login
                acessar_conta_op1(cpf, conta_logada=conta_logada)
                print(f"\t\t\tSaldo disponível em conta corrente: R$ {cliente_pf[cpf].get('saldo'):.2f}.")
                print(f"\t\t##################################################  Banco Monetizar  ##################################################\n")
                print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                print(f"\t\t\tDigite:")
                print(f"\t\t\t[1] SAQUE")
                print(f"\t\t\t[2] DEPÓSITO")
                print(f"\t\t\t[3] EXTRATO")
                print(f"\t\t\t[4] SAIR")
                op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                while (op_1 == 1) or (op_1 == 2) or (op_1 == 3) or (op_1 == 4):
                    if op_1 == 2:
                        registro_1 = "  Depósito "
                        registro_2 = datetime.now()
                        depositar(cpf, registro_1, registro_2)  ## DEPOSITO RECEBE ARGUMENTOS SOMENTE POR POSICAO
                        print(f"\t\t\tSaldo disponível em conta corrente R$ {cliente_pf[cpf].get('saldo'):.2f}. ")
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] SAQUE;")
                        print("\t\t\t[2] DEPÓSITO;")
                        print("\t\t\t[3] EXTRATO;")
                        print("\t\t\t[4] SAIR.")
                        op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                    elif op_1 == 3:
                        extrato(cpf, saldo=saldo, n=n)  ## ARGUMENTO POSICIONAL CPF, NOMEADO 'N'
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] SAQUE;")
                        print("\t\t\t[2] DEPÓSITO;")
                        print("\t\t\t[3] EXTRATO;")
                        print("\t\t\t[4] SAIR.")
                        op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                    elif op_1 == 1:
                        registro_1 = "   Saque   "
                        registro_2 = datetime.now()
                        registro_2 = registro_2.strftime('%d/%m/%Y')
                        registro_3 = datetime.now() + timedelta(days=1)
                        registro_3 = registro_3.strftime('%d/%m/%Y')
                        saque(data=registro_2, tipo=registro_1, data2=registro_3, cpf=cpf)  ## ARGUMENTOS NOMEADOS
                        print(f"\t\t\tSaldo disponível em conta corrente R$ {cliente_pf[cpf].get('saldo'):.2f}.")
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] SAQUE;")
                        print("\t\t\t[2] DEPÓSITO;")
                        print("\t\t\t[3] EXTRATO;")
                        print("\t\t\t[4] SAIR.")
                        op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                    elif op_1 == 4:
                        sair_da_conta(cpf)
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print("\t\t\tBem-vindo ao Banco Monetizar, é um prazer tê-lo como cliente.\n")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] ABRIR NOVA CONTA")
                        print("\t\t\t[2] ACESSAR UMA CONTA EXISTENTE")
                        print("\t\t\t[3] SAIR")
                        break
                opcao = int(input("\t\t\tDigite agora a opção escolhida: "))

            ### ACESSAR A CONTA PELO PROPRIO NUMERO
            elif op == 2:
                conta = int(input("\t\t\tInforme o número de sua conta corrente sem o dígito: "))
                conta_corrente = conta
                cpf = cliente_pf_aux1[conta_corrente].get('cpf')
                login = True
                conta_logada = login
                acessar_conta_op2(cpf, conta=conta, conta_logada=conta_logada)
                print(f"\t\t\tSaldo disponível em conta corrente: R$ {cliente_pf[cpf].get('saldo'):.2f}.")
                print(f"\t\t##################################################  Banco Monetizar  ##################################################\n")
                print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                print(f"\t\t\tDigite:")
                print(f"\t\t\t[1] SAQUE")
                print(f"\t\t\t[2] DEPÓSITO")
                print(f"\t\t\t[3] EXTRATO")
                print(f"\t\t\t[4] SAIR")
                op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                while op_1 == 1 or op_1 == 2 or op_1 == 3 or op_1 == 4:
                    if op_1 == 2:
                        registro_1 = "  Depósito "
                        registro_2 = datetime.now()
                        depositar(cpf, registro_1, registro_2)  ## DEPOSITO RECEBE ARGUMENTOS SOMENTE POR POSICAO
                        print(f"\t\t\tSaldo disponível em conta corrente R$ {cliente_pf[cpf].get('saldo'):.2f}. ")
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] SAQUE;")
                        print("\t\t\t[2] DEPÓSITO;")
                        print("\t\t\t[3] EXTRATO;")
                        print("\t\t\t[4] SAIR.")
                        op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                    elif op_1 == 3:
                        extrato(cpf, saldo=saldo, n=n)  ## ARGUMENTO POSICIONAL CPF, NOMEADO 'N'
                        print(f"\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] SAQUE;")
                        print("\t\t\t[2] DEPÓSITO;")
                        print("\t\t\t[3] EXTRATO;")
                        print("\t\t\t[4] SAIR.")
                        op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                    elif op_1 == 1:
                        registro_1 = "   Saque   "
                        registro_2 = datetime.now()
                        registro_2 = registro_2.strftime('%d/%m/%Y')
                        registro_3 = datetime.now() + timedelta(days=1)
                        registro_3 = registro_3.strftime('%d/%m/%Y')
                        saque(data=registro_2, tipo=registro_1, data2=registro_3, cpf=cpf)  ## ARGUMENTOS NOMEADOS
                        print(f"\t\t\tSaldo disponível em conta corrente R$ {cliente_pf[cpf].get('saldo'):.2f}.")
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print(f"\t\t\tAgência: 0001 / Conta Corrente: {cliente_pf[cpf].get('conta_corrente')}-{1} / Conta Logada: {cliente_pf[cpf].get('conta_logada')}")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] SAQUE;")
                        print("\t\t\t[2] DEPÓSITO;")
                        print("\t\t\t[3] EXTRATO;")
                        print("\t\t\t[4] SAIR.")
                        op_1 = int(input("\t\t\tDigite agora a opção escolhida: "))
                    elif op_1 == 4:
                        sair_da_conta(cpf)
                        print("\t\t##################################################  Banco Monetizar  ##################################################\n")
                        print("\t\t\tBem-vindo ao Banco Monetizar, é um prazer tê-lo como cliente.\n")
                        print("\t\t\tDigite:")
                        print("\t\t\t[1] ABRIR NOVA CONTA")
                        print("\t\t\t[2] ACESSAR UMA CONTA EXISTENTE")
                        print("\t\t\t[3] SAIR")
                        break
                opcao = int(input("\t\t\tDigite agora a opção escolhida: "))


        elif opcao == 3:
            print("\t\t\tFinalizando o sistema...")
            system_on = False
            break
        else:
            pass
print("\t\t\tSistema encerrado.")