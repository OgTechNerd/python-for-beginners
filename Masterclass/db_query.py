
import pyodbc
from prettytable import PrettyTable
from datetime import date
import re
import argparse

driver = '{ODBC Driver 13 for SQL Server}'
sql_server = '10.16.51.196'
sql_port = 1433
sql_database = ['SLDATEN']
sql_username = 'sa'
sql_password = 'cbj2dlYW2P90Ln*'


def establish_connection(rsslist, tenant):
    for db in sql_database:
        print('Attempting Connection...')
        conn_str = (
            r'DRIVER=%s;' % driver +
            r'SERVER=%s;' % sql_server +
            r'DATABASE=%s;' % db +
            r'UID=%s;' % sql_username +
            r'PWD=%s;' % sql_password
        )
        print(conn_str)
        conn = pyodbc.connect(conn_str)

        print('Connected!!!')
        print(rsslist)
        print(tenant)
        #dbquery(conn, db, rsslist, tenant)
        conn.close()

def dbquery(conn, db, rsslist, tenant):
    print("Executing the query")
    for item in rsslist:
        cursor = conn.cursor()
        query = """ select * from [db].[CLIENT].[GWGIKUND] where KD_SP_01=rssid """

        query_with_tenantid = re.sub("db", tenant, query)
        query_with_rssid_and_tenantid =  re.sub("rssid", item, query_with_tenantid)
        print(query)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script gets the RSS IDS from the Database for Customer")
    parser.add_argument( "-r", "--rssid", help=" provide rssid", type=str, nargs='+')
    parser.add_argument( "-t", "--tenantid", help=" provide tenantid", type=int)
    args = parser.parse_args()