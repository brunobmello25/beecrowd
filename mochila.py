def dp(pesos, valores, peso_restante):
    if len(pesos) == 1:
        if peso_restante >= pesos[0]:
            return valores[0]
        else:
            return 0

    last_index = len(pesos) - 1

    if peso_restante >= pesos[last_index]:
        return max(
            valores[last_index]
            + dp(pesos[:-1], valores[:-1], peso_restante - pesos[last_index]),
            dp(pesos[:-1], valores[:-1], peso_restante),
        )
    else:
        return dp(pesos[:-1], valores[:-1], peso_restante)


def main():
    tests = int(input())

    for t in range(tests):
        n_itens = int(input())

        pesos = []
        valores = []

        for i in range(n_itens):
            # map input split
            valor, peso = map(int, input().split())
            pesos.append(peso)
            valores.append(valor)

        print(dp(pesos, valores, 50))


if __name__ == "__main__":
    main()
