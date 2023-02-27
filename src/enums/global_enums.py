from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'The number of elements is not equal'
