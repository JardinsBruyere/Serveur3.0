CREATE TABLE ListeTypeComposants (
  typeComposant INTEGER PRIMARY KEY AUTOINCREMENT,
  NomComposant CHAR (30),
  FOREIGN KEY (typeComposant) REFERENCES Composant(type)
);

CREATE TABLE Composant (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type INTEGER,
  DateAjout DATETIME DEFAULT (datetime('now','localtime')),
  Position INTEGER,
  FOREIGN KEY (id) REFERENCES Alerte(ComposantCible),
  FOREIGN KEY (id) REFERENCES RelevesCapteurs(IdCapteur),
  FOREIGN KEY (Position) REFERENCES ListeBacPosition(Capteur)
);

CREATE TABLE ListeTypeAlerte (
  TypeAlerte INTEGER PRIMARY KEY AUTOINCREMENT,
  Criticite INTEGER,
  MethodeNotification INTEGER,
  FOREIGN KEY (TypeAlerte) REFERENCES Alerte(TypeAlerte)
);

CREATE TABLE Alerte (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  TypeAlerte INTEGER,
  ComposantCible INTEGER,
  seuil INTEGER,
  FOREIGN KEY (id) REFERENCES AlerteRecu(NumeroDalerte)
);

CREATE TABLE AlerteRecu (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  DateAjout DATETIME DEFAULT (datetime('now','localtime')),
  NumeroDalerte INTEGER
);

CREATE TABLE RelevesCapteurs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  IdCapteur INTEGER,
  DateAjout DATETIME DEFAULT (datetime('now','localtime')),
  Valeur INTEGER
);

CREATE TABLE Bac (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  x INTEGER,
  y INTEGER,
  etage INTEGER,
  NomBac CHAR (100),
  FOREIGN KEY (id) REFERENCES ListeBacPosition(Bac)
);

CREATE TABLE ListeBacPosition (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Capteur INTEGER,
  Bac INTEGER
);

INSERT INTO Composant (type,Position) VALUES (2,7);
INSERT INTO ListeTypeComposants (NomComposant) VALUES ("Temperature");
INSERT INTO ListeTypeAlerte (Criticite,MethodeNotification) VALUES (2,1);
INSERT INTO Alerte (TypeAlerte,ComposantCible, seuil) VALUES (2,1,1);
INSERT INTO AlerteRecu (NumeroDalerte) VALUES (1);
INSERT INTO RelevesCapteurs (IdCapteur,Valeur) VALUES (1,16);
INSERT INTO Bac (x,y,etage,NomBac) VALUES (4,9,0,"Bac a tomate");
INSERT INTO ListeBacPosition (Capteur,Bac) VALUES (1,1);