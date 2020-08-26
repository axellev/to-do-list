CREATE TABLE IF NOT EXISTS "todolists" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL CHECK(length(title) >= 1),
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO todolists VALUES
  (1, 'First to-do list'),
  (2, 'Training final project');

CREATE TABLE IF NOT EXISTS "items" (
	"id"	INTEGER NOT NULL UNIQUE,
	"description"	TEXT NOT NULL CHECK(length(description) >= 3),
	"status"	TEXT NOT NULL DEFAULT todo,
	"todolist" INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
  CONSTRAINT fk_todolists
	FOREIGN KEY("todolist_id") 
  REFERENCES todolists("id")
  ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "users" (
  "id"	INTEGER NOT NULL UNIQUE,
  "username"	TEXT NOT NULL UNIQUE,
  "email"	TEXT NOT NULL UNIQUE,
  "hashed_password"	TEXT NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT),
);

INSERT INTO items VALUES
  (21, 'try DB browser','todo', 1),
  (23, 'create connexion db in python','todo', 1),
  (28, 'display database in python program', 'todo', 1),
  (1, 'make an example list', 'done', 2),
  (3, 'make a new git commit', 'done', 2),
  (5, 'looping trough a dictionnary', 'done', 2),
  (7, 'read flask documentation', 'done', 2),
  (2, 'install venv', 'todo', 2),
  (10, 'open my webpage made with flask', 'todo', 2),
  (4, 'print HTML from my file display.py','todo', 2),
  (6, 'change display.one to print ID','todo', 2),
  (8, 'sort list with key filter and lambda','todo', 2),
  (14, 'clean code','todo', 2),
  (12, 'complete howto.md','todo', 2),
  (15, 'make a function that use todolist_0','todo', 2),
  (20, 'commit it','todo', 1),
  (35, 'delete items','todo', 1),
  (18, 'update items','todo', 1);

DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES
  ('todolists', 2),
  ('items', 28);
