import socket
import sys
import logging



# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def encrypt(message): 
    logging.info('the message is "%s"',message[0])
    cipher = '' 
    for letter in message[0]:
        logging.info(letter)
        if letter != ' ': 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher 

def main(): 
    logging.info('Main')

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address given on the command line
    server_name = socket.gethostname()
    server_address = (server_name, 10000)
    logging.info('Started')
    logging.info('starting up on "%s"', server_address)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        logging.info('waiting for a connection-sharonde')
        connection, client_address = sock.accept()

        
        try:
            logging.info('client connected: "%s"', client_address)
            while True:
                # data = connection.recv(16)
                data  = encrypt(client_address)
                logging.info('encrypted data: "%s"', data)
                if data:
                    connection.sendall(data.encode())
                else:
                    continue
        except socket.error:
            continue
        finally:
            connection.close()

# Executes the main function 
if __name__ == '__main__':
    # logging.basicConfig(filename='/tcp_script/tcp_socket-output.log', filemode='w',encoding='utf-8', level=logging.DEBUG)
    root_logger= logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('/tcp_script/tcp_socket-output.log', 'w', 'utf-8')
    formatter = logging.Formatter('%(name)s %(message)s')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    main()