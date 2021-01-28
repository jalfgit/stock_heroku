select strftime("%m",date) "month",avg($SYMBOL) "AVG_PRICE"  
from $SYMBOL 
group by month  
order by 1 asc 
limit $n
