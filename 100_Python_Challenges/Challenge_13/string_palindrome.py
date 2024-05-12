def is_palindrome(string):
    string = string.replace(" ", '').lower()

    resersed_string = string[::-1]

    return string == resersed_string

print(is_palindrome("madam"))