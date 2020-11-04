#import doce
#from doce import "oque vai ser importado"
import math
#from math import (ctrl + backspace lista de comandos)
#Quando começar com from o comando pode se chamado diretamente

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
