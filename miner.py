import hashlib
import time

# Definindo o endereço da carteira de Dogecoin e a dificuldade
wallet_address = "DAkzcyXd5yDQRaYiVbrcqq93S9LZKSBQr6"
difficulty = 4  # Número de zeros iniciais no hash para validar o bloco

def mine_block():
    # Dados fictícios do bloco
    block_data = "Block Data for Dogecoin"

    # Começa a minerar
    nonce = 0
    while True:
        block_header = f"{block_data}{nonce}"
        block_hash = hashlib.sha256(block_header.encode()).hexdigest()

        # Verifica se o hash tem a quantidade de zeros (dificuldade)
        if block_hash[:difficulty] == "0" * difficulty:
            print(f"Bloco minerado: {block_hash}")
            print(f"Enviando para a carteira: {wallet_address}")
            break
        nonce += 1

if __name__ == "__main__":
    mine_block()
