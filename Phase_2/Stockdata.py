import requests
from datetime import datetime
import time
from_date=input('enter the start date yyyy/mm/dd')
end_date=input('enter the end date yyyy/mm/dd')
st=datetime.strptime(from_date, '%Y/%m/%d')
et=datetime.strptime(end_date, '%Y/%m/%d')
p1=time.mktime(st.timetuple())
p2=time.mktime(et.timetuple())
#p2=datetime.datetime(int(et[0]),int(et[1]),int(et[2])).timestamp()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url=f'https://query1.finance.yahoo.com/v7/finance/download/TCS.BO?period1={int(p1)}&period2={int(p2)}&interval=1d&events=history&includeAdjustedClose=true';
content=requests.get(url,headers=headers).content
#print(content)
with open('D:\stock1.csv','wb') as f:
    f.write(content)