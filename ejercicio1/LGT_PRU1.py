def calculo(numero):
    divisor = 0
    total   = 0
    div     = 0
    if numero > 1:
        if numero % 2 == 0:
            iterar = numero / 2
        else:
            iterar = (numero - 1) / 2

        for i in range(1, int(iterar) + 1):
            if numero % i == 0:
                aux = numero / i
                if aux != divisor:
                    divisor = aux
            
                if i == iterar:
                    div = int(divisor)
                else:
                    div = divisor
                    
                if  div != numero:
                    total = total + div       
        if total < numero:
            return 'Defectivo'
        else:
            if total > numero:
              return 'Abundante'
            else:
                if total < numero:
                  return 'Perfecto'
    
    else:
        return 'No tiene divisores propios'
		
		
j = 0
lista = []
for  j in range(0 , 5): 
    numero = int(input("Ingresa un numero: "))
    lista.append(numero)
   
for numero in lista:
    resultado = calculo(numero)
    print('El número ', numero, ' : ', resultado)
    