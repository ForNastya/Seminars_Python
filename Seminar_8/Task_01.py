def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)