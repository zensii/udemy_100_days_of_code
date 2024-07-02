# caeser cipher
def encode(message, shift):
    encoded_msg = ''
    for char in message:
        encoded_msg += chr(ord(char) + shift)
    return encoded_msg


def decode(message, shift):
    decoded_msg = ''
    for char in message:
        decoded_msg += chr(ord(char) - shift)
    return decoded_msg


while True:

    print('What would you like to do, (E)ncode, (D)ecode a message or (Q)uit ? ')

    while True:
        action = input()
        match action:
            case 'E':
                message = input('Enter the message to encode: ')
                shift = int(input('What is the cipher shift: '))
                print(f'Your encoded message is: {encode(message, shift)}')
                break
            case 'D':
                to_decode = input('Enter a message to decode: ')
                shift = int(input('Enter the cipher shift: '))
                print(f'Your decoded message is: {decode(to_decode, shift)}')
                break
            case 'Q':
                print('Goodbye.')
                exit()
            case _:
                print('Please select \'E\' or \'D\'')

