CREATE TABLE IF NOT EXISTS users_notes(
    id UUID NOT NULL PRIMARY KEY,
    text TEXT NOT NULL
);

GRANT ALL ON DATABASE notes TO service_notes;