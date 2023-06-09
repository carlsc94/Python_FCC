
def arithmetic_arranger(lista:list,mostrar = False):
    Numerator = ''
    Denominator = ''
    Separator = ''
    Result = ''

    if len(lista) >5:
        return print('Error: too many problems')

    for element in lista:
        element = element.split()
        cadenaVacia = ''
        adicional = '    '
        separador = '-'

        try:
            if (element[1] == '+'):
                resultado = str(int(element[0])+ int(element[2]))
            elif(element[1] == '-'):
                resultado = str(int(element[0])- int(element[2]))
            else:
                return print("Error: Operator must be '+' or '-'.")
        except:
            return print("Error: Numbers must only contain digits.")

        maximo = max(len(element[0]),len(element[2]))

        
        

        if 4 >= len(element[0]) >= len(element[2]) :
            numerador = f"{cadenaVacia.ljust(2+maximo-len(element[0]))}{element[0]}"
            denominador = f"{element[1]}{cadenaVacia.ljust(1+maximo-len(element[2]))}{element[2]}"
            resultado = f"{cadenaVacia.ljust(2+maximo-len(resultado))}{resultado}"

        elif(4 >= len(element[2]) >= len(element[0])):
             numerador = f"{cadenaVacia.ljust(2+maximo-len(element[0]))}{element[0]}"
             denominador = f"{element[1]}{cadenaVacia.ljust(1+maximo-len(element[2]))}{element[2]}"
             resultado = f"{cadenaVacia.ljust(2+maximo-len(resultado))}{resultado}"
        else:
            return print("Error: Numbers cannot be more than four digits.")
        
        separador = separador.ljust(len(denominador),'-')

        if Denominator == '':
            Numerator = numerador
            Denominator = denominador
            Separator = separador
            Result = resultado
            
        else:
            Numerator = Numerator+adicional+numerador
            Denominator = Denominator+adicional+denominador
            Separator = Separator + adicional + separador
            Result = Result + adicional+resultado


    if mostrar:
        print(f"{Numerator}\n{Denominator}\n{Separator}\n{Result}")
    else:
        print(f"{Numerator}\n{Denominator}\n{Separator}")
        

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)