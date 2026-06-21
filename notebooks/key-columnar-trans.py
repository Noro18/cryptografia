import math

def get_key_order(keyword):
    """Return column order based on alphabetical ranking of keyword letters."""
    indexed = sorted(enumerate(keyword.upper()), key=lambda x: x[1])
    order = [0] * len(keyword)
    for rank, (original_idx, _) in enumerate(indexed):
        order[original_idx] = rank + 1
    return order

def encrypt(plaintext, keyword):
    keyword = keyword.upper()
    plaintext = plaintext.upper().replace(" ", "")
    num_cols = len(keyword)
    num_rows = math.ceil(len(plaintext) / num_cols)

    # Pad plaintext with X if needed
    padded = plaintext.ljust(num_rows * num_cols, 'X')

    # Build grid
    grid = [list(padded[i*num_cols:(i+1)*num_cols]) for i in range(num_rows)]

    key_order = get_key_order(keyword)

    # Sort columns by key order
    col_sequence = sorted(range(num_cols), key=lambda i: key_order[i])

    ciphertext = ""
    for col in col_sequence:
        for row in grid:
            ciphertext += row[col]

    return ciphertext, grid, key_order, padded, num_rows, num_cols

def decrypt(ciphertext, keyword):
    keyword = keyword.upper()
    ciphertext = ciphertext.upper().replace(" ", "")
    num_cols = len(keyword)
    num_rows = math.ceil(len(ciphertext) / num_cols)

    key_order = get_key_order(keyword)
    col_sequence = sorted(range(num_cols), key=lambda i: key_order[i])

    # Figure out column lengths (last columns may be shorter if uneven)
    full_cols = len(ciphertext) % num_cols
    col_lengths = []
    for i in range(num_cols):
        col_lengths.append(num_rows if (full_cols == 0 or col_sequence.index(i) < full_cols) else num_rows - 1)

    # Actually: all columns are same length when padded. Assume padded.
    col_len = num_rows

    # Split ciphertext into columns
    columns = {}
    idx = 0
    for col in col_sequence:
        columns[col] = list(ciphertext[idx:idx+col_len])
        idx += col_len

    # Rebuild grid row by row
    grid = []
    for r in range(num_rows):
        row = [columns[c][r] for c in range(num_cols)]
        grid.append(row)

    plaintext = ''.join(''.join(row) for row in grid).rstrip('X')
    return plaintext, grid

def print_grid(keyword, key_order, grid, title):
    num_cols = len(keyword)
    col_w = 4

    print(f"\n  {'─'*((col_w)*num_cols + num_cols - 1)}")
    print(f"  {title}")
    print(f"  {'─'*((col_w)*num_cols + num_cols - 1)}")

    # Keyword row
    header = "  " + " ".join(f" {keyword[i]} " for i in range(num_cols))
    print(header)

    # Key order row
    order_row = "  " + " ".join(f"[{key_order[i]}]" for i in range(num_cols))
    print(order_row)

    print("  " + "─"*((col_w)*num_cols + num_cols - 1))

    # Grid rows
    for row in grid:
        print("  " + " ".join(f" {ch} " for ch in row))

    print("  " + "─"*((col_w)*num_cols + num_cols - 1))

def print_banner():
    print("\n" + "═"*52)
    print("   KEYWORD COLUMNAR TRANSPOSITION CIPHER TOOL")
    print("═"*52)

def main():
    print_banner()

    print("\n  Choose mode:")
    print("  [1] Encrypt")
    print("  [2] Decrypt")
    choice = input("\n  Enter 1 or 2: ").strip()

    if choice not in ('1', '2'):
        print("  Invalid choice. Exiting.")
        return

    keyword = input("\n  Enter keyword : ").strip()
    if not keyword.isalpha():
        print("  Keyword must contain letters only.")
        return

    if choice == '1':
        plaintext = input("  Enter plaintext: ").strip()
        if not plaintext:
            print("  Plaintext cannot be empty.")
            return

        ciphertext, grid, key_order, padded, num_rows, num_cols = encrypt(plaintext, keyword)

        print("\n" + "─"*52)
        print("  ENCRYPTION STEPS")
        print("─"*52)
        print(f"\n  Keyword        : {keyword.upper()}")
        print(f"  Plaintext      : {plaintext.upper()}")
        print(f"  Padded text    : {padded}  (padded with X if needed)")

        print_grid(keyword.upper(), key_order, grid, "Grid Layout (read rows left→right)")

        # Show column reading order
        col_sequence = sorted(range(num_cols), key=lambda i: key_order[i])
        print("\n  Column reading order:")
        for rank, col in enumerate(col_sequence):
            col_letters = ''.join(row[col] for row in grid)
            print(f"    Col {rank+1} → [{keyword.upper()[col]}] : {col_letters}")

        print("\n" + "═"*52)
        print(f"  CIPHERTEXT : {ciphertext}")
        print("═"*52 + "\n")

    else:
        ciphertext = input("  Enter ciphertext: ").strip()
        if not ciphertext:
            print("  Ciphertext cannot be empty.")
            return

        plaintext, grid = decrypt(ciphertext, keyword)
        key_order = get_key_order(keyword)

        print("\n" + "─"*52)
        print("  DECRYPTION STEPS")
        print("─"*52)
        print(f"\n  Keyword    : {keyword.upper()}")
        print(f"  Ciphertext : {ciphertext.upper()}")

        print_grid(keyword.upper(), key_order, grid, "Reconstructed Grid")

        print("\n" + "═"*52)
        print(f"  PLAINTEXT  : {plaintext}")
        print("═"*52 + "\n")

if __name__ == "__main__":
    main()
