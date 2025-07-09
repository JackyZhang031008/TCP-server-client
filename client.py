import socket

# 创建一个 TCP 套接字对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义服务器的 IP 地址和端口号
server_ip = '172.20.15.11'
server_port = 7777

try:
    # 连接到服务器
    client_socket.connect((server_ip, server_port))
    print(f"成功连接到服务器 {server_ip}:{server_port}")

    # 要发送的消息
    message_to_send = 'Hello, my boy!'
    # 编码并发送消息
    client_socket.send(message_to_send.encode('utf-8'))
    print(f"已发送消息: {message_to_send}")

    # 接收服务器的响应
    received_message = client_socket.recv(1024)
    print(f"收到服务器响应: {received_message.decode('utf-8')}")

except ConnectionRefusedError:
    print(f"无法连接到服务器 {server_ip}:{server_port}，请检查服务器是否正在运行。")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    # 关闭套接字连接
    client_socket.close()