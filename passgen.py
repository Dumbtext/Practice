from random import choice,randint
from passwordmeter import test

lettas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specials = ['@','$',"!"]


def create_pass(numlettas=8, numdigits=4, numspecial=3):
    pass_str = ''
    for _ in range(numlettas):
        pass_str += choice(lettas).capitalize()
    for _ in range(numdigits):
        pass_str += str(randint(1, 9))
    for _ in range(numspecial):
        pass_str += choice(specials)
    return pass_str

def main():
    pass_str=create_pass()
    strength, improvements=test(pass_str)
    print('\nPassword is: %s'%pass_str)
    print('\nStrength: %r'%strength, improvements)

if __name__ == '__main__':
    main()