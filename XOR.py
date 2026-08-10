

def convert_bin(c):
    return format(c, '0b')


def convert_hex(c):
    return format(c, '0x')


def transform_str(text, key):

    print(f"{'Char':<6}{'ASCII':<8}{'Binary':<10}{'Hexa':<6}{'XOR(Dec)':<10}{'XOR(Char)':<10}{'XOR(Binary)':<12}")

    print("-" * 60)

    for ch in text:

        ascii_val = ord(ch)
        ascii_bin = convert_bin(ascii_val)
        ascii_hex = convert_hex(ascii_val)

        xor_val = ascii_val ^ key
        xor_char = chr(xor_val)
        xor_bin = convert_bin(xor_val)

        print(f"{ch:<6}{ascii_val:<8}{ascii_bin:<10}{ascii_hex:<6}{xor_val:<10}{xor_char:<10}{xor_bin:<12}")


text = "Hello"
key = 127

transform_str(text, key)
