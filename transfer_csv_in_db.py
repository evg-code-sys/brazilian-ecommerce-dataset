import os
import kagglehub
import pandas as pd
import sqlite3

'''
Переобразуем csv файлы в базу данных на основе sqlite3, для демонстрирование знаний SQL.

Примечание: В базе данных нет ещё 4 файла из датасета "Brazilian E-Commerce Public Dataset by Olist" (Используется в проекте: 5/9 csv файлов)
'''

NAME_DB = 'olist_brazilian.db'
DATASET_NAME = 'olistbr/brazilian-ecommerce' 

# Функция превращает csv файлы в таблицы для базы данных 'olist_brazilian.db'
def create_simple_db() -> str:
    conn = sqlite3.connect(NAME_DB)
    
    try:
        # Путь к скачанным файлам с сайта https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data?select=olist_customers_dataset.csv
        path = kagglehub.dataset_download(DATASET_NAME) 

        csv_files = [
            'olist_customers_dataset.csv',
            'olist_orders_dataset.csv',
            'olist_order_items_dataset.csv',
            'olist_products_dataset.csv',
            'olist_order_reviews_dataset.csv'
        ]
        
        for file in csv_files:
            file_path = os.path.join(path, file)

            # Проверка пути -> Если путь соответствует, тогда записываем таблицу в базу, иначе выводим соответсвующее сообщение
            if os.path.exists(file_path):
                table_name = file.replace('.csv', '')

                df = pd.read_csv(file_path)
                pd.read_csv(file_path).to_sql(table_name, conn, if_exists='replace', index=False)

                print(f'Таблица {table_name} загружена ({len(df)} строк)')

            else:
                print(f'Файл {file} не найден')
        
        return f'\nБаза данных {NAME_DB} успешно создана.'
    
    except Exception as e:
        return f'Ошибка: {e}'
    
    finally:
        conn.close()


if __name__ == '__main__':
    print(create_simple_db())