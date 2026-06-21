def num_to_letter(n):
    return chr(n + ord('A'))

def matrix_vector_mod26(matrix, vector, mod=26):
    print("Matrix:")
    for row in matrix:
        print(row)

    print("\nVector:")
    print(vector)

    print("\nStep-by-step calculation:\n")

    result = []

    for i, row in enumerate(matrix):
        total = 0
        print(f"Row {i} calculation:")

        for j, value in enumerate(row):
            product = value * vector[j][0]
            total += product
            print(f"  {value} * {vector[j][0]} = {product}")

        modded = total % mod
        result.append([modded])

        print(f"  Sum = {total}")
        print(f"  {total} mod {mod} = {modded}\n")

    print("Final Output Vector (mod 26):")
    for row in result:
        print(row)

    print("\nLetter conversion (A=0 ... Z=25):")

    letters = []
    for row in result:
        letter = num_to_letter(row[0])
        letters.append(letter)
        print(f"{row[0]} -> {letter}")

    print("\nFinal Message:")
    print("".join(letters))

    return result


# Matrix (fixed)
matrix = [
    [23, 22],
    [5, 19]
]

# Vector input
vector = [
    [13],
    [14]
]

matrix_vector_mod26(matrix, vector)
