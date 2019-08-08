----Creating pizza_db database----
create database pizza_db

-----Creating a table for restaurant data-----
create table restaurant (
             id varchar(30) primary key,
	         name varchar(30),
             address varchar(100) not null,
	         zip_code int not null,
             latitude float not null,
             longitude float not null,
             city varchar(30) not null,
             state varchar(20) not null,
	         categories text[] not null,
	         price_level int ,
	         rating int
             )
			 
---Creating table for pizza data-------
---ndex(['restaurant_id', 'pizza_name', 'pizza_description', 'maximum_amount',
       'minimum_amount', 'pizza_seen_dates'],
create table pizza (
          id serial primary key,
          restaurant_id varchar(30) not null,
	      pizza_name varchar(50) not null,
	      pizza_description varchar(100) not null,
	      maximum_amount float not null,
	      minimum_amount float not null
          )
		  
---Creating a table for other pizza details----
create table pizza_det (
		id serial primary key,
	    pizza_name varchar(50) not null,
        pizza_seen_date date not null)