SELECT developer_name, COUNT(*) AS total_projects
FROM luxury_housing
GROUP BY developer_name
ORDER BY total_projects DESC;

SELECT configuration, COUNT(*) AS total_units
FROM luxury_housing
GROUP BY configuration;

SELECT micro_market, COUNT(*) AS total_projects
FROM luxury_housing
GROUP BY micro_market;