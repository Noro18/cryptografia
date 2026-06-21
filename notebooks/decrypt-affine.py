ciphertext = "UFQFAU OMF FNDO VNEE"

print("=" * 55)
print("         DECRYPTION PROCESS: x = 19(y - 13) mod 26")
print("=" * 55)
print(f"{'Char':<6} {'y':>4} {'y-13':>6} {'19(y-13)':>10} {'x (mod 26)':>12} {'Plain'}")
print("-" * 55)

plaintext = ""

for ch in ciphertext:
    if ch == " ":
        plaintext += " "
        print(f"{'(sp)':<6} {'-':>4} {'':>6} {'':>10} {'':>12} {' '}")
        continue

    y = ord(ch) - ord('A')           # Convert letter to 0–25
    inner = y - 13
ciphertext = "UFQFAU OMF FNDO VNEE"

print("=" * 40)
print("  DECRYPTION: x = 19(y - 13) mod 26")
print("=" * 40)

plaintext = ""

for ch in ciphertext:
    if ch == " ":
        plaintext += " "
        continue

    y = ord(ch) - ord('A')
    inner = y - 13
    product = 19 * inner
    x = product % 26
    plain = chr(x + ord('A'))
    plaintext += plain

    print(f"\nLetter : {ch}")
    print(f"  y             = {y}  ({ch} -> {y})")
    print(f"  y - 13        = {y} - 13 = {inner}")
    print(f"  19 * (y - 13) = 19 * {inner} = {product}")
    print(f"  x mod 26      = {product} mod 26 = {x}")
    print(f"  Plain letter  = {x} -> {plain}")

print("\n" + "=" * 40)
print(f"  Ciphertext : {ciphertext}")
print(f"  Plaintext  : {plaintext}")
print("=" * 40)
