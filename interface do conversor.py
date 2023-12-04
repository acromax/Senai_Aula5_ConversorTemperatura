#Interface gráfica do conversor de temp

import PySimpleGUI as psg

import funcoesConversorTemperatura
from funcoesConversorTemperatura import celsius_para_fahrenheit

layout = [
              [psg.Text('Informe a temperatura em celsius: '), psg.InputText(key= 'valores')],
              [psg.Text('Fahrenheit -'), psg.Text( text= '', key= 'resultado')],
              [psg.Button('calcular'), psg.Button('limpar')],
        ]

janela = psg.Window('Conversor de temperatura', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'limpar':
        janela['valores'].update('')
        janela['resultado'].update('')
        janela['valores'].set_focus()
    else:
        valores = int(valores['valores'])
        janela['resultado'].update(funcoesConversorTemperatura.celsius_para_fahrenheit(valores))

janela.close()
