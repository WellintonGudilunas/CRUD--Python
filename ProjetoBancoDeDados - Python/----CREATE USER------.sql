drop user 'Admin'@'localhost';

create user 'Admin'@'localhost'
	IDENTIFIED by '3333';
    
GRANT SELECT, DELETE, DROP, REFERENCES, CREATE, ALTER, INSERT, UPDATE ON projetodb.* TO 'Admin'@'localhost';

GRANT UPDATE ON projetodb.* TO 'Admin'@'localhost';