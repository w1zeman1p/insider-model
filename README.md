# Insider AI Model

## form4s table:
'''
id
cik
title
link
term
date
file_id
created_at
updated_at
ticker
company_id
document
day_traded_price
plus_3_months_price
plus_6_months_price
plus_12_months_price
day_traded_volume
day_traded_market_cap
insider_id
'''

## form4s#document:

The document data is stored as an hstore column that looks like this

{"d":
  {"schema_version"=>"X0202",
   "document_type"=>"4",
   "period_of_report"=>"2006-06-09",
   "not_subject_to_section_16"=>false,
   "issuer_name"=>"SEATTLE GENETICS INC /WA",
   "issuer_cik"=>"0001060736",
   "issuer_trading_symbol"=>"SGEN",
   "owner_cik"=>"000131749300010879390001087940",
   "owner_name"=>"14159 capital (GP), LLCBAKER JULIANBAKER FELIX",
   "owner_address"=>
    {"street1"=>"667 MADISON AVE667 MADISON AVENUE667 MADISON AVENUE",
     "street2"=>"17TH FL",
     "city"=>"NEW YORKNEW YORKNEW YORK",
     "state"=>"NYNYNY",
     "zip"=>"100211002110021",
     "state_description"=>""},
   "is_director"=>false,
   "is_officer"=>false,
   "is_ten_percent_owner"=>false,
   "is_other"=>false,
   "officer_title"=>"",
   "transactions"=>
    [{"acquired_or_disposed_code"=>"A",
      "nature_of_ownership"=>"See footnote",
      "code"=>"P",
      "shares"=>1162.0,
      "security_title"=>"Common Stock",
      "direct_or_indirect_code"=>"I",
      "form_type"=>"4",
      "equity_swap_involved"=>false,
      "transaction_date"=>"2006-06-09",
      "shares_after"=>38953.0,
      "price_per_share"=>4.11},
     {"acquired_or_disposed_code"=>"A",
      "nature_of_ownership"=>"See footnote",
      "code"=>"P",
      "shares"=>30035.0,
      "security_title"=>"Common Stock",
      "direct_or_indirect_code"=>"I",
      "form_type"=>"4",
      "equity_swap_involved"=>false,
      "transaction_date"=>"2006-06-09",
      "shares_after"=>68988.0,
      "price_per_share"=>4.0},
     {"acquired_or_disposed_code"=>"A",
      "nature_of_ownership"=>"See footnote",
      "code"=>"P",
      "shares"=>399.0,
      "security_title"=>"Common Stock",
      "direct_or_indirect_code"=>"I",
      "form_type"=>"4",
      "equity_swap_involved"=>false,
      "transaction_date"=>"2006-06-13",
      "shares_after"=>69387.0,
      "price_per_share"=>3.9},
     {"acquired_or_disposed_code"=>"A",
      "nature_of_ownership"=>"See footnote",
      "code"=>"P",
      "shares"=>852.0,
      "security_title"=>"Common Stock",
      "direct_or_indirect_code"=>"I",
      "form_type"=>"4",
      "equity_swap_involved"=>false,
      "transaction_date"=>"2006-06-13",
      "shares_after"=>70239.0,
      "price_per_share"=>4.0161},
     {"acquired_or_disposed_code"=>"A",
      "nature_of_ownership"=>"See footnote",
      "code"=>"P",
      "shares"=>630.0,
      "security_title"=>"Common Stock",
      "direct_or_indirect_code"=>"I",
      "form_type"=>"4",
      "equity_swap_involved"=>false,
      "transaction_date"=>"2006-06-13",
      "shares_after"=>70869.0,
      "price_per_share"=>4.0445}],
   "derivative_transactions"=>[],
   "sum_shares"=>33078.0,
   "sum_shares_after"=>70869.0,
   "per_code_p"=>100.0,
   "per_code_s"=>0,
   "per_code_v"=>0,
   "per_code_a"=>0,
   "per_code_d"=>0,
   "per_code_f"=>0,
   "per_code_i"=>0,
   "per_code_m"=>0,
   "per_code_c"=>0,
   "per_code_e"=>0,
   "per_code_h"=>0,
   "per_code_o"=>0,
   "per_code_x"=>0,
   "per_code_g"=>0,
   "per_code_l"=>0,
   "per_code_w"=>0,
   "per_code_z"=>0,
   "per_code_j"=>0,
   "per_code_k"=>0,
   "per_code_u"=>0}
}
