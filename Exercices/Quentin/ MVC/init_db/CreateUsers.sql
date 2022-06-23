CREATE TABLE contact(
userid INT NOT NULL,
name VARCHAR(255) NOT NULL,
firstname VARCHAR(255) NOT NULL,
password INT NOT NULL,
email VARCHAR(255) NOT NULL,
userdescription VARCHAR(255),
PRIMARY KEY (userid)
);

CREATE TABLE roles(
    iduser INT NOT NULL,
    poste VARCHAR(255) NOT NULL,
    CONSTRAINT fkuserid
        FOREIGN KEY(iduser)
            REFERENCES contact(userid)
);