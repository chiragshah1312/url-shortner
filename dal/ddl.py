CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS urls(
    url_id INTEGER PRIMARY KEY AUTOINCREMENT,
    uid VARCHAR(25),
    link text,
    created_timestamp TIMESTAMP,
    updated_timestamp TIMESTAMP
);
"""
]