--Integrity Constrains

--IC-1: Two reservations for the same boat can not have their corresponding date intervals intersecting.
CREATE OR REPLACE FUNCTION tg_insert_reservation_proc()
RETURNS TRIGGER AS
$$
DECLARE cursor_reservation CURSOR FOR
    SELECT * FROM reservation;
DECLARE reserva reservation%ROWTYPE;
BEGIN
    OPEN cursor_reservation;
    LOOP
        FETCH cursor_reservation INTO reserva;
        IF reserva IS NULL THEN
            EXIT;
        ELSIF (new.start_date <= reserva.end_date) AND (new.end_date >= reserva.start_date) AND reserva.iso_code_boat=new.iso_code_boat AND reserva.cni=new.cni THEN
            RAISE EXCEPTION 'Reservation_Overlap' USING HINT ='The reservation overlaps with another on the data base';
        END IF;
    END LOOP;
    CLOSE cursor_reservation;
    RETURN new;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_insert_reservation ON reservation;
CREATE TRIGGER tg_insert_reservation
BEFORE INSERT OR UPDATE ON reservation
FOR EACH ROW EXECUTE PROCEDURE tg_insert_reservation_proc();

--IC-2: Any location must be specialized in one of three - disjoint - entities: marina, wharf, or port.
CREATE OR REPLACE FUNCTION verify_location()
RETURNS TRIGGER AS
$$
BEGIN
    IF (SELECT count(*) FROM (
        SELECT latitude, longitude FROM wharf
        UNION ALL
        SELECT latitude, longitude FROM marina
        UNION ALL
        SELECT latitude, longitude FROM port) a
        WHERE latitude=new.latitude AND longitude=new.longitude
        --vai unir as 3 tabelas com os repetidos e contar os pares (lat,long) na lista e se for diferente nenhum ou nao esta (=0) ou esta em varios (erro)
        ) <> 1
        THEN
        RAISE EXCEPTION 'The location % is not specialized in only one type of location.', new.name;
    END IF;
  RETURN new;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_verify_location ON location;
CREATE CONSTRAINT TRIGGER tg_verify_location
AFTER INSERT ON location DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE verify_location();


--IC-3: A country where a boat is registered must correspond - at least - to one location.
CREATE OR REPLACE FUNCTION tg_check_country_proc()
RETURNS TRIGGER AS
$$
BEGIN
    IF (SELECT count(DISTINCT (latitude,longitude)) -- distinct is implicit since lat,long are PK --count(*)
        FROM location
        WHERE iso_code=new.iso_code)<1
    THEN
    RAISE EXCEPTION 'Country does not have at least one location';
    END IF;
RETURN new;
END ;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tg_check_country ON boat;
CREATE TRIGGER tg_check_country
BEFORE INSERT OR UPDATE ON boat
FOR EACH ROW EXECUTE PROCEDURE tg_check_country_proc();



