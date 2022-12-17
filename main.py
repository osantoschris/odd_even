numero = int(input('Digite o número: '))

def par_impar(numero):
    resto = numero % 2
    if resto == 0:
        return True
    else:
        return False

if par_impar(numero) == True:
    print('O número é par!')
else:
    print('O número é ímpar!')