# faça um programa que leia o ano de nascimento de um jovem e informe de acordo sua idade
# se ele ainda vai se alsitar ao serviço militar obrigatorio
# se é a hora de se alistar
# ou se já passou o tempo do alistamento
# caso ele ainda não tenha 18 anos avisar quanto tempo falta para ele se alistar
from datetime import date

print('Bora calcular quanto tempo falta para seu alistamento obrigatorio!!')
anoNascimento = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - anoNascimento
faltaIdade = 18 - idade
saldo = int
print('Quem Nasceu em {} tem {} anos em {}'.format(anoNascimento, idade, date.today().year))
if idade < 18:
    saldo = 18 - idade
    print('Você deve realizar o processo daqui {} anos'.format(faltaIdade))
    ano = date.today().year + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Você já pode realizar o processo de inscrição, procure alistamento militar até julho ')
else:
    saldo = idade - 18
    print('Você já devia ter se alistado há {} anos,'.format(saldo))
    print('Caso não tenha se alistado procure a junta militar proxima da sua casa')
    ano = date.today().year - saldo
    print('Seu alistamento foi em {}'.format(ano))
