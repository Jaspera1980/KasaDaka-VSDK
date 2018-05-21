
# coding: utf-8

# In[2]:


import sqlalchemy

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
    # postgresql://federer:grandestslam@localhost:5432/tennis
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

"""Update disease diagnosis in database"""
#Select items from service_development_callsessionstep
q0 = con.execute("SELECT _visited_element_id, session_id FROM service_development_callsessionstep")
q1 = q0.fetchall()

#Counter of unique id's
from collections import Counter
count_list = []
for item in q1:
    count_list.append(item[1])

#Update for loop
count = 0
for item in q1:
    #Count number of same id's
    no_of_ids = count_list.count(item[1])
    #Match on session_id
    matching_id = str(item[1])
    #PK number with matching diagnosis
    disease_dict = {16:"Bursal Disease", 17:"Fowl Pox", 18:"Marek's Disease", 19:"Newcastle Disease"}
    #If pk=x then state the diagnosis
    if item[0] in disease_dict.keys():
        disease = str("'" + disease_dict[item[0]] + "'" + " ")
    #If no diagnosis is found return 'No diagnosis'
    else:
        count += 1
        if count != no_of_ids:
            print("No of iterations:",count)
            continue
        else:
            count = 0
            disease = "'No diagnosis' "
    query_stmt = "UPDATE service_development_callsession SET disease = " + disease + "WHERE id = " + matching_id
    q2 = con.execute(query_stmt)

#close connection
q0.close()
q2.close()

