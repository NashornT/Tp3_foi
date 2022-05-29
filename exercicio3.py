def concurso_fantasia():

    
    nomes = []
    notas= []
    
    for i in range(1,6):

        nome =  str(input(f'Informe o nome do {i}° participante: '))
        if (nome.isnumeric()):
            print(f'Valor inválido no {i}° nome')
            break
        
        nota = float(input(f'Informe a nota do {i}° participante: de 0 a 10 '))
        if (nota < 0 or nota > 10):
            print(f'Valor inválido na  {i}° nota')
            break
        else:
            nomes.append(nome)
            notas.append(nota)

    try:
        print(f'O(a) vencedor(a) foi {nomes[notas.index(max(notas))]} com nota {max(notas)}!')
    except:
        pass

concurso_fantasia()

