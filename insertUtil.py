import pandas as pd

# Hello there~~~!!!!
tablename = 'datacovid'
def getAttr(cols, dtype):
    attr=""
    for x in cols:
        attr += x + ' ' + dtype + ','
    attr += 'date ' + dtype
    return attr

def insert(conn):
    # Mình sẽ thực hiện insert 5 ngày đầu của tháng 3 cho bài lab này
    dt=['03-01-2022','03-02-2022','03-03-2022','03-04-2022','03-05-2022']
    counter = 1
    for d in dt:
        # Dữ liệu mình sẽ lấy từ link git thầy cung cấp trên utex
        url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + d + '.csv'
        df = pd.read_csv(url, index_col=0)
        cols = list(df.columns)
        attr = getAttr(cols, 'VARCHAR(255)')
        attr = 'id int, ' + attr
        attr += ', PRIMARY KEY (id)'
        mycursor = conn.cursor()

        mycursor.execute('CREATE TABLE IF NOT EXISTS ' + tablename +'(' + attr + ')')
        for index, row in df.iterrows():
            attr = getAttr(cols,'')
            attr = 'id, ' + attr
            vals = list()
            params = '%s, '
            for x in cols:
                params += '%s, '
                vals.append(str(row[x]))
            vals.append(d)
            vals.insert(0, counter)
            x = tuple(vals)
            params += '%s'

            query = 'INSERT INTO ' + tablename + ' (' + attr + ') ' + 'VALUES ('+params+')'
            mycursor.execute(query, x)
            print('total ' + str(counter) + ' row inserted')
            counter = counter + 1
    print('insert complete')
    conn.commit()

def select(conn):
    mycursor = conn.cursor()
    mycursor.execute('SELECT * FROM ' + tablename + ' LIMIT 100')
    res = mycursor.fetchall()
    for x in res:
        print(x)
