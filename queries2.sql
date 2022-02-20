-- Queries
-- 1. Who is the owner with the most boats per country?
select id_owner, iso_code_owner, iso_code, nboats
from (select id_owner, iso_code_owner, iso_code, count((cni,iso_code)) as nboats
    from boat
    group by id_owner, iso_code_owner, iso_code order by iso_code) f
where nboats>= all(select nboats2
    from (select id_owner, iso_code_owner, iso_code, count((cni,iso_code)) as nboats2
    from boat
    group by id_owner, iso_code_owner, iso_code order by iso_code) f2
    where f2.iso_code=f.iso_code
    );

-- 2. List all the owners that have at least two boats in distinct countries.
select distinct id_owner, iso_code_owner, count(distinct iso_code) as ncountry
from boat
group by id_owner, iso_code_owner
having count(distinct iso_code) > 1;

-- 3. Who are the sailors that have sailed to every location in 'Portugal'?
-- JUSTIFICAR entre PT ou Portugal + ir buscar info as trip em vez de ao sailor (pq a trip tem os sailors que sailam, e nao todos)
select distinct s.id_sailor, s.iso_code_sailor
from trip s
where not exists (
    (select latitude,longitude
    from location l
    where l.iso_code = (select iso_code from country where name='Portugal'))
    except (
        select end_latitude, end_longitude
        from trip t
        where t.id_sailor = s.id_sailor and t.iso_code_sailor = s.iso_code_sailor
));

-- 4. List the sailors with the most trips along with their reservations
select id_sailor, iso_code_sailor, cni, iso_code_boat, start_date, end_date, count((date, cni, iso_code_boat, id_sailor, iso_code_sailor, start_date, end_date)) as ntrips
from trip
group by cni, iso_code_boat, id_sailor, iso_code_sailor, start_date, end_date --reservation
order by ntrips desc;

-- 5.List the sailors with the longest duration of trips (sum of trip durations) for the same single reservation;
-- display also the sum of the trip durations.
select id_sailor, iso_code_sailor, sum(duration) as sum_trip
from trip
group by cni, iso_code_boat, id_sailor, iso_code_sailor, start_date, end_date --reservation
order by sum_trip desc;

