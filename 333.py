
import psycopg2
conn = psycopg2.connect(database="Maxim27", user="postgres",
 password="Rhumes1212", host="localhost", port=5432)
cur = conn.cursor()


cur.execute('''
 INSERT INTO temp_table (random_text)
 SELECT md5(random()::text)
 FROM generate_series(1, 100);
 ''')

cur.execute('''
 select * from temp_table;
 ''')
print(*cur.fetchall(), sep='\n')




