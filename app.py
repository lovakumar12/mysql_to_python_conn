import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:admin@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']

for file in files:
    df = pd.read_csv(f'/Users/thoufiq/THOUFIQ/techTFQ/YouTube/VIDEOS/SQL Queries/SQL Case Studies - Datasets/Famous Paintings/Dataset/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)