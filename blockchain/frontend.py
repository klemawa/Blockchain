import tkinter as tk
from tkinter import messagebox
from blockchain import Blockchain

#instancja
blockchain = Blockchain()

def mine_block():
    #wydobycie blokuu
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_transaction('sender1', 'recipient1', 1) # Nagroda za wydobycie
    previous_hash = blockchain.hash(last_block)
    blockchain.create_block(proof, previous_hash)
    messagebox.showinfo("Sukces", "Nowy blok został wydobyty!")

def new_transaction():
    #pobieranie danych
    sender = sender_entry.get()
    recipient = recipient_entry.get()
    amount = amount_entry.get()
    #dodawanie noiwej transakcji
    blockchain.new_transaction(sender, recipient, amount)
    messagebox.showinfo("Sukces", "Transakcja została dodana!")

def check_balance():
    #pobieranie adresu
    address = address_entry.get()
    #liczenie salda
    balance = blockchain.get_balance(address)
    messagebox.showinfo("Saldo portfela", f"Saldo portfela dla adresu {address}: {balance}")

def view_chain():
    #wyświetlanie łańcucha bloków
    chain_info = ''
    for block in blockchain.chain:
        chain_info += f"Index: {block['index']}, Proof: {block['proof']}, Previous Hash: {block['previous_hash']}\n"
    messagebox.showinfo("Łańcuch bloków", chain_info)

# interfejs
root = tk.Tk()
root.title("Blockchain")

#pola danych do transakcji
sender_label = tk.Label(root, text="Wysyłający:")
sender_label.grid(row=0, column=0, padx=5, pady=5)
sender_entry = tk.Entry(root)
sender_entry.grid(row=0, column=1, padx=5, pady=5)

recipient_label = tk.Label(root, text="Odbiorca:")
recipient_label.grid(row=1, column=0, padx=5, pady=5)
recipient_entry = tk.Entry(root)
recipient_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(root, text="Kwota:")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

#dodawanie transakcji
transaction_button = tk.Button(root, text="Dodaj transakcję", command=new_transaction)
transaction_button.grid(row=3, column=0, padx=5, pady=5)

#wyobycie bloku
mine_button = tk.Button(root, text="Wydobądź blok", command=mine_block)
mine_button.grid(row=3, column=1, padx=5, pady=5)

#łańcuch bloków
view_chain_button = tk.Button(root, text="Wyświetl łańcuch bloków", command=view_chain)
view_chain_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

#adres portfela
address_label = tk.Label(root, text="Adres portfela:")
address_label.grid(row=5, column=0, padx=5, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, padx=5, pady=5)

# Przycisk do sprawdzania salda
balance_button = tk.Button(root, text="Sprawdź saldo", command=check_balance)
balance_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

root.mainloop()
