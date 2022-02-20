-- TRIGGERS to ensure the app functions properly

-- verify if new sailor/owner is already is person before inserting
CREATE OR REPLACE FUNCTION chk_person_proc() RETURNS TRIGGER AS
$$
BEGIN
    IF (NEW.id,NEW.iso_code) IN (SELECT id,iso_code FROM person) THEN
        RETURN NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_person ON person;
CREATE TRIGGER chk_person
BEFORE INSERT ON person
FOR EACH ROW EXECUTE PROCEDURE chk_person_proc();

-- verify if sailor is also owner before deleting
CREATE OR REPLACE FUNCTION chk_sailor_del_proc() RETURNS TRIGGER AS
$$
BEGIN
    IF (OLD.id,OLD.iso_code) NOT IN (SELECT id,iso_code FROM owner) THEN --not owner
        DELETE FROM person WHERE id=OLD.id AND iso_code=OLD.iso_code;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_sailor_del ON sailor;
CREATE TRIGGER chk_sailor_del
AFTER DELETE ON sailor
FOR EACH ROW EXECUTE PROCEDURE chk_sailor_del_proc();

-- verify if owner is also sailor before deleting
CREATE OR REPLACE FUNCTION chk_owner_del_proc() RETURNS TRIGGER AS
$$
BEGIN
    IF (OLD.id,OLD.iso_code) NOT IN (SELECT id,iso_code FROM sailor) THEN --not sailor
        DELETE FROM person WHERE id=OLD.id AND iso_code=OLD.iso_code;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_owner_del ON owner;
CREATE TRIGGER chk_owner_del
AFTER DELETE ON owner
FOR EACH ROW EXECUTE PROCEDURE chk_owner_del_proc();

-- check if schedule is already present when adding reservation
CREATE OR REPLACE FUNCTION chk_sch_proc() RETURNS TRIGGER AS
$$
BEGIN
    IF (NEW.start_date,NEW.end_date) IN (SELECT start_date,end_date FROM schedule) THEN
        RETURN NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS chk_sch ON schedule;
CREATE TRIGGER chk_sch
BEFORE INSERT ON schedule
FOR EACH ROW EXECUTE PROCEDURE chk_sch_proc();

-- delete schedule when deleting reservation
CREATE OR REPLACE FUNCTION del_sch_proc() RETURNS TRIGGER AS
$$
BEGIN
    IF (SELECT count((new.start_date,new.end_date)) FROM reservation)>0 THEN
        RETURN NULL;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS del_sch ON reservation;
CREATE TRIGGER del_sch
BEFORE DELETE ON schedule
FOR EACH ROW EXECUTE PROCEDURE del_sch_proc();
