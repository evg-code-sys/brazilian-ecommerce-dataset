# **brazilian-ecommerce-dataset**
Данный репозиторий хранит аналитические действия с датасетом _"Brazilian E-Commerce Public Dataset by Olist"_

![Brazilian E-Commerce Public Dataset by Olist](https://i.imgur.com/HRhd2Y0.png)

# **Структура данных:**
1. Olist_customers_dataset.csv -- _"customer_id"_ --> Olist_orders_dataset.csv;
2. Olist_orders_dataset.csv <-- _"order_id"_ --> Olist_orders_dataset.csv <-- _"order_id"_ --> Olist_order_reviews_dataset.csv;
3. Olist_order_items.csv -- _ "product_id"_ -> Olist_products_dataset.csv.