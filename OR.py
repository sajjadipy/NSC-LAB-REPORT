def convert_bin(c):
    return format(c, '0b')


def convert_hex(c):
    return format(c, '0x')


def transform_str(text, key):

    print(f"{'Char':<6}{'ASCII':<8}{'Binary':<10}{'Hexa':<6}{'OR(Dec)':<10}{'OR(Char)':<10}{'OR(Binary)':<12}")

    print("-" * 60)

    for ch in text:

        ascii_val = ord(ch)
        ascii_bin = convert_bin(ascii_val)
        ascii_hex = convert_hex(ascii_val)

        or_val = ascii_val | key
        or_char = chr(or_val)
        or_bin = convert_bin(or_val)

        print(f"{ch:<6}{ascii_val:<8}{ascii_bin:<10}{ascii_hex:<6}{or_val:<10}{or_char:<10}{or_bin:<12}")


text = "Hello"
key = 127

transform_str(text, key)