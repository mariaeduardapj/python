s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    if s1==s2==s3:
        print('\033[34mÉ possível formar um \033[1;34mtriângulo equilatero\033[34m com esses segmentos.\033[m')
    elif r1!=r2!=r3!=r1:
        print('\033[34mÉ possível formar um \033[1;34mtriangulo escaleno\033[34m com esses segmentos.\033[m')
    else:
        print('\033[34mÉ possível formar um \033[1;34mtriângulo   isósceles\033[34m com esses segmentos.\033[m')
else:
    print('\033[31mNão é possível formar um triângulo com esses segmentos.\033[m')