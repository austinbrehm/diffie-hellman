# diffie hellman is used a lot in cryptography

def main():
    # g and n are public
    # a and b are private

    def diffie_hellman(a, b, g, n):
        secret = (g ** (a * b)) % n
        return secret

    x = int(input('a: '))
    y = int(input('b: '))
    z = int(input('g: '))
    e = int(input('n: '))
    secret_key = diffie_hellman(x, y, z, e)
    print('The secret is ' + str(secret_key))


if __name__ == "__main__":
    main()