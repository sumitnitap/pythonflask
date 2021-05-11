# Imports for DocumentPrint modules
from DocumentManagementError import InvalidUsage
import DocumentManagementService

# Pip-installed modules
from flask import Flask, jsonify

app = Flask(__name__)

# Custom error handler
@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify({"errors":[error.to_dict()]})
    response.status_code = error.status_code
    return response

@app.errorhandler(404) 
def invalid_route(e): 
    response = jsonify({"errors":[{"code" : 404
                      , "message" : 'Route not found'}]})
    response.status_code=404
    return response

@app.errorhandler(500) 
def invalid_route(e): 
    response = jsonify({"errors":[{"code" : 500
                      , "message" : 'Internal server error'}]})
    response.status_code=500
    return response

@app.errorhandler(405) 
def invalid_route(e): 
    response = jsonify({"errors":[{"code" : 405
                      , "message" : 'Method not allowed'}]})
    response.status_code=405
    return response

@app.errorhandler(400) 
def invalid_route(e): 
    response = jsonify({"errors":[{"code" : 400
                      , "message" : 'Bad request'}]})
    response.status_code=400
    return response

# search customer active files
@app.route('/document-services/document-handling-facility'
              '/customers/<int:bqreferenceid>/active-files', methods=['GET'])
def customer_active_files(bqreferenceid):
    return DocumentManagementService.fetch_customer_active_files(bqreferenceid)

# search customer files
@app.route('/document-services/document-handling-facility'
               '/customers/files', methods=['POST'])
def customer_files():
    """Call the 'fetch_customer_files()' method
    """
    return DocumentManagementService.fetch_customer_files()

# search documents
@app.route('/document-services/document-handling-facility'
                '/customers/documents', methods=['POST'])
def customer_documents():
    return DocumentManagementService.fetch_customer_documents()
    
#Reception API method
@app.route('/document-services/document-handling-facility'
                '/files/register', methods=['POST'])
def file_reception():
    return DocumentManagementService.submit_file()

# Document-preview/composition API
@app.route('/document-services/document-handling-facility'
           '/document-preview/request', methods = ['POST'])
def document_preview_route():
    return DocumentManagementService.document_preview_service()

if __name__=="__main__":
    app.run(host="0.0.0.0", port="5001")