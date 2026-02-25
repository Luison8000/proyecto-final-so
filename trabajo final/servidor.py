# Crear contexto SSL
contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Crear socket normal
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print(f"Servidor seguro escuchando en puerto {PORT}...")

while True:
    conn, addr = servidor.accept()
    print(f"Conexión segura desde {addr}")

    # Envolver conexión en TLS
    conn_segura = contexto.wrap_socket(conn, server_side=True)

    datos = conn_segura.recv(4096).decode()
    respuesta = procesar_comando(datos)

    conn_segura.send(respuesta.encode())
    conn_segura.close()
