-- lists all bands with Glam rock as their main style ranked by oldest
SELECT band_name, IFNULL((split), 2020) - formed AS lifespan
FROM metal_bands
WHERE INSTR(style, 'Glam rock') > 0
ORDER BY lifespan DESC;
