create database lib_login;
use lib_login;
create table User(User_ID varchar(20), Name varchar(20) unique, Password VARCHAR(64), Email LONGTEXT, Contact_number varchar(10), SecretQuestion LONGTEXT, SecretAnswer LONGTEXT, primary key(User_ID));
create table Admin(Admin_ID varchar(20), Name varchar(20) unique, Password VARCHAR(64), SecretQuestion LONGTEXT, SecretAnswer LONGTEXT, primary key(Admin_ID));  

DELIMITER //
CREATE TRIGGER before_insert_User
BEFORE INSERT ON User
FOR EACH ROW
BEGIN
    SET NEW.User_ID = CONCAT('U', (SELECT IFNULL(MAX(CAST(SUBSTRING(User_ID, 2) AS SIGNED)) + 1, 1) FROM User));
END;
//
DELIMITER ; 

insert into Admin(Admin_ID, name, Password, SecretQuestion, SecretAnswer) values('A1', 'admin1', 'admin1', 'What is the name of your first pet?', 'Rico');
insert into Admin (Admin_ID, Name, Password, SecretQuestion, SecretAnswer) values('A2', 'admin2', 'admin2', 'In what city were you born?', 'Bengaluru');

drop role 'user';
drop role 'admin';

create role 'user';
create role 'admin';
