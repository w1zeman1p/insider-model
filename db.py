import psycopg2 as pg

conn = pg.connect(database='insider_ideas_dev')

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
    with conn.cursor('batches') as cur:
        sql = """
        SELECT id, day_traded_price - plus_3_months_price as price_change
        FROM form4s
        WHERE day_traded_price IS NOT NULL
        AND plus_3_months_price IS NOT NULL
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

