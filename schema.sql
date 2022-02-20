/*************
  DROP ALL THE TABLES OF THE DATABASE
 **************/
drop table if exists person,sailor,owner,country,boat,boatwithvhf,trip,location,port,wharf,marina,schedule,reservation cascade;

/*************
  CREATION OF ALL THE TABLES OF THE DATABASE
 **************/


-- Country
create table country(
    isocode varchar(3),
    country_name varchar(70) not null,
    flag varchar(2083) not null,
    primary key (isocode),
    unique(country_name),
    unique(flag),
    check (isocode not similar to '%[0-9]%')
);

-- Person
create table person(
    idcard integer,
    person_name varchar(80) not null,
    isocode varchar(3),
    primary key(idcard, isocode),
    foreign key(isocode) references country(isocode),
    check(idcard>0)
    --every person must be in either table sailor or/and owner
);

create table sailor(
    idcard integer,
    isocode varchar(3),
    primary key(isocode,idcard),
    foreign key(isocode,idcard) references person(isocode,idcard)
);

create table owner(
    idcard integer,
    isocode varchar(3),
    birthdate date not null,
    primary key(isocode,idcard),
    foreign key(isocode,idcard) references person(isocode,idcard)
    --every owner must have a boat
);

-- Boat
create table boat(
    isocode_boat varchar(3),
    cni integer,
    year numeric(4,0) not null,
    length integer not null,
    boat_name varchar(80) not null,
    isocode_owner varchar(3) not null,
    idcard integer not null,
    primary key(isocode_boat,cni),
    foreign key (isocode_boat) references country(isocode),
    foreign key (isocode_owner,idcard) references owner(isocode,idcard),
    check (length>0),
    check (year>0),
    check (cni>0)
);

create table boatwithvhf(
    isocode varchar(3),
    cni integer,
    mmsi varchar(9) not null,
    primary key(isocode,cni),
    foreign key (isocode,cni) references boat(isocode_boat,cni)
);

-- Location
create table location(
    latitude numeric(8,6),
    longitude numeric(9,6),
    name varchar(80) not null,
    isocode varchar(3) not null,
    primary key(latitude, longitude),
    foreign key (isocode) references country(isocode)
    -- two locations must be at least 1 mile apart
    -- Every location must exist in one of the following tables: 'marina', 'wharf', 'port'
    -- No location can exist at the same time in two of the following tables: 'marina', 'wharf', 'port'
);

create table marina(
    latitude numeric(8,6),
    longitude numeric(9,6),
    primary key(latitude, longitude),
    foreign key(latitude,longitude) references location(latitude,longitude)
);

create table wharf(
    latitude numeric(8,6),
    longitude numeric(9,6),
    primary key(latitude, longitude),
    foreign key(latitude,longitude) references location(latitude,longitude)
);

create table port(
    latitude numeric(8,6),
    longitude numeric(9,6),
    primary key(latitude, longitude),
    foreign key(latitude,longitude) references location(latitude,longitude)
);


-- Schedule
create table schedule(
    start_date date,
    end_date date,
    primary key(start_date, end_date),
    check (end_date > start_date)
);

-- Reservation
create table reservation(
    isocode_boat varchar(3),
    cni integer,
    isocode_sailor varchar(3),
    idcard integer,
    start_date date,
    end_date date,
    primary key  (isocode_boat,cni, isocode_sailor, idcard, start_date, end_date),
    foreign key (isocode_boat,cni) references boat(isocode_boat,cni),
    foreign key (isocode_sailor,idcard) references sailor(isocode,idcard),
    foreign key (start_date,end_date) references schedule(start_date,end_date)
    --Reservation schedules of a boat must not overlap
);

create table trip(
    date date,
    duration interval not null,
    isocode_boat varchar(3),
    cni integer,
    isocode_sailor varchar(3),
    idcard integer,
    start_date date,
    end_date date,
    from_latitude numeric(8,6) not null,
    from_longitude numeric(9,6) not null,
    to_latitude numeric(8,6) not null,
    to_longitude numeric(9,6) not null,
    primary key (isocode_boat, cni, isocode_sailor, idcard,start_date,end_date, date),
    foreign key (isocode_boat,cni,isocode_sailor,idcard,start_date,end_date) references reservation(isocode_boat,cni,isocode_sailor,idcard,start_date,end_date),
    foreign key (from_latitude,from_longitude) references location(latitude,longitude),
    foreign key (to_latitude,to_longitude) references location(latitude,longitude),
    check (duration > interval '0 seconds'),
    check (date+duration <= end_date),
    check (date >= start_date and date <= end_date)
    --Trips for one reservation of a boat must not overlap
);



