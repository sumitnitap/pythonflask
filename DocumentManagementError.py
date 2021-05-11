class InvalidUsage(Exception):
    """User-defined exception
    :param message: stores the column names from stored procedure response
    :type message: string
    :param code: stores the rows fetched from the stored procedure
    :type code: string
    :param status_code: stores the rows fetched from the stored procedure
    :type status_code: string
    :return: Dict of user defined excpetion
    :rtype: Dict
    """
    status_code = 400

    def __init__(self, message, code, status_code=None):
        Exception.__init__(self)
        self.message = message
        self.code = code
        if status_code is not None:
            self.status_code = status_code
        

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        rv['code'] = self.code
        return rv