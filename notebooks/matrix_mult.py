def multiply_matrix_scalar(matrix, scalar, mod=26):
    print(f"Scalar: {scalar}")
    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nStep-by-step multiplication:\n")

    result = []

    for i, row in enumerate(matrix):
        new_row = []
        for j, value in enumerate(row):

            multiplied = scalar * value
            modded = multiplied % mod

            print(f"Row {i}, Col {j}:")
            print(f"  {scalar} * {value} = {multiplied}")
            print(f"  {multiplied} mod {mod} = {modded}\n")

            new_row.append(modded)

        result.append(new_row)

    print("Final Result Matrix (mod 26):")
    for row in result:
        print(row)

    return result


# Example usage
matrix = [
    [5, 24],
    [9, 3]
]

scalar = 15

multiply_matrix_scalar(matrix, scalar)
