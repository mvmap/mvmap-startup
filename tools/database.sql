SET SESSION storage_engine = "InnoDB";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS company;
CREATE TABLE company (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company_name varchar(200),
    product_name varchar(200),
    website varchar(300),
    location varchar(100),
    create_time varchar(300), 
    status varchar(50),
    stage varchar(50),
    domain varchar(100),
    tags varchar(200),
    intro varchar(1000),
    thumb_large varchar(200),
    thumb_small varchar(200),
    juzi_url varchar(200),
    KEY(id)
);


DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company_id int NOT NULL REFERENCES company(id),
    product_name varchar(200),
    product_type varchar(50),
    product_url varchar(200),
    product_intro varchar(500),
    juzi_url varchar(200),
    KEY(id)
);
