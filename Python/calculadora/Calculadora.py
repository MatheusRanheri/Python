def soma(a , b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "Erro!!!"
    return a / b

def calculadora():
    print("--------Menu-------")
    print(" [1] -- somar      ")
    print(" [2] -- subtrair   ")
    print(" [3] -- multiplicar")
    print(" [4] -- dividir    ")
    print("-------------------")
    
    calcular = input("Digite o numero para a operação")
    a = int(input("Informe o primeiro numero"))
    b = int(input("Informe o segundo numero"))
    
    if calcular == "1":
        resultado = soma(a,b)
        print(resultado)
    elif calcular == "2":
        resultado = subtrair(a,b)
        print(resultado)
    elif calcular == "3":
        resultado = multiplicar(a,b)
        print(resultado)
    elif calcular == "4":
        resultado = dividir(a,b)
        print(resultado)
    else:
        print("Esse número não está nas opções selecionaveis")

        if __name__=="__main__":
            calculadora()