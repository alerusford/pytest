# from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                # validate(item, schema)
                schema.parse_obj(item)
        else:
            # validate(self.response_json, schema)
            schema.parse_obj(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
