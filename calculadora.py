from calc import Calc
lista =  ['x', '+', '-', '/','**','S']
x = 2
while True:
    print("+ | Soma")
    print("- | Subtração")
    print("/ | Divisao")
    print("x | Multiplicação")
    print("** | Exponemcição")
    print("S | Sair")
    
   
    op = input("Digite o operador")
    if op not in lista:
            print("Operador não esta listado ou voce digitou incorretamente")
            print("Digite novamente")
        
    if op in lista:
        try:
            num1 = float(input("Digite um numero"))
            num2 = float(input("Digite o segundo numero"))
            if op == '+':
                    print(f'A soma do {num1} + {num2} =', Calc.soma(num1, num2))
            if op == '-':
                    print(f'A soma do {num1} - {num2} =', Calc.sub(num1, num2))
            if op == '/':
                    print(f'A soma do {num1} / {num2} =', Calc.div(num1, num2))
            if op == 'x':
                    print(f'A soma do {num1} x {num2} =', Calc.mult(num1, num2))
            if op == '**':
                    print(f'A soma do {num1} + {num2} =', Calc.exp(num1, num2))
            else:
                break
        except ValueError:
            print("Digite um numero")
                



