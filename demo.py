from flask import Flask
from visa.logger import logging
from visa.exception import CustomException
import os
import sys


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception (" we are testing our custom exception file")
    except Exception as e:
        visa = CustomException(e,sys)
        logging.info(visa.error_message)
        logging.info("we are testing logging module")
        return "hello World"
    
    


if __name__=="__main__":
    app.run(debug=True)