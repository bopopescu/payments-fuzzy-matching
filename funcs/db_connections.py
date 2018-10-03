import pandas as pd, mysql.connector

def fetch_name_sql(acc_num, sort_code):
    
    #Datasource addresse
    source = mysql.connector.connect(user='dbmaster', password='dbmaster',
                              host='t2micro-testdb.cxjtbapssbv8.eu-west-1.rds.amazonaws.com',
                              database='test_db1')
                              
    sort_code = str(sort_code.replace('-', ''))
    
    query = "SELECT CustName FROM test_db1.sample_payments_data WHERE (SortCode = '" + sort_code + "' AND AccNumber = '" + acc_num + "')"

    cursor = source.cursor()
    cursor.execute(query)
    result_df = pd.DataFrame(cursor.fetchall())
    
    return result_df