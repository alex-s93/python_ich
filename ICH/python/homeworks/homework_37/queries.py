show_tables = "show tables;"

select_all_from_table = "select * from {table};"

get_all_users_names = "select id, name from users;"

get_sales_by_user_id = """
SELECT
    sales.sid AS order_id, product.prod AS product, product.quantity AS quantity
FROM product
         INNER JOIN sales ON product.pid = sales.pid
         INNER JOIN users ON users.id = sales.id
WHERE users.id = {id};
"""