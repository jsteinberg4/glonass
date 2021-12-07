
USE db_glonass;

-- DROP TABLE IF EXISTS star_catalog;  
-- CREATE TABLE star_catalog (
-- 	HIP INT,
--     Catalog VARCHAR(255),
--     Survey VARCHAR(255)
-- );
-- ALTER TABLE star_catalog ADD PRIMARY KEY (HIP);
-- ALTER TABLE star_characteristics ADD FOREIGN KEY (HIP) REFERENCES star_catalog(HIP);

-- SHOW VARIABLES LIKE "max_allowed_packet";
-- SET GLOBAL max_allowed_packet = 10000000;

-- GRANT ALL ON db_glonass TO root;

-- SHOW VARIABLES LIKE "local_infile";
-- SET GLOBAL local_infile = 'ON';
-- SHOW VARIABLES LIKE "secure_file_priv";

-- LOAD DATA LOCAL INFILE 'star_catalog.csv' INTO TABLE star_catalog;