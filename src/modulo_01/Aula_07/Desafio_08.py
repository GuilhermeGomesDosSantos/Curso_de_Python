
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('Uma distância em metros: '))
cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10
print('A media de {}metros corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}cm\n{:.0f}mm'.format(metros, km, hm, dam, cm, mm))
