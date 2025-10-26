import os

from sqlalchemy import create_engine, select, Select
from sqlalchemy.engine import Engine

from app.models import records

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "data", "records.db")
DB_URL = f"sqlite:///{DB_PATH}"

engine: Engine = create_engine(DB_URL, connect_args={"check_same_thread": False})


def get_all_ids():
    with engine.connect() as conn:
        res = conn.execute(select(records.c.id)).all()
        return [r[0] for r in res]


def get_record_by_id(rid: int):
    stmt: Select = select(records).where(records.c.id == rid)
    with engine.connect() as conn:
        row = conn.execute(stmt).first()
        if row:
            return dict(row._mapping)
        return None