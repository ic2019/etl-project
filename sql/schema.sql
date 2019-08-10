----Creating pizza_db database----
create database pizza_db


-----drop existing table pizza------------
drop table if exists pizza;

----drop existing table restaurant-----------
drop table if exists restaurant;


-----drop existing table best_piza_restaurants----
drop table if exists best_pizza_restaurants;

-----Creating a table for restaurant data-----
create table restaurant (
             id varchar(30) primary key,
	         name varchar(100),
             address varchar(100) not null,
	         zip_code varchar(10) not null,
             latitude float not null,
             longitude float not null,
             city varchar(50) not null,
             state varchar(20) not null,
	         categories varchar not null,
	         price_level int ,
	         rating int
             );
			 
---Creating table for pizza data-------
create table pizza (
          id serial primary key,
          restaurant_id varchar(30) not null references restaurant (id),
	      pizza_name varchar(100) not null,
	      pizza_description varchar not null,
	      maximum_amount float not null,
	      minimum_amount float not null,
	      pizza_dates varchar not null
          );
		  


---Creating a table best pizza stores----
create table best_pizza_restaurants (
		id serial primary key,
	    restaurant_name varchar(100) not null,
	    city varchar(50) not null,
        address varchar(100),
		state varchar(20) not null,
		zip_code varchar(10),
	    price_level int ,
	    rating int
		);
		
---verifying if table exists---
SELECT * FROM restaurant;
SELECT * FROM pizza;
select * from best_pizza_restaurants;
		
		
		
