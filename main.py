class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class Item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Transaction:
    def __init__(self, transaction_id, items):
        self.transaction_id = transaction_id
        self.items = items

clients = [
    Client(1, "Anna"),
    Client(2, "Martins")
]

items = [
    Item(1, "Coca-cola", 10),
    Item(2, "Fanta", 70),
    Item(3, "Sprite", 40)
]

transactions = [
    Transaction(1, [items[0], items[1]]),
    Transaction(2, [items[2]]),
    Transaction(3, [items[1], items[2]])
]

clients[0].add_transaction(transactions[0])
clients[0].add_transaction(transactions[2])
clients[1].add_transaction(transactions[1])

print("All clients:")
for client in clients:
    print(f"Client: {client.name}")

    print("Transactions:")
    for transaction in client.transactions:
        print(f"  Transaction ID: {transaction.transaction_id}")

        print("  Items purchased:")
        for item in transaction.items:
            print(f"    {item.name} - ${item.price}")
