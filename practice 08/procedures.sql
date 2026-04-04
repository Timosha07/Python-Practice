-- Upsert
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO phonebook (name, phone) 
    VALUES (p_name, p_phone)
    ON CONFLICT (name) 
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;

--  Массовая вставка

CREATE OR REPLACE FUNCTION batch_insert_users(p_names TEXT[], p_phones TEXT[])
RETURNS TABLE(failed_name TEXT, failed_phone TEXT) AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        
        IF p_phones[i] ~ '^[0-9]+$' AND length(p_phones[i]) > 5 THEN
            INSERT INTO phonebook (name, phone) 
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (name) DO NOTHING;
        ELSE
            failed_name := p_names[i];
            failed_phone := p_phones[i];
            RETURN NEXT;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Удаление 
CREATE OR REPLACE PROCEDURE delete_record(p_target TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE name = p_target OR phone = p_target;
END;
$$;