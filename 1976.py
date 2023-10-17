def make_matrix(n):
    matrix = [[None] * n for _ in range(n)]

    return matrix


def print_m(m):
    max_len = max(
        max(len(str(m[i][j])) for j in range(1, len(m[i]))) for i in range(1, len(m))
    )

    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            print(str(m[i][j]).center(max_len), end=" ")
        print()


def pd(dimensions, costs, choices):
    n_dim = len(dimensions) - 1
    for n in range(1, n_dim):
        i = 1
        j = i + n

        while j <= n_dim:
            possibilities = []
            for k in range(i, j):
                cost = costs[i][k] + costs[k + 1][j] + d(dimensions, i - 1, k, j)
                possibilities.append((cost, k))

            smaller = min(possibilities, key=lambda x: x[0])
            costs[i][j] = smaller[0]
            choices[i][j] = smaller[1]

            i += 1
            j += 1


def d(dimensions, i, k, j):
    return dimensions[i] * dimensions[k] * dimensions[j]


def number_to_letter(x):
    return f"A{x}"


def find_parens(choices, i, j):
    if i == j:
        print(number_to_letter(i), end="")
    else:
        print("(", end="")
        choice = choices[i][j]
        find_parens(choices, i, choice)
        find_parens(choices, choice + 1, j)
        print(")", end="")


def init_dimensions(n):
    dimensions = []
    for i in range(n):
        d1, d2 = map(int, input().split())

        if len(dimensions) == 0:
            dimensions.append(d1)
            dimensions.append(d2)
        else:
            dimensions.append(d2)
    return dimensions


def main():
    n = int(input())

    while n != 0:
        dimensions = init_dimensions(n)
        costs = None
        choices = None

        costs = make_matrix(n + 1)
        choices = make_matrix(n + 1)

        for i in range(1, n + 1):
            costs[i][i] = 0

        pd(dimensions, costs, choices)

        find_parens(choices, 1, n)
        print()
        print(costs[1][n])

        n = int(input())


if __name__ == "__main__":
    main()
