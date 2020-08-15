CREATE TABLE IF NOT EXISTS "items" (
	"id"	INTEGER NOT NULL UNIQUE,
	"description"	TEXT NOT NULL CHECK(length(description) >= 5),
	"status"	TEXT NOT NULL DEFAULT todo,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO items VALUES
  (1, 'try DB browser','todo'),
  (3, 'create connexion db in python','todo'),
  (8, 'display database in python program', 'todo');

DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES
  ('items',11); 
