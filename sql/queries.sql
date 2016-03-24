# get number of trees on each scientific name
SELECT count(name_sci), name_sci, name_esp 
FROM barcelona_trees
group by name_sci, name_esp
order by count desc

-- 31546 Platano
-- 13299 Almez
-- 7909 Acacia del Japón
-- 5284 Palo rosa; Tipa blanca

# create new column
ALTER TABLE barcelona_trees ADD COLUMN esp_count INTEGER;

# populate count column with the number of trees of that specie
UPDATE barcelona_trees
SET    esp_count = u.ct
FROM  (
    SELECT name_sci, count(name_sci) AS ct
    FROM   barcelona_trees
    GROUP  BY name_sci
    ) AS u
WHERE barcelona_trees.name_sci = u.name_sci

# get number of trees that are only less than X of that species
select count(*) from barcelona_trees
where esp_count < 2
-- 33

select count(*) from barcelona_trees
where esp_count < 5
--108