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
