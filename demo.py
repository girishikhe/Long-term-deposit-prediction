from long_term_deposit_prediction.logger import logging
from long_term_deposit_prediction.exception import DepositException
import sys

logging.info("welcome to custom log")
try:
    a=2/0
except Exception as e:
    raise DepositException(e,sys)

