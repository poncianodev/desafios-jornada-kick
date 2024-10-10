# Crie uma função chamada eh_par que recebe um número como parâmetro e retorna True se o número for par e False se for ímpar.

def eh_par(num):
  if num % 2 == 0:
    return "par"
  else:
    return "impar"
  
print(eh_par(3))