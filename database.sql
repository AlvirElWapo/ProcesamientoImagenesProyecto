DROP DATABASE IF EXISTS ProcesamientoDatabase;
CREATE DATABASE ProcesamientoDatabase;

USE ProcesamientoDatabase;

CREATE TABLE Producto_disponible
(
	id INT AUTO_INCREMENT,
    	name CHAR(20),
    	PRIMARY KEY (id)
);

CREATE TABLE lista_de_compras 
(
    id INT AUTO_INCREMENT,
    producto_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (producto_id) REFERENCES Producto_disponible(id)
);
	

INSERT INTO Producto_disponible(name) VALUES
    ('atun'),
    ('sopa'),
    ('gelatina'),
    ('te'),
    ('avena'),
    ('leche'),
    ('rico pollo'),
    ('jumex'),
    ('palomitas');



/*CONSULTA:*/
SELECT prd.name, COUNT(prd.name),ldc.id 
FROM Producto_disponible prd 
JOIN lista_de_compras ldc 
ON ldc.producto_id = prd.id 
GROUP BY prd.name;




