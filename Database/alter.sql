

ALTER TABLE courseinfo
ADD CONSTRAINT fk_user_name
FOREIGN KEY (user_name)
REFERENCES login(username);