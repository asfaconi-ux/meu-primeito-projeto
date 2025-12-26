print("=== Calculadora Simples ===")

while True:
    print("\nEscolha uma operação:")
    print("1) Adição (+)")
    print("2) Subtração (-)")
    print("3) Multiplicação (*)")
    print("4) Divisão (/)")
    print("5) Potência (**)")
    print("0) Sair")

    opcao = input("Digite a opção: ")

    if opcao == "0":
        print("Saindo... até mais!")
        break

    # Recebe pelo menos 2 números (requisito)
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    # Condicional (requisito) + 4+ operações (requisito)
    if opcao == "1":
        resultado = n1 + n2
        print(f"Resultado: {n1} + {n2} = {resultado}")

    elif opcao == "2":
        resultado = n1 - n2
        print(f"Resultado: {n1} - {n2} = {resultado}")

    elif opcao == "3":
        resultado = n1 * n2
        print(f"Resultado: {n1} * {n2} = {resultado}")

    elif opcao == "4":
        if n2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            resultado = n1 / n2
            print(f"Resultado: {n1} / {n2} = {resultado}")

    elif opcao == "5":
        resultado = n1 ** n2
        print(f"Resultado: {n1} ** {n2} = {resultado}")

    else:
        print("Opção inválida. Tente novamente.")
