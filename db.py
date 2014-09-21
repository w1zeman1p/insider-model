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
          plus_3_months_price,
          plus_6_months_price,
          plus_12_months_price,
          day_traded_price,
          day_traded_volume,
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
            yield map(extract_features, batch)

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

def extract_features(tpl):
    plus_3_months_price = tpl['plus_3_months_price']
    day_traded_price = tpl['day_traded_price']
    price_change_diff = plus_3_months_price - day_traded_price
    if price_change_diff > 0.10:
        price_change = 1
    else:
        price_change = 0

    day_traded_volume = tpl['day_traded_volume']
    plus_12_months_price = tpl['plus_12_months_price']

    document = json.loads(tpl['document']['d'])
    sum_shares = document['sum_shares']
    sum_shares_after = document['sum_shares_after']

    # title
    is_director = 1 if document['is_director'] else 0
    is_officer = 1 if document['is_officer'] else 0
    is_ten_percent_owner = 1 if document['is_ten_percent_owner'] else 0
    is_other = 1 if document['is_other'] else 0

    # it would be cool to do some natural language processing here:
    # officer_title = document['officer_title']

    # transaction code percentages
    per_code_p = document['per_code_p']
    per_code_s = document['per_code_s']
    per_code_v = document['per_code_v']
    per_code_a = document['per_code_a']
    per_code_d = document['per_code_d']
    per_code_f = document['per_code_f']
    per_code_i = document['per_code_i']
    per_code_m = document['per_code_m']
    per_code_c = document['per_code_c']
    per_code_e = document['per_code_e']
    per_code_h = document['per_code_h']
    per_code_o = document['per_code_o']
    per_code_x = document['per_code_x']
    per_code_g = document['per_code_g']
    per_code_l = document['per_code_l']
    per_code_w = document['per_code_w']
    per_code_z = document['per_code_z']
    per_code_j = document['per_code_j']
    per_code_k = document['per_code_k']
    per_code_u = document['per_code_u']

    return (price_change,
            sum_shares,
            sum_shares_after,
            day_traded_volume,
            day_traded_price,
            is_officer,
            is_director,
            is_ten_percent_owner,
            is_other,
            per_code_p,
            per_code_s,
            per_code_v,
            per_code_a,
            per_code_d,
            per_code_f,
            per_code_i,
            per_code_m,
            per_code_c,
            per_code_e,
            per_code_h,
            per_code_o,
            per_code_x,
            per_code_g,
            per_code_l,
            per_code_w,
            per_code_z,
            per_code_j,
            per_code_k,
            per_code_u)
