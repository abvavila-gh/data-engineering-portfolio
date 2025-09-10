select
    customer_id,
    sum(amount) as total_sales,
    count(distinct order_id) as total_orders
from {{ ref('stg_sales') }}
group by customer_id