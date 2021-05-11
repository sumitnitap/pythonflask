from Constants import ASCII
import subprocess
import configparser
from DocumentManagementError import InvalidUsage

def call_batch_for_application_id():
       """
       Call the Batch script to retreive application id and application secret
       :security_file - location of the batch file from config.ini file 
       :param(output) - list containing application id and application secret
       """
       config = configparser.ConfigParser()
       config.read("config.ini")
       security_file=config['DocumentPrint']['mssql-security-file']
       try:
              out = subprocess.Popen(['sh',security_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
              stdout,stderr = out.communicate()
       except Exception as e:
              raise InvalidUsage(format(e),"500-Unable to open batch file",status_code=500)
       app_id_pwd=[]
       app_id_pwd.append(stdout.split()[0].decode(ASCII))
       app_id_pwd.append(stdout.split()[1].decode(ASCII))
       return app_id_pwd

def call_batch_for_file_id():
       """
       Call the Batch script to retreive application id and application secret
       :security_file - location of the batch file from config.ini file 
       :param(output) - list containing application id and application secret
       """
       config = configparser.ConfigParser()
       config.read("config.ini")
       security_file=config['DocumentPrint']['reception-security-file']
       try:
              out = subprocess.Popen(['sh',security_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
              stdout,stderr = out.communicate()
       except Exception as e:
              raise InvalidUsage(format(e),"500-Unable to open batch file",status_code=500)
       app_id_pwd=[]
       app_id_pwd.append(stdout.split()[0].decode(ASCII))
       app_id_pwd.append(stdout.split()[1].decode(ASCII))
       return app_id_pwd

