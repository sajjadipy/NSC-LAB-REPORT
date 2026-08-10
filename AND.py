def convert_bin(c):
    return format(c, '0b')


def convert_hex(c):
    return format(c, '0x')


def transform_str(text, key):

    print(f"{'Char':<6}{'ASCII':<8}{'Binary':<10}{'Hexa':<6}{'AND(Dec)':<10}{'AND(Char)':<10}{'AND(Binary)':<12}")

    print("-" * 60)

    for ch in text:

        ascii_val = ord(ch)
        ascii_bin = convert_bin(ascii_val)
        ascii_hex = convert_hex(ascii_val)

        and_val = ascii_val & key
        and_char = chr(and_val)
        and_bin = convert_bin(and_val)

        print(f"{ch:<6}{ascii_val:<8}{ascii_bin:<10}{ascii_hex:<6}{and_val:<10}{and_char:<10}{and_bin:<12}")


text = "Hello"
key = 127

transform_str(text, key)