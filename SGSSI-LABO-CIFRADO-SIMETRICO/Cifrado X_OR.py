def xor_bytes(datos, clave):
    """Aplica XOR byte a byte entre datos y clave."""
    return bytes(d ^ k for d, k in zip(datos, clave))


# Datos de prueba
mensaje = b"ATAQUE AL AMANECER"
clave = b"CLAVE1234567890123"
#añado el 2 y el 3 para que ambos tengan longitud 18
print(len(clave))
print(len(mensaje))
# Comprobar que tienen la misma longitud
if len(mensaje) != len(clave):
    raise ValueError("El mensaje y la clave deben tener la misma longitud.")

# Cifrado
criptograma = xor_bytes(mensaje, clave)

# Descifrado: XOR con la misma clave
mensaje_descifrado = xor_bytes(criptograma, clave)

# Mostrar resultados en hexadecimal
print("Mensaje     :", mensaje.hex().upper())
print("Clave       :", clave.hex().upper())
print("Criptograma :", criptograma.hex().upper())
print("Descifrado  :", mensaje_descifrado.hex().upper())

# Comprobación
if mensaje_descifrado == mensaje:
    print("Comprobación: CORRECTA")
else:
    print("Comprobación: ERROR")
