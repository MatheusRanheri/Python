def soma(a , b):
    return a + b;

def subtrair(a,b):
    return a - b;

def multiplicar(a,b):
    return a * b;

def dividir(a,b):
    return a / b;

def calculadora():
    print("--------Menu-------");
    print(" [1] -- somar      ");
    print(" [2] -- subtrair   ");
    print(" [3] -- multiplicar");
    print(" [4] -- dividir    ");
    print("-------------------");
    
    calcular = input('Digite o numero para a operação');
    a = input('Informe o primeiro numero');
    b = input('Informe o segundo numero');
    
    if calcular == "1":
        resultado = soma(a,b);
        print(resultado);
    elif calcular == "2":
        resultado = subtrair(a,b);
        print(resultado);
    elif calcular == "3":
        resultado = multiplicar(a,b);
        print(resultado);
    elif calcular == "4":
        resultado = dividir(a,b);
        print(resultado);

    