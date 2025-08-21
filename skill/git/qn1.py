
symbol_list = [chr(i) for i in range(33, 127) if not chr(i).isalnum()]

def compute_shifts_from_key(key):
    # letters: use letter positions (a=1..z=26) so result is intuitive
    sum_letters = sum((ord(c.lower()) - 96) for c in key if c.isalpha())
    # digits: sum the numeric digits (1+2+3 -> 6)
    sum_digits = sum(int(c) for c in key if c.isdigit())
    # symbols: count of non-alnum characters (excluding letters/digits)
    symbol_count = sum(1 for c in key if not c.isalnum())
    # total (fallback) used for Unicode chars
    total = sum(ord(c) for c in key)
    letter_shift = sum_letters % 26
    digit_shift = sum_digits % 10
    # if there are no symbols in key, symbol_count will be 0, that's OK
    symbol_shift = symbol_count % len(symbol_list)
    return letter_shift, digit_shift, symbol_shift, total

def encrypt(text, letter_shift, digit_shift, symbol_shift, total):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + letter_shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + letter_shift) % 26 + 97)
        elif ch.isdigit():
            result += chr((ord(ch) - 48 + digit_shift) % 10 + 48)
        elif ch == " ":
            # keep spaces as spaces (common choice)
            result += ch
        else:
            code = ord(ch)
            # ascii punctuation/symbols between 33 and 126 that are not alnum
            if 33 <= code <= 126 and not ch.isalnum():
                idx = symbol_list.index(ch)  # ch is in symbol_list
                result += symbol_list[(idx + symbol_shift) % len(symbol_list)]
            else:
                # other unicode (emoji, etc.) - do a basic shift with total key
                result += chr((ord(ch) + total) % 1114111)
    return result

def decrypt(text, letter_shift, digit_shift, symbol_shift, total):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 - letter_shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 - letter_shift) % 26 + 97)
        elif ch.isdigit():
            result += chr((ord(ch) - 48 - digit_shift) % 10 + 48)
        elif ch == " ":
            result += ch
        else:
            code = ord(ch)
            if 33 <= code <= 126 and not ch.isalnum():
                idx = symbol_list.index(ch)
                result += symbol_list[(idx - symbol_shift) % len(symbol_list)]
            else:
                result += chr((ord(ch) - total) % 1114111)
    return result

# ----------------- main -----------------
print("=== Caesar Cipher (Category-Preserving) ===")
msg = input("Enter your message: ")

key_input = input("Enter shift (integer) OR key string (like ABCDabcd@123): ")

# try parse integer first; if fails, treat as key string
try:
    s = int(key_input)
    letter_shift = s % 26
    digit_shift = s % 10
    symbol_shift = s % len(symbol_list)
    total = s
    print(f"\nUsing integer shift: {s}")
except Exception:
    letter_shift, digit_shift, symbol_shift, total = compute_shifts_from_key(key_input)
    print("\nUsing key string -> computed shifts:")
    print(f"  letter_shift = {letter_shift}")
    print(f"  digit_shift  = {digit_shift}")
    print(f"  symbol_shift = {symbol_shift}")
    # (optional) don't print total if you prefer

encrypted_msg = encrypt(msg, letter_shift, digit_shift, symbol_shift, total)
print("\nEncrypted:", encrypted_msg)

decrypted_msg = decrypt(encrypted_msg, letter_shift, digit_shift, symbol_shift, total)
print("Decrypted:", decrypted_msg)
