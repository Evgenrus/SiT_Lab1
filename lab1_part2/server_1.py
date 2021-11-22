# server.py
import select, socket
from functions import *

def main():
    sock = socket.socket()
    sock.bind(('', 8008))
    sock.listen(5)
    sock.setblocking(False)
    inputs = [sock]  # сокеты, которые будем читать
    outputs = []  # сокеты, в которые надо писать
    client_msg = ''
    server_msg_1 = ''
    server_msg_2 = ''
    code = ''
    client_conn = 0
    server_conn = 0
    flag = True

    print('\nОжидание подключения...')
    while inputs:
        reads, send, excepts = select.select(inputs, outputs, inputs)

        for conn in reads:
            if conn == sock:
                new_conn, client_addr = conn.accept()
                print('Успешное подключение!')
                new_conn.setblocking(False)
                inputs.append(new_conn)
            else:
                data = conn.recv(1024)
                if not data:
                    break
                code = data.decode('utf-8')[-1]
                if code == '0':
                    client_conn = conn
                    text = data.decode('utf-8')[0:-1]
                    print('Сообщение от клиента: ', text)
                    client_msg = F(text)
                elif code == '1':
                    server_conn = conn
                    text_1 = data.decode('utf-8')[0:-1]
                    print('Первое сообщение от сервера: ', text_1)
                    server_msg_1 = F1(text_1)
                elif code == '2':
                    server_conn = conn
                    text = data.decode('utf-8')[0:-1]
                    print('Второе сообщение от сервера: ', text)
                    server_msg_2 = text
                if conn not in outputs:
                    outputs.append(conn)

        for conn in send:
            if conn == client_conn:
                conn.send(server_msg_2.encode('utf-8'))
            if conn == server_conn:
                if code == '1' and flag is True:
                    flag = False
                    conn.send(client_msg.encode('utf-8'))
                elif code == '2':
                    conn.send(server_msg_1.encode('utf-8'))

        for conn in excepts:
            print('Клиент отвалился...')
            inputs.remove(conn)
            if conn in outputs:
                outputs.remove(conn)
            conn.close()
    sock.close()


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            break
