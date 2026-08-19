CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists programminglanguage(
        id integer primary key autoincrement,
        name text,
            short_name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists command_processing(
        id integer primary key autoincrement,
        programminglanguage_id text,
            type text,
            description text,
            script_or_cli text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists switch(
        id integer primary key autoincrement,
        name text,
            programming_language_id text,
            description text,
            typeargument text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists interprocess_communication(
        id integer primary key autoincrement,
        programminglanguage_id text,
            name text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists way_handle_insecure_data(
        id integer primary key autoincrement,
        programminglanguage_id text,
            name text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists way_handle_insecure_code(
        id integer primary key autoincrement,
        programminglanguage_id text,
            name text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists generate_other_language_in_the_programming_language(
        id integer primary key autoincrement,
        programminglanguage_id text,
            otherprogramminglanguage_id text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists generate_the_programming_language_from_other_language(
        id integer primary key autoincrement,
        programminglanguage_id text,
            fromotherprogramminglanguage_id text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists translate_the_programming_language_to_other_language(
        id integer primary key autoincrement,
        programminglanguage_id text,
            otherprogramminglanguage_id text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists embedprogramminglanguageinascript(
        id integer primary key autoincrement,
        programminglanguage_id text,
            script_programminglanguage_id text,
            description text,
            script text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
