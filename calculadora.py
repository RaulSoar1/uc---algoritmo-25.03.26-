def calculadora():
    print("Calculadora iniciada")

calculadora()

def calculadora(a, b, operacao):
    if operacao == "+":
        print(a + b)
    elif operacao == "-":
        print(a - b)
    elif operacao == "*":
        print(a * b)
    elif operacao == "/":
        print(a / b)

calculadora(10, 5, "+")

def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Erro: divisão por zero"
        return a / b

resultado = calculadora(10, 5, "*")
print(resultado)

def calculadora():
    while True:
        print("\n=== Calculadora ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Saindo...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        try:
            a = float(input("Digite o primeiro valor: "))
            b = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == "1":
            print("Resultado:", a + b)
        elif opcao == "2":
            print("Resultado:", a - b)
        elif opcao == "3":
            print("Resultado:", a * b)
        elif opcao == "4":
            if b == 0:
                print("Erro: divisão por zero!")
            else:
                print("Resultado:", a / b)

calculadora()