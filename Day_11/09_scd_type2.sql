UPDATE dim_customer

SET

end_date=CURRENT_DATE,

current_flag='N'

WHERE customer_id=2

AND current_flag='Y';