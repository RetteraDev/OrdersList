-- Запрос создает таблицу orders
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    order_number INT NOT NULL UNIQUE NOT NULL,
    cost INT NOT NULL,
    delivery_date DATE NOT NULL
);
