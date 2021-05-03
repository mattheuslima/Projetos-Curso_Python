def calc_terreno(l,c):
    area=round(l*c,2)
    print(f'\nA área do terreno é {area}m².')


print("Controle de terrenos")
print("="*20)
calc_terreno(float(input("Qual a largura do terreno? ")),float(input("Qual o comprimento do terreno? ")))