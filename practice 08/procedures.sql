
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    INSERT INTO phonebook (name, number) 
    VALUES (p_name, p_phone)
    ON CONFLICT (name) DO UPDATE 
    SET number = EXCLUDED.number;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_many_contacts(p_names VARCHAR[], p_phones VARCHAR[])
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_upper(p_names, 1) LOOP

        IF length(p_phones[i]) >= 5 THEN
            INSERT INTO phonebook (name, number) VALUES (p_names[i], p_phones[i])
            ON CONFLICT (name) DO NOTHING;
        ELSE
            RAISE NOTICE 'Invalid phone for user %: %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 5. Удаление по имени или номеру
CREATE OR REPLACE PROCEDURE delete_contact(p_target VARCHAR)
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE name = p_target OR number = p_target;
END;
$$ LANGUAGE plpgsql;