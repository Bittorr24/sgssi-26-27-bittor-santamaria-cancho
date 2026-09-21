from collections import Counter
FREQ_ES = {
    'E': 16.78, 'A': 11.96, 'O': 8.69, 'L': 8.37, 'S': 7.88, 'N': 7.01,
    'D': 6.87, 'R': 4.94, 'U': 4.80, 'I': 4.15, 'T': 3.31, 'C': 2.92,
    'P': 2.776, 'M': 2.12, 'Y': 1.54, 'Q': 1.53, 'B': 0.92, 'H': 0.89,
    'G': 0.73, 'F': 0.52, 'V': 0.39, 'J': 0.30, 'Ñ': 0.29, 'Z': 0.15,
    'X': 0.06, 'K': 0.00, 'W': 0.00,
}

ORIGINAL = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""


def frecuencias_texto(texto: str):
    letras = [c for c in texto if c.isalpha()]
    total = len(letras)
    conteo = Counter(letras)
    return sorted(
        ((letra, n, 100 * n / total) for letra, n in conteo.items()),
        key=lambda t: -t[1],
    )


def imprimir_tabla_frecuencias_español():
    print("\n=== Frecuencias del español ===")
    for letra, pct in sorted(FREQ_ES.items(), key=lambda t: -t[1]):
        print(f"  {letra}: {pct:5.2f}%")


def imprimir_tabla_frecuencias_texto():
    print("\n=== Frecuencias del texto cifrado ===")
    for letra, n, pct in frecuencias_texto(ORIGINAL):
        print(f"  {letra}: {n:3d}  ({pct:5.2f}%)")


def aplicar_mapa(texto: str, mapa: dict) -> str:
    """Sustituye cada letra cifrada por la que le hayas asignado.
    Se busca por el carácter TAL CUAL aparece en el texto (no por su
    mayúscula), porque en este cifrado 'v' y 'V' son dos símbolos
    distintos: cambiar uno no afecta al otro.
    Lo que no está en el mapa se deja igual que en el original."""
    salida = []
    for c in texto:
        if c.isalpha() and c in mapa:
            nueva = mapa[c]
            salida.append(nueva.upper() if c.isupper() else nueva.lower())
        else:
            salida.append(c)
    return ''.join(salida)


def imprimir_original_y_auxiliar(mapa: dict):
    imprimir_tabla_frecuencias_texto()
    print("\n--- ORIGINAL ---")
    print(ORIGINAL)
    print("\n--- AUXILIAR ---")
    print(aplicar_mapa(ORIGINAL, mapa))


def asignar_por_frecuencia() -> dict:
    """Empareja la letra cifrada más frecuente con la letra española
    más frecuente, la segunda con la segunda, etc. Es solo un punto de
    partida: con un texto de este tamaño no acierta todas las letras."""
    frec_texto = frecuencias_texto(ORIGINAL)
    frec_español = sorted(FREQ_ES.items(), key=lambda t: -t[1])
    mapa = {}
    for (letra_cifrada, _, _), (letra_plana, _) in zip(frec_texto, frec_español):
        mapa[letra_cifrada] = letra_plana.lower()
    return mapa


def main():
    imprimir_tabla_frecuencias_español()

    mapa = asignar_por_frecuencia()
    imprimir_original_y_auxiliar(mapa)

    print("\nAsignación inicial hecha por orden de frecuencia (arriba).")
    print("Comandos:")
    print("  X E          -> cambio manual: letra cifrada X por letra plana E")
    print("  salir        -> termina\n")

    while True:
        entrada = input("> ").strip()
        if not entrada:
            continue

        if entrada.lower() == "salir":
            break

        partes = entrada.split()

        if len(partes) == 2 and len(partes[0]) == 1 and len(partes[1]) == 1:
            letra_tecleada, plana = partes[0], partes[1].lower()
            # 'v' y 'V' son dos símbolos distintos en este cifrado: se
            # respeta tal cual la mayúscula/minúscula que hayas tecleado.
            # El resto de letras siempre aparecen en mayúscula en el
            # texto cifrado, así que se normalizan a mayúscula.
            cifrada = letra_tecleada if letra_tecleada.lower() == 'v' else letra_tecleada.upper()
            mapa[cifrada] = plana
            print(f"Cambiado: '{cifrada}' -> '{plana}'")
            imprimir_original_y_auxiliar(mapa)
            continue

        print("Formato no reconocido. Usa: X E   (o 'salir')")


if __name__ == "__main__":
    main()