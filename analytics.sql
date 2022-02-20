-- 1.
select extract(year from trip_start_date) as year, extract(month from trip_start_date) as month, trip_start_date as day, count(trip_start_date)
from trip_info
--group by grouping sets ((extract(year from trip_start_date)), (extract(month from trip_start_date)), (trip_start_date))
group by grouping sets ((extract(year from trip_start_date)), (extract(month from trip_start_date)), (trip_start_date))
order by extract(year from trip_start_date), extract(month from trip_start_date), trip_start_date;

-- 2.
select country_name_origin, loc_name_origin, count((country_name_origin,loc_name_origin))
from trip_info
group by rollup (country_name_origin,loc_name_origin)
order by country_name_origin,loc_name_origin;