import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password="")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

cursor.execute("SELECT * FROM sabana_datos")
data = cursor.fetchall()
cabecera = ['employee_id',
'last_name',
'first_name',
'title',
'reports_to',
'birth_date',
'hire_date',
'address',
'city',
'state',
'country',
'postal_code',
'phone',
'fax',
'email',
'c_customer_id',
'c_first_name',
'c_last_name',
'c_company',
'c_address',
'c_city',
'c_state',
'c_country',
'c_postal_code',
'c_phone',
'c_fax',
'c_email',
'support_rep_id',
'invoice_id',
'customer_id',
'invoice_date',
'billing_address',
'billing_city',
'billing_state',
'billing_country',
'billing_postal_code',
'total',
'track_id',
'name',
'album_id',
'media_type_id',
'genre_id',
'composer',
'milliseconds',
'bytes',
't_unit_price']

dataf = pd.DataFrame(data)
dataf.to_csv('sabana_datos.csv', header=cabecera)

#Closing the connection
conn.close()