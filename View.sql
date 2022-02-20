drop view if exists trip_info;

create view trip_info(country_iso_origin,country_name_origin,country_iso_dest,country_name_dest,loc_name_origin,
    loc_name_dest,cni_boat,country_iso_boat, country_name_boat,trip_start_date) as
select country_iso_origin,country_name_origin,country_iso_dest,country_name_dest,loc_name_origin,
       loc_name_dest,cni_boat,country_iso_boat, country_name_boat,trip_start_date
from (select c1.iso_code as country_iso_origin, c1.name as country_name_origin,
             l1.name as loc_name_origin, t.date as trip_start_date,
             c2.iso_code as country_iso_dest, c2.name as country_name_dest,
             l2.name as loc_name_dest, b.cni as cni_boat, b.iso_code as country_iso_boat,
             c.name as country_name_boat
        from ((country c1 join location l1 on c1.iso_code = l1.iso_code)
        join trip t on t.start_latitude = l1.latitude and t.start_longitude = l1.longitude
        join (country c2 join location l2 on c2.iso_code = l2.iso_code)
            on t.end_latitude = l2.latitude and t.end_longitude = l2.longitude
        join (boat b join country c on b.iso_code = c.iso_code) on t.iso_code_boat = b.iso_code and t.cni = b.cni)) as data;

