SELECT
    c.login,
    COUNT(o.id) AS orders_count
FROM couriers AS c
JOIN orders AS o
    ON o.courierId = c.id
WHERE o.inDelivery = true
GROUP BY c.login;