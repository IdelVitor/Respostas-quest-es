palavra = input('Me diga uma palavra: ')

palavra_invertida = ""

for i in range(len(palavra) - 1, -1, -1):  
    palavra_invertida += palavra[i]  

print(f"A palavra invertida é: {palavra_invertida}")