import socket

# 创建一个 TCP 套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 定义服务器的 IP 地址和端口号
server_ip = '172.20.15.11'
server_port = 7777

# 绑定 IP 地址和端口号
server_socket.bind((server_ip, server_port))

# 开始监听，最大连接数为 5
server_socket.listen(5)
print(f"服务器正在监听 {server_ip}:{server_port}...")

try:
    while True:
        # 接受客户端连接
        print("等待客户端连接...")
        client_connection, client_address = server_socket.accept()
        print(f"客户端 {client_address} 已连接")

        try:
            # 接收客户端消息
            print("准备接收客户端消息...")
            client_message = client_connection.recv(1024)
            if client_message:
                client_message_decoded = client_message.decode('utf-8')
                print(f"收到客户端消息: {client_message_decoded}")

                # 将消息转换为大写并发送回客户端
                response_message = client_message.upper()
                client_connection.send(response_message)
                print(f"已发送响应消息: {response_message.decode('utf-8')}")
            else:
                print("未收到客户端消息")

        except Exception as e:
            print(f"处理客户端 {client_address} 时发生错误: {e}")
        finally:
            # 关闭客户端连接
            client_connection.close()
            print(f"客户端 {client_address} 连接已关闭")

except KeyboardInterrupt:
    print("服务器已停止，正在关闭...")
finally:
    # 关闭服务器套接字
    server_socket.close()