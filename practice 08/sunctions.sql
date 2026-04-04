-- 1. Поиск по паттерну
CREATE OR REPLACE FUNCTION search_records(p_pattern TEXT)
RETURNS SETOF phonebook AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    WHERE name ILIKE '%' || p_pattern || '%' 
       OR surname ILIKE '%' || p_pattern || '%' 
       OR phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Пагинация
CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INT, p_offset INT)
RETURNS SETOF phonebook AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    ORDER BY id 
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;