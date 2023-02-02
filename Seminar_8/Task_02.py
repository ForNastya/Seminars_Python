def encrypt_caesar(msg, shift=3):
    s_symbols1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    b_symbols1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(s_symbols1)
    small_symbols2 = s_symbols1[shift:] + s_symbols1[:shift]
    big_symbols2 = b_symbols1[shift:] + b_symbols1[:shift]
    translation = msg.maketrans(s_symbols1 + b_symbols1, small_symbols2 + big_symbols2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)

print (encrypt_caesar('Добрый день)',5))