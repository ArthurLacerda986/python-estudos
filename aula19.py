primeiro_valor = input('Digite Um valor: ')
segundo_valor = input('Digite Um valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} o primeiro valor é maior do que o segundo {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor} o primeiro valor é equivalente ao segundo valor {segundo_valor}')
else:
    print(f'{segundo_valor} o segundo valor é maior do que o primeiro {primeiro_valor}')