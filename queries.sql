\echo
\echo QUERIES
\echo
\echo *******************************************************************************************************
\echo A. All boats that have been reserved at least once
\echo *******************************************************************************************************
\echo
select b.boat_name,b.cni,b.isocode_boat
from boat b inner join reservation r on b.cni = r.cni and b.isocode_boat = r.isocode_boat;

\echo
\echo *******************************************************************************************************
\echo B. All sailors that have reserved boats registered in the country 'Portugal'
\echo *******************************************************************************************************
\echo
select person_name,r.idcard, isocode_sailor
from reservation r inner join person p on r.idcard = p.idcard and r.isocode_sailor=p.isocode
where isocode_boat = (select isocode from country where country_name='Portugal');

\echo
\echo *******************************************************************************************************
\echo C. All reservations longer than 5 days
\echo *******************************************************************************************************
\echo
select *
from reservation
where end_date - start_date > 5;

\echo
\echo *******************************************************************************************************
\echo D. Name and CNI of all boats registered in 'South Africa' whose owner name ends with 'Rendeiro'
\echo *******************************************************************************************************
\echo
select boat_name, cni
from boat t
    inner join owner o on t.isocode_owner = o.isocode and t.idcard = o.idcard
    inner join person p on o.isocode = p.isocode and o.idcard = p.idcard
where isocode_boat = (select isocode from country where country_name='South Africa')
    and person_name like '%Rendeiro';