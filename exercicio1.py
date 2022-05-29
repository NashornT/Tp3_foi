def divisor_de_contas():
    try:
        valor = input('Informe o valor total do consumo: R$ ')
        tot_pessoas = input('Informe o total de pessoas: ')
        percentual = input('Informe o percentual do serviço, entre 0 e 100: ')


        
        if (valor.isalpha() or tot_pessoas.isalpha() or percentual.isalpha()):
            print('Valor inválido !!')
            exit     
        else:
            valor = float(valor)
            tot_pessoas = int(tot_pessoas)
            percentual = int(percentual)
            valor_taxa = valor + percentual
            valor_taxa = str(valor_taxa).replace('.',',')
        

            print(f'O valor total da conta foi {valor}')
            print(f'Adicionando percentual de serviço de {percentual}')
            print(f'O valor total da conta com a taxa de serviço sera de: R$ {valor_taxa}')

            if (tot_pessoas < 0):
                print('Numéro de pessoas invalido')
            elif (0 > percentual and percentual > 100):
                print('O percentual está fora do intervalo sugerido')
            else:
                valor_final = ((valor+percentual)/tot_pessoas)
                valor_final = str(valor_final).replace('.',',')
                print(f'Dividindo a conta para {tot_pessoas} pessoa(s), cada pessoa deverá pagar  R$ {valor_final}')
    except:
        print('Valor inválido !!')
        

divisor_de_contas()