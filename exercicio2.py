def verificador_idade():
    try:
        idade = input('Informe a idade: ')

        if(idade.isalpha()):
            print('Valor Inválido !!')
            exit
        else:
            idade = int(idade)

            if (idade < 0):
                print('Valor Inválido')
                exit
            else:
                if (idade >= 18 and idade <70 ):
                    print('Tem obrigação de votar.')
                elif (idade >= 16 and idade < 18 or idade >= 70 ):
                    print('Não tem obrigação de votar.')
                elif (idade > 70):
                    print('Não tem obrigação de votar.')
                else:
                    print('Não tem direito a voto')
    except:
        print('Valor Inválido !!')


verificador_idade()
