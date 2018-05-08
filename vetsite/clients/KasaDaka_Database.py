import sqlalchemy
import pandas as pd

#Database details
user = 'postgres'
password = '123@abc'
db = 'KasaDaka'
host='127.0.0.1'
port=5432

#Function: Connection and Metadata
def connect(user, password, db, host, port):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://postgres:123@abc@127.0.0.1:5432/KasaDaka
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

#Connect to database
#con = create_engine('postgresql://postgres:123@abc@127.0.0.1:5432/KasaDaka')
con, meta = connect(user, password, db, host, port)


# Function: List all database tables
def tables(connection):
    table_names = connection.table_names()
    for table in table_names:
        print(table)


# Fuction: retrieve data from query
def query(query):
    qlist = []
    rs = con.execute(query)

    fa = rs.fetchall()
    #for key in rs.keys():
    for count, row in enumerate(fa):
        for count2, column in enumerate(row):
            qlist.append(str(rs.keys()[count2]) + ":  " + str(fa[count][count2]))
    return qlist


# Function: Query to DataFrame
def query_df(query):
    # Execute query
    rs = con.execute(query)
    # Query results, and export to DataFrame
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    # Close query
    rs.close()
    # DataFrame with query results
    return df