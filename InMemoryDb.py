class InMemoryDB:

    def __init__(self):
        self.commited = {}
        self.staged = None
        self.inTransaction = False

    def begin_transaction(self):
        if self.inTransaction:
            raise RuntimeError("Transaction already in progress")
        self.staged = {}
        self.inTransaction = True

    def commit(self):
        if not self.inTransaction:
            raise RuntimeError("Can't call commit without an active transaction")
        self.commited.update(self.staged)
        self.staged = None
        self.inTransaction = False

    def rollback(self):
        if not self.inTransaction:
            raise RuntimeError("Can't call rollback without an active transaction")
        self.staged = None
        self.inTransaction = False

    def put(self, key, value):
        if not self.inTransaction:
            raise RuntimeError("Can't call put without an active transaction")
        self.staged[key] = value

    def get(self, key):
        return self.commited.get(key)

if __name__ == "__main__":
    db = InMemoryDB()
    print(db.get("A"))  # None

    try:
        db.put("A", 5)
    except RuntimeError as err:
        print("Error:", err)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # Still None (uncommitted)
    db.put("A", 6)
    db.commit()
    print(db.get("A"))  # 6

    for fn in (db.commit, db.rollback):
        try:
            fn()
        except RuntimeError as err:
            print("Error:", err)

    print(db.get("B"))  # None

    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B"))  # None

    db2 = InMemoryDB()
    db2.begin_transaction()
    db2.put("X", 99)
    db2.commit()
    print(db2.get("X"))  # 99
