# diffie hellman is used a lot in cryptography
# g and n are public
# a and b are private
def diffie_hellman(a, b, g, n):
    secret = (g ** (a * b)) % n
    return secret
