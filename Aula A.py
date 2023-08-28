"""
Sets (Conjuntos) - valores que não se repetem

add (adicionar),
update(atualizar)
clear e discard

Union "|" (Une)
interserction "&" (Todos os elementos presente (iguais) nos dois sets)
Difference "-" (Elementos diferentes apenas no set da esquerda)
symmetric_difference "^" (Elementos diferentes que estao nos dois sets, mas não em ambos)
"""
SET_1 = set()
SET_2 = {1, 2, 3, 4, 5, 6}

print('Usando "add" ')
print("Antes:", SET_2)
SET_2.add(7)
SET_2.add(('A', 'B', 'C'))
print("Depois", SET_2)
# SET_2.add(['A', 'B', 'C'])  Não add list
# SET_2.add({'A': 'a', 'B': 'b', 'C': 'b'}) Não add dict

print("\nUsando update")
SET_1.update(['D', 'E', 'F', 'G'], {10, 11, 12, 13})  # Atualiza e add sem lista ou set
SET_1.update('Python')  # atualiza separando as letras!
print(SET_1)
print(SET_2)
# print(SET_1[1]) Não pode acessar suas indices!

print("\nPode remover usando clear ou discard")
SET_1.clear()  # Limpa todos set
SET_2.discard(2)  # remove o valor especifico
print(SET_1)
print(SET_2)

print('\nComo os valores não se repetem, pode usar o set para eleminar valores repetidos')
List_1 = ['Everton', 'Everton', 'Everton', 'Everton', 'Maria', 'Maria']
print(List_1)
List_1 = set(List_1)  # Test cast
List_1 = list(List_1)
print(List_1)


print('\nUsando union, interserction, difference, symmtric difference')
SET_2 = {1, 2, 3, 4, 5, 6}
SET_3 = {1, 2, 3, 4, 5, 7}
print(SET_2)
print(SET_3)
print('Juntos "|"', SET_2 | SET_3)  # Juntos os elementos, porem exclui os repetidos
print('Elementos presentes "&"', SET_2 & SET_3)  # Todos elementos presentes(iguais) nos dois sets
print('Elementos diferentes da esquerda "-"', SET_2 - SET_3)  # So aparece elemento diferente no set da esquerda
print('Elementos diferentes dos set "^"', SET_2 ^ SET_3)  # Só aparece elemento diferentes dos dois sets

print('\nComparações logicas')
List_2 = ['Everton', 'Maria', 'João']
List_3 = ['Everton', 'Everton', 'Everton', 'Everton', 'Maria', 'Maria', 'Maria', 'João']
print(List_2)
print(List_3)
if set(List_2) == set(List_3):
    print('Fazendo um conversão na lis para set, se tornam iguais!')
