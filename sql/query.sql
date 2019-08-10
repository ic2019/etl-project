----Querying restaurant table----
select * from restaurant limit 5;

---Querying for top rated restaurants from each state-----
select name, max(rating), state 
          from restaurant
		  group by state, name, rating
		  order by rating desc limit 50;
		  
---Querying pizza table ---
select * from pizza limit 5;

---Querying distinct pizzas available from Datafinty stores---
select distinct(pizza_name)
		from pizza;

---How many pizza restaurants are available in each states for Datafinity stores?---
select state, count(name) as "store count per state"
		from restaurant
		group by state
		order by "store count per state" desc;


