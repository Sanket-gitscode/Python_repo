def string_to_int(string: str) -> int:
    result = 0
    started = False
    sign = 1
    sign_seen = False

    for ch in string:

        # Skip leading spaces
        if not started and not sign_seen and ch.isspace():
            continue

        # Handle sign
        if not started and not sign_seen:
            if ch == "-":
                sign = -1
                sign_seen = True
                continue

            if ch == "+":
                sign = 1
                sign_seen = True
                continue

        # Stop at first non-digit
        if not ch.isdigit():
            break

        # We are now reading the number
        started = True

        digit = int(ch)
        result = result * 10 + digit

    result *= sign

    # 32-bit signed integer range
    if result > 2147483647:
        return 2147483647

    if result < -2147483648:
        return -2147483648

    return result