import pandas as pd
data_HTML = pd.read_html('http://www.mail.ru')
#data_HTML.head()
#data_HTML.info()
print(data_HTML)
data_HTML.head()