# OPERADORES ARITMÉTICOS:   ORDEM DE PRECEDÊNCIA:
# [ + ] Adição              1° |()| Parenteses
# [ - ] Subtração           2° |**| Potência
# [ * ] Multiplicação       3° |*, /, //, %|
# [ / ] Divisão             4° |+, -| Adição e Subtração
# [ ** ] Potência
# [ // ] Divisão Inteira
# [  % ] Resto de Divisão

# DESAFIOS:

# Sucessor e antecessor do numero:
n1 = int(input('Digite um número: '))
s1 = n1 + 1
a1 = n1 - 1
print('O número {} tem seu sucessor {} e antecessor {} '.format(n1,s1,a1))