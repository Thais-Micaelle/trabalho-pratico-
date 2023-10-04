altura = float(input ("informe o valor da altura: "))
peso =float(input("informe o peso"))

imc = peso/(altura*altura)

print("IMC: ",round(imc, 2)) 

if imc < 18.5:
    print("abaixo do peso")       
elif imc < 24.9:
    print("peso normal")      
elif imc <29.9:
    print("sobrepeso")
else:
    print("obeso")
                
            
                