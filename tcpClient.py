from socket import *

# constants
serverPort = 55772
serverName = 'localhost'

# Create socket object for client
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Read sentence from screen ( keyboard)
sentence = input('Input lowercase sentence')
clientSocket.send(sentence.encode())

# receive answer
answerSentence = clientSocket.recv(2048).decode()
print(f'From Server: {answerSentence}')
clientSocket.close()