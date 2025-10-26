from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

records = Table(
    "records",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type", String, nullable=False),
    Column("url", String, nullable=True),
    Column("picture", String, nullable=True),
    Column("text", String, nullable=True),
)