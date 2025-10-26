import random
import sqlite3
from pathlib import Path

NUM_MIN = 50
NUM_MAX = 150

BASE_DIR = Path(__file__).parent / "app"
DATA_DIR = BASE_DIR / "data"
DB_FILE = DATA_DIR / "records.db"

DATA_DIR.mkdir(parents=True, exist_ok=True)

if DB_FILE.exists():
    DB_FILE.unlink()

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute(
"""
CREATE TABLE records (
id INTEGER PRIMARY KEY,
type TEXT NOT NULL,
url TEXT,
picture TEXT,
text TEXT
)
"""
)


count = random.randint(NUM_MIN, NUM_MAX)
print(f"Seeding {count} records into {DB_FILE}")

for i in range(1, count + 1):
    rtype = random.choice(["webview", "image", "text"])
    if rtype == "webview":
        url = f"https://google.com"
        picture = None
        text = None
    elif rtype == "image":
        picture = f"https://ih1.redbubble.net/image.4905811447.8675/flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
        url = None
        text = None
    else:
        text = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
        url = None
        picture = None

    cur.execute(
    "INSERT INTO records (id, type, url, picture, text) VALUES (?, ?, ?, ?, ?)",
    (i, rtype, url, picture, text),
    )


conn.commit()
conn.close()
print("Seeding complete.")