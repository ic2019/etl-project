----Querying restaurant table----
select * from restaurant limit 5;

---Querying pizza table ---
select * from pizza limit 5;

---Querying for top rated restaurants from each state-----
select name, max(rating), state 
          from restaurant
		  group by state, name, rating
		  order by rating desc limit 50;
		  
---Querying distinct pizzas available from Datafinty stores---
select distinct(pizza_name)
		from pizza;

---How many pizza restaurants are available in each states for Datafinity stores?---
select state, count(name) as "store count per state"
		from restaurant
		group by state
		order by "store count per state" desc;

------ Which is the cheapest type of pizza sold in Datafinity stores by store names?-------
select r.name, min(p.minimum_amount) as "Cheapest Price"
        from restaurant r
		inner join pizza p
		on r.id = p.restaurant_id
		group by r.name
		order by "Cheapest Price" ;
		
-----Which is the most expensive pizza sold in Datafinity stores?------
select r.name, min(p.minimum_amount) as "Max Price"
        from restaurant r
		inner join pizza p
		on r.id = p.restaurant_id
		group by r.name
		order by "Max Price" desc;
		
-----Which state has the maximum number of pizza restaurants? (Top 5)-----
select state, count(state) as "count of restaurants"
        from restaurant r
		group by state
		order by "count of restaurants" desc limit 5;

------ Which is the most popular pizza by state?-------
select r.state, p.pizza_name, count(pizza_name) as count
       from restaurant r
	   left join pizza p
	   on r.id = p.restaurant_id
	   group by r.state, p.pizza_name
	   order by count desc limit 10;

------ Which all restaurant offer vegg pizzas based on description?-----
select distinct(r.name), p.pizza_name, r.city, r.state
       from restaurant r
	   left join pizza p
	   on r.id = p.restaurant_id
	   where p.pizza_description like '%veg%' 
	   AND r.name <> '-NA-' 
	   limit 5;
	   
-----Which are the top rated restaurants by rating?------
select name, rating
     from restaurant
	 order by rating desc limit 5;
	   

		


