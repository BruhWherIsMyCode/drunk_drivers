CREATE TABLE IF NOT EXISTS drivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    family_name TEXT NOT NULL,
    plate_number TEXT NOT NULL
)