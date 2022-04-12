from yahoo_fin.stock_info import *


stock_no = '2889.TW'

data = get_data(stock_no , start_date = '1970/01/01')
data.head()
stock = pd.DataFrame.from_dict(data)
stock.to_csv(r"目錄"+stock_no+".csv")