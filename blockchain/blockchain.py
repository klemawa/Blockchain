import hashlib
import json
from time import time
from tkinter import messagebox



class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(proof=100, previous_hash='1')  # Tworzenie bloku genezyjskiego

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Czyszczenie listy transakcji
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    # W klasie Blockchain dodajemy metodę do obliczania salda dla określonego adresu
    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['sender'] == address:
                    balance -= int(transaction['amount'])
                elif transaction['recipient'] == address:
                    balance += int(transaction['amount'])
        return balance

    # W interfejsie użytkownika aktualizujemy funkcję do sprawdzania salda
    def check_balance():
        # Pobieramy adres z interfejsu użytkownika
        address = address_entry.get()
        # Obliczamy saldo dla danego adresu
        balance = blockchain.get_balance(address)
        # Wyświetlamy saldo w oknie dialogowym
        messagebox.showinfo("Saldo portfela", f"Saldo portfela dla adresu {address}: {balance}")

    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Dowód pracy polega na uzyskaniu hashu z 4 początkowymi zerami


# Tworzenie nowej instancji blockchaina
blockchain = Blockchain()

# Przykładowe transakcje i wydobycie nowego bloku
blockchain.new_transaction('sender1', 'recipient1', 1)
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)
blockchain.create_block(proof, blockchain.hash(last_block))

# Wyświetlenie łańcucha bloków
print("Blockchain:")
print(blockchain.chain)
