import psycopg2 as pg
import psycopg2.extras
import json

conn = pg.connect(database='insider_ideas_dev')
psycopg2.extras.register_hstore(conn)

def save_prediction(data):
    with conn.cursor() as cur:
        sql = """
        INSERT INTO predictions
        (c1, c2, c3)
        VALUES
        (%s, %s, %s)
        """
        cur.execute(sql, tuple(data.values()))
        conn.commit()

def mini_batches(batch_size=100):
    #with conn.cursor('batches') as cur:
    with conn.cursor(name = 'batches', cursor_factory = psycopg2.extras.RealDictCursor) as cur:
        sql = """
        SELECT
          plus_3_months_price - day_traded_price as price_change,
          document
        FROM
          form4s
        WHERE
          day_traded_price IS NOT NULL
        AND
          plus_3_months_price IS NOT NULL
        """
        cur.execute(sql)

        while True:
            batch = cur.fetchmany(batch_size)
            if not batch:
                break
            yield batch

def top_predictions(num=10):
    with conn.cursor() as cur:
        sql = """
        SELECT *
        FROM predictions
        ORDER BY predicted_return DESC
        LIMIT %s
        """
        #cur.execute(sql, (num,))
        return [{'id': 22, 'return': 33}]

