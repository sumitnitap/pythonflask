# Import for DocumentPrint modules
from DocumentManagementUtil import json_key_value_mapper_util, date_format_util

def fetch_customer_active_file_mapper(row_header, row_data):
    """Map stored procedure columns to json response naming conventions

    :param key_header: stores the column names from stored procedure response
    :type key_header: list
    :param values: stores the rows fetched from the stored procedure
    :type values: list
    :return: customer file records as python dictionaries
    :rtype: list
    """
    data=[]
    dict_key ={'FileName':'fileName',
            'FileRceivedDate':'fileReceivedDate',
            'ProcessDate':'processDate',
            'PrintEndDate':'printEndDate',
            'InsertCompleteDate':'insertCompleteDate',
            'DueDate':'dueDate',
            'MailPieces':'mailPieces',
            'JobControlNumber':'jobControlNumber',
            'FileStatus':'fileStatus'}
    dates=['fileReceivedDate','processDate'
           ,'printEndDate','insertCompleteDate','dueDate']
    data=json_key_value_mapper_util(dict_key, row_header, row_data)
    for d in data:
        date_format_util(d,dates)
    return data
   

def search_files_mapper(row_header, row_data):
    """Map stored procedure columns to json response naming conventions

    :param key_header: stores the column names from stored procedure response
    :type key_header: list
    :param values: stores the rows fetched from the stored procedure
    :type values: list
    :return: customer file records as python dictionaries
    :rtype: list
    """
    data=[]
    dict_key ={'FileName':'fileName',
            'FileReceivedDate':'fileReceivedDate',
            'ProcessDate':'processDate',
            'PrintEndDate':'printEndDate',
            'InsertCompleteDate':'insertCompleteDate',
            'MailDate':'mailDate',
            'DueDate':'dueDate',
            'MailPieces':'mailPieces',
            'JobControlNumber':'jobControlNumber',
            'FileStatus':'fileStatus',
            'ResponseFileStatus':'responseFileStatus'}
    dates=['fileReceivedDate','processDate','printEndDate'
            ,'insertCompleteDate','dueDate','mailDate']
    data=json_key_value_mapper_util(dict_key, row_header ,row_data)
    for d in data:
        date_format_util(d,dates)
    return data

def search_documents_mapper(row_header, row_data):
    """Map stored procedure columns to json response naming conventions

    :param key_header: stores the column names from stored procedure response
    :type key_header: list
    :param values: stores the rows fetched from the stored procedure
    :type values: list
    :return: customer file records as python dictionaries
    :rtype: list
    """
    data=[]
    dict_key ={'CustomerFileName':'customerFileName',
        'RecipientName':'recipientName',
        'RecipientAddress1':'recipientAddress1',
        'RecipientAddress2':'recipientAddress2',
        'RecipientCityStateZip':'recipientCityStateZip',
        'CustomerUniqueId':'customerUniqueId',
        'CheckNumber':'checkNumber',
        'TrackingNumber':'trackingNumber',
        'HMDS_JobControlNumber':'jobControlNumber',
        'FileReceivedDate':'fileReceivedDate',
        'MailDate':'mailDate'}
    dates=['fileReceivedDate','mailDate']
    data=json_key_value_mapper_util(dict_key, row_header, row_data)
    for d in data:
        date_format_util(d,dates)
    return data

def submit_file_mapper(row_header, row_data):
    """Map stored procedure columns to json response naming conventions

    :param row_header: stores the column names from stored procedure response
    :type key_header: list
    :param row_data: stores the rows fetched from the stored procedure
    :type values: list
    :return: customer file records as python dictionaries
    :rtype: list
    """
    data=[]
    dict_key = {'FileId':'fileId',
                'FileName':'fileName',
                'ProcessStatusId':'code',
                'ProcessStatus':'description',
                'SubmissionDateTime':'submissionDateTime'}
    dates=['submissionDateTime']
    data=json_key_value_mapper_util(dict_key,row_header,row_data)
    for d in data:
        date_format_util(d,dates)
    return data