# Imports for DocumentPrint modules
import DocumentManagementError

# Pip-installed modules
import Constants
from datetime import datetime
from jsonschema import validate, exceptions
import json

def validate_wildcard_input(input_string):
    """ Validate if the wildcard character * is not passed as 
        the first character in the search field.
    :param input_string: json attribute to be validated
    :type input_string: string
    """
    if input_string[0] == Constants.ASTERIX:
        raise DocumentManagementError.InvalidUsage(
                          Constants.WILDCARD_FIRST_LOCATION
                          , Constants.BAD_REQUEST
                          , status_code=400)
    else:
        return True

def date_validation(date_string):
    """ Validate if the date passed is of format 'MM-DD-YYYY'
    :param date_string: json date attribute to be validated for defined format
    :type date_string: 
    """     
    date_format = Constants.REQUEST_DATE_FORMAT
    try:
        date_obj = datetime.strptime(date_string, date_format)
    except ValueError:
        raise DocumentManagementError.InvalidUsage(
                          Constants.INVALID_DATE_FORMAT
                          , Constants.BAD_REQUEST
                          , status_code=400)


def date_format_util(data,list_date):
    """ Converts any date-time to the format 'MM-DD-YYYY hh:mm:ss'
    :param data:key value from the list of dictionary
                (rows fetched from database)
    :type data: dict
    :param list_date:list of date fields in response
    :type data: list
    :return: key value of rows fetched from db with date defined date format
    :rtype: Dict
    """ 
    date_format = Constants.RESPONSE_DATE_FORMAT
    for date in list_date:
        if(data[date] is not None):
            data[date]=data[date].strftime(date_format)
    return data

def json_key_value_mapper_util(dict_key,row_header,row_data):
    """ Maps column name with its corresponding row value. 
        Also matches the response key name as per design.
    :param dict_key:response key and its corresponding design key
    :type dict_key: dict
    :param row_header:Column name from store procedure code
    :type row_header: list
    :param row_data:rows returned from store procedure
    :type row_data: tupple
    :return: key value response as per design
    :rtype: list of Dict
    """
    json_keys=[]
    data=[]
    for header in row_header:
        json_keys.append(dict_key[header])
    for row in row_data:
        data.append(dict(zip(json_keys,row)))
    return data



def validateJson(jsonData, req_schema):
    """ Validates the Request Body (json) with the correspnding schema 
    :param(input) - jsonData: The request body to be validated given in the POST request 
    :param(output) - True (Given JSON body is valid) OR False (Given JSON body is Invalid)
    """     
    try:
        validate(instance=jsonData, schema=req_schema)
    except exceptions.ValidationError as err:
        return err.message
    return True

def dict_raise_on_duplicates(ordered_pairs):
    """Reject duplicate keys."""
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            raise DocumentManagementError.InvalidUsage("Duplicate field found: "+k
                          , Constants.BAD_REQUEST
                          , status_code=400)
        else:
           d[k] = v
    return d

def validateJsonString(jsonData):
    try:
        json.loads(jsonData)
    except ValueError:
        return False
    return True