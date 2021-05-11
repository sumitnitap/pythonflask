# Imports for DocumentPrint modules
from DocumentManagementError import InvalidUsage
import DocumentManagementSecurity
import Constants

# Pip-installed modules
import pyodbc
import configparser
from smb.SMBConnection import SMBConnection
from smb import smb_structs

# Python in-built imports
from socket import gethostname

# Reading database connection details from file 'config.ini'
config = configparser.ConfigParser()
config.read("config.ini")
# Reading application id and secret
app_id_pwd=DocumentManagementSecurity.call_batch_for_application_id()
mssql_username=str(app_id_pwd[1])
mssql_password=str(app_id_pwd[0])
mssql_server=config['DocumentPrint']['mssql-server']
mssql_database=config['DocumentPrint']['mssql-database']
mssql_driver=config['DocumentPrint']['mssql-driver']
mssql_Trusted_Connection=config['DocumentPrint']['mssql-trusted_connection']
def db_connect():
    try:
        ms_connection = pyodbc.connect('DRIVER='+mssql_driver+
                                ';SERVER='+mssql_server+
                                ';DATABASE='+mssql_database+
                                ';UID='+mssql_username+
                                ';PWD='+ mssql_password+
                                ';Trusted_Connection='+mssql_Trusted_Connection+
                                ';MARS_Connection=yes')
    except pyodbc.Error as err:
        raise InvalidUsage(format(err),"500-Database connection failed",status_code=500)
    return ms_connection

def get_smb_connection():
    smb_structs.SUPPORT_SMB2 = True
    # Reading application id and secret
    app_id_pwd=DocumentManagementSecurity.call_batch_for_file_id()
    userID=str(app_id_pwd[1])
    password=str(app_id_pwd[0])
    client_machine_name = gethostname()
    server_ip = config[Constants.DOCUMENTPRINT][Constants.SERVER_IP]
    server_name = config[Constants.DOCUMENTPRINT][Constants.SERVER_NAME]
    domain_name = config[Constants.DOCUMENTPRINT][Constants.DOMAIN_NAME]
    smb_conn = None
    try:
        # Connecting to Remote windows server using pysmb
        smb_conn = SMBConnection(userID, password, client_machine_name, 
            server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
        conn_obj = smb_conn.connect(server_ip, int(Constants.RECEPTION_PORT))
    except IOError as err:
        raise InvalidUsage(format(err),"500-pysmb connection failed",status_code=500)
    return smb_conn