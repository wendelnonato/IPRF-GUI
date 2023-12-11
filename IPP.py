# Sistema para recolhimento de IR com base no salário
while True:
    print('\n\t\t\t -- Calculadora de IPRF MENSAL --')

    # Entradas
    salariobt = float(input('Informe o salário Bruto: '))
    dependentes = int(input('Informe o número de dependentes: '))

    # Processamento
    descontodp = dependentes * 189.59
    salario_base = salariobt - descontodp

    if salario_base < 1903.98:
        aliquota = 0.0
        desconto = 0.0
    elif salario_base <= 2826.65:
        aliquota = 0.075
        desconto = 142.8
    elif salario_base <= 3751.05:
        aliquota = 0.15
        desconto = 354.8
    elif salario_base <= 4664.8:
        aliquota = 0.225
        desconto = 636.13
    else:
        aliquota = 0.275
        desconto = 869.36

    impostobt = salario_base * aliquota
    irdevido = impostobt - desconto
    salariolq = salariobt - irdevido
    aliquotaef = irdevido / salariobt

    print('\n\t\t\t -- Imposto de Renda --')
    print
    print(f'Salario Bruto:{salariobt}')
    print(f'Numero de dependentes:{dependentes}')

    print(f'\nSalario base:{salario_base}')
    print(f'Aliquiota:{aliquota}')
    print(f'IR Devido:'), print(round(irdevido, 3))
    print(f'Salario liquido:{salariolq}')
    print(f'Alíquiota Efetiva:'), print(round(aliquotaef, 3))
    print('-'*70)
    print('\n\n\t\tDeseja Calular outro Imposto de Renda?')
    print('\nCaso sim digite:(S), Caso deseja sair digite (N):')
    op = input('(S/N):')
    if op.lower() == 's':
        print('Carregando!')
        pass
    elif op.lower() == 'n':
        print('\nObrigado Ate a proxima consulta!')
        break
    else:
        print('Informação invalida!!')
        break