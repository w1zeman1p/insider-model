require 'rest_client'

filing = {
  sum_shares: -200,
  sum_shares_after: 200,
  day_traded_volume: 200,
  day_traded_price: 200,
  is_officer: 0,
  is_director: 0,
  is_ten_percent_owner: 1,
  is_other: 0,
  per_code_p: 0,
  per_code_s: 100,
  per_code_v: 0,
  per_code_a: 0,
  per_code_d: 0,
  per_code_f: 0,
  per_code_i: 0,
  per_code_m: 0,
  per_code_c: 0,
  per_code_e: 0,
  per_code_h: 0,
  per_code_o: 0,
  per_code_x: 0,
  per_code_g: 0,
  per_code_l: 0,
  per_code_w: 0,
  per_code_z: 0,
  per_code_j: 0,
  per_code_k: 0,
  per_code_u: 0
}

puts RestClient.post(
  'http://localhost:8765/predict',
  filing.to_json,
  content_type: :json,
  accept: :json
).body
