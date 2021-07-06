import keyboard
from time import sleep
from dicionarioexames import codigos
from dicionariopreços import precos

linhas = []
alpha = []
omega = []

with open("exames.txt", "rt") as listaexames:  # lê o arquivo exames.txt e adiciona os exames na lista linhas
    for linha in listaexames:
        linhas.append(linha.lstrip('  1234567890 - ').rstrip(' \n'))

for w in linhas:  # adiciona os códigos correspondentes aos exames à lista alpha
    alpha.append(codigos[w])

print([linhas])

sleep(3)

for c in range(0, len(alpha), 1):  # digita os códigos no formulário do sistema Vivver
    if c == 0:
        keyboard.write(alpha[c], 'tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('up')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('enter')
        sleep(0.4)
    else:
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.write(alpha[c])
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('tab')
        keyboard.press_and_release('up')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('shift+tab')
        keyboard.press_and_release('enter')
        sleep(0.4)

for q in alpha:  # adiciona os preços dos exames à lista omega
    omega.append(precos[q])

total = sum(omega)

omega = [float(i) for i in omega]
print('=-' * 50)
print(f"{'FATURA DOS EXAMES':^100}")
print('=-' * 50)
for r in range(len(linhas)):  # imprime a fatura dos exames e o valor do total no console
    print(f'{r + 1} - R$ {omega[r]:.2f}......{linhas[r]} ----- ({alpha[r]})')
print(f'R$ {total:.2f}......TOTAL')
print('=-' * 50)
