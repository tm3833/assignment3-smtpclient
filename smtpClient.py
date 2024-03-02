from socket import *
#tracy miles
#cs-gy 6843
#3-2-2024

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = 'smtp.gmail.com'
    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    # Fill in start
    clientSocket.connect((mailserver, 587))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1) 
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailfrom = 'MAIL FROM: <myemail@gmail.com>\r\n'
    # Fill in start
    clientSocket.send(mailfrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        print ('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    rcptto = 'RCPT TO: <rcptemail@hotmail.com>\r\n'
    # Fill in start
    clientSocket.send(rcptto.encode())
    recv3 = clientSocket.recv(1024).decode()
    print(recv3)
    if recv3[:3] != '250':
        print ('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    data = 'sending data\r\n'
    # Fill in start
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    print(recv4)
    if recv4[:3] != '354':
        print ('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send('SUBJECT: Hello - test\r\n')
    clientSocket.send('hello there')
    clientSocket.send(msg)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    msgend = '\r\n.\r\n'
    clientSocket.send(endmsg.encode()+ msgend)
    recv5 = clientSocket.recv(1024).decode()
    print(recv5)
    if recv5[:3] != '250':
        print ('250 reply not received from server.')
        
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitcmd = 'Quit\r\n'
    clientSocket.send(quitcomd.encode())
    recv6 = clientSocket.recv(1024).decode()
    print recv6
    if recv6[:3] != '250':
        print ('250 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
