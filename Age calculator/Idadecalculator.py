import datetime
nome = input('Insira se nome: ')
print('Olá ' + nome)

while True:
    
    data_nascimento = input('Por favor, digite a sua data de nascimento (DD/MM/AAAA): ')

    try:
     
        nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
       
        break
    except ValueError:
       
        print('Data de nascimento inválida. Por favor, tente novamente.')


hoje = datetime.datetime.now()


idade = hoje.year - nascimento.year


if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
    idade -= 1


print(f'A idade do {nome} é {idade} anos.')
print('Obrigado por usar nossos serviços, Volte sempre')
