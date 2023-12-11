import PySimpleGUI as psg
def calcular_imposto(salario_bruto, num_dependentes):

    desc_dependentes = 189.59 * num_dependentes
    salario_base = salario_bruto - desc_dependentes

    if salario_base < 1903.98:
        aliquota = 0.0
        fx_desc = 0.0
        imposto_bruto = (salario_base * aliquota) - 0.0
    elif salario_base <= 2826.65:
        aliquota = 0.075
        fx_desc = 142.80
        imposto_bruto = (salario_base * aliquota) - 142.80
    elif salario_base <= 3751.05:
        aliquota = 0.15
        fx_desc = 354.80
        imposto_bruto = (salario_base * aliquota) - 354.80
    elif salario_base <= 4664.68:
        aliquota = 0.225
        fx_desc = 636.13
        imposto_bruto = (salario_base * aliquota) - 636.13
    else:
        aliquota = 0.275
        fx_desc = 869.36
        imposto_bruto = (salario_base * aliquota) - 869.36

    ir_devido = imposto_bruto
    salario_liquido = salario_bruto - ir_devido
    aliquota_efetiva = ir_devido / salario_bruto

    return {
        'salario_base': salario_base,
        'aliquota': aliquota,
        'ir_devido': ir_devido,
        'salario_liquido': salario_liquido,
        'aliquota_efetiva': aliquota_efetiva,
    }


psg.theme('reds')

layout = [
    [psg.Text('Informe o salário bruto: '), psg.Input(key='salario_bruto')],
    [psg.Text('Informe o número de dependentes: '), psg.Input(key='num_dependentes')],
    [psg.Button('Calcular'), psg.Button('Limpar'), psg.Button('Fechar', button_color=('white', 'black'))],
    [psg.Text('', size=(40, 5), key='output')],
]

janela = psg.Window('Calculadora de Imposto de Renda', layout)

while True:
    event, values = janela.read()

    if event == psg.WINDOW_CLOSED or event == 'Fechar':
        break
    elif event == 'Calcular':
        salario_bruto = float(values['salario_bruto'])
        num_dependentes = int(values['num_dependentes'])

        resultado = calcular_imposto(salario_bruto, num_dependentes)

        output_text = (
            f'Salário base: R${resultado['salario_base']:.2f}\n'
            f'Alíquota:  {resultado['aliquota'] * 100:.1f}%\n'
            f'IR Devido: R${resultado['ir_devido']:.2f}\n'
            f'Salário Líquido: R$ {resultado['salario_liquido']:.2f}\n'
            f'Alíquota Efetiva: {resultado['aliquota_efetiva'] * 100:.2f}%'
        )

        janela['output'].update(output_text)

    elif event == 'Limpar':
        janela['salario_bruto'].update('')
        janela['num_dependentes'].update('')
        janela['output'].update('')
        janela['salario_bruto'].set_focus()

janela.close()