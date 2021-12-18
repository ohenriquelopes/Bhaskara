def Bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("\nValor de x1: {}".format(x1))
    print("\nValor de x2: {}".format(x2))

if __name__ == '__main__':
    while True:
        print("Calculando as raizes de uma equação de 2 grau\n")

        a = float(input("Digite um valor para A: "))
        b = float(input("Digite um valor para B: "))
        c = float(input("Digite um valor para C: "))

        Bhaskara(a, b, c)

        repeat = input("\nDigite n para sair ou aperte Enter para um novo calculo: \n")
        if (repeat == 'n'):
            break