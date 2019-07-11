@@ -0,0 +1,56 @@
import pyodbc
from prettytable import PrettyTable
from datetime import date
import re
import argparse
from tabulate import tabulate

driver = '{ODBC Driver 13 for SQL Server}'
sql_server = '10.10.50.169'
sql_port = 1433
sql_database = 'AML_HB01'
sql_username = 'sa'
sql_password = 'cbj2dlYW2P90LnDUZraR+'


def establish_connection(rssid_list, tenantid):
        print('Attempting Connection...')
        conn_str = (
            r'DRIVER=%s;' % driver +
            r'SERVER=%s;' % sql_server +
            r'DATABASE=%s;' % sql_database +
            r'UID=%s;' % sql_username +
            r'PWD=%s;' % sql_password
        )
        print(conn_str)
        conn = pyodbc.connect(conn_str)
        print('Db Connected!!!')
        dbquery(conn, rssid_list, tenantid)
        conn.close()

def dbquery(conn, rssid_list, tenantid):
    print("Executing the Query ")
    for item in rssid_list:
        cursor = conn.cursor()
        query = """select  KD_SP_01, INSTITUTSNR, KUNDNR, LIEFERDAT ,KD_SP_10 ,KD_SP_13 ,KD_SP_17 ,KD_SP_19 ,KD_SP_21 ,KD_SP_27
                from [db].[CLIENT].[GWGIKUND] where KD_SP_01='rssid'"""
        query_with_tenantid = re.sub("db", tenantid, query)
        query_with_rssid_and_tenantid =  re.sub("rssid", item, query_with_tenantid)
        #print(query_with_rssid_and_tenantid)
        cursor.execute(query_with_rssid_and_tenantid)
        for row in cursor:
            print("\n")
            print tabulate([list(row)], headers=['RSS_ID', 'INSTITUTE NO', 'CUSTOMERNO', 'DELIVERYDATE', 'KD_10', 'KD_13', 'NameID', 'KD_19', 'KD_21', 'KD_27'], tablefmt='orgtbl')
            print("\n")
        cursor.close()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script gets the RSS IDS from the Database for Customer")
    parser.add_argument( "-r", "--rssid", help="provide rssid", type=str, nargs='+')
    parser.add_argument( "-t", "--tenantid", help="provide tenantid", type=int)
    args = parser.parse_args()
    tenantid = "AML_HB"+str(args.tenantid)
    establish_connection(args.rssid, tenantid)