import time
import random

usuarios = ["Ana", "Bruno", "Carlos", "Diana"]

while True:
    usuario = random.choice(usuarios)
    acao = random.choice(["login", "logout", "erro"])
    log = f"{usuario} realizou {acao}"
    print(log)  # log vai para stdout
    with open("app.log", "a") as f:
        f.write(log + "\n")
    time.sleep(2)