mensagem_criptografada = ['7', '4', '-1', '8', '3', '-1', 
'5', '1', '-1']
codigo_letra = ''
palavra = ''

for letra in mensagem_criptografada:
    if letra == '-1':
        palavra += (chr(int(codigo_letra)))
        codigo_letra = ''        
    else:
        codigo_letra = codigo_letra + letra
print(palavra)