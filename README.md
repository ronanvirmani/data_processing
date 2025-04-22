# In‑Memory Key‑Value Database

This project is an in memory database with transaction support.
## Files

| File              | Description                                    |
|-------------------|------------------------------------------------|
| `inMemoryDb.py` | Core implementation and a demonstration script |
| `README.md`       | You are here — setup & usage instructions      |

## Requirements

* **Python 3.8 +** 

## Setup

1. **Clone or download** this repository (or just copy the two files somewhere on disk).

## Running the file
python3 inMemoryDb.py

## Sample test

```
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
```

## How the assignment could be modified

Talk more about making sure that the values passed into the functions are correct type that way the dictionary doesn't get an invalid key.
Could add a size() function to see how large the dictionary currently is. We could also just have the students provide a video explaining their code
and how them running it for grading.



