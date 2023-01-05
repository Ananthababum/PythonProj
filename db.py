import pyodbc 
import pandas as pd
from sqlalchemy import create_engine



# prodconn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=10.0.161.100,3242;'
#                       'Database=misdb;'
#                       'UID=misreportuser;' 
#                       'PWD=nmsdflnmsflg0217$;'
#                       )
                      

testconn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=HPLAPCHN045\SSISSQLSERVERMDX;'
                      'Database=testdb;'
                      'Trusted_Connection=yes;'
                    #   'UID=rvwuser;' 
                    #   'PWD=rvw;'
                      )   




cursor = testconn.cursor()
fetchdata = cursor.execute('SELECT * FROM test')

for row in fetchdata:
    print(row)

# df = pd.DataFrame(fetchdata,columns=['Emp Id','Emp Name','Empd Addr','Emp Mobile'])
# # df.to_csv('out.csv')
# # print(df)
# df.head()

# for data in fetchdata:
#     print(data)

# records = cursor.fetchall()

# print(len(records))


# print(records)


