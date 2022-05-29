nomes = ['Gustavo','Romario','Vanessa','Alberto','Jose']
notas = [10,9,9.7,6,7.5]

vencedor = []
nome_vencedor = ''
maior_valor = ''


'''for i in dic:
    print(i)
    print(dic[i]) 
'''



''' if (maior_valor < dic[i]):
        maior_valor = dic[i] 
        nome_vencedor = i
    else:
        pass
'''

'''
    if (dic[i] not in vencedor):
        vencedor.append(dic[i])
        
    else:
        print('numero ja adicionado')
'''


#print(max(dic.values()))


print(max(notas))
print(nomes[notas.index(max(notas))])