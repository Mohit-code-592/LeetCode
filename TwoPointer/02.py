def check(ch):
    return ch.isalnum()

def valid_palindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if not check(s[start]):
            start += 1
            continue

        if not check(s[end]):
            end -= 1
            continue

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True

    