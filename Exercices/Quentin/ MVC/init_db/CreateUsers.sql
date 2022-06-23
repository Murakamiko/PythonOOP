CREATE TABLE contact(
userid SERIAL,
name VARCHAR(255) NOT NULL,
firstname VARCHAR(255) NOT NULL,
password INT NOT NULL,
email VARCHAR(255) NOT NULL,
userdescription VARCHAR(255),
PRIMARY KEY (userid)
);

CREATE TABLE roles(
    roleid SERIAL PRIMARY KEY,
    poste VARCHAR(80) UNIQUE NOT NULL,
);

CREATE TABLE userrole(
    roleid INT NOT NULL,
    userid INT NOT NULL,
    CONSTRAINT fk_userroleid FOREIGN KEY (roleid) REFERENCES roles(roleid)
    CONSTRAINT fk_useruserid FOREIGN KEY (roleid) REFERENCES 
);