select date(date) "date",$SYMBOL, volume 
from $SYMBOL 
order by 1 desc 
limit $n
