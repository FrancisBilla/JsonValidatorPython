#!/usr/bin/env python3

from cerberus import Validator
import json


v = Validator()
# v.schema = {"contact_details": {
#     "type": "dict",
#     "schema": {
#         "phone": {
#             "type": "string",
#             "minlength": 10,
#             "maxlength": 10,
#             "regex": "^0[0-9]{9}$"
#         },
#         "email": {
#             "type": "string",
#             "minlength": 8,
#             "maxlength": 255,
#             "required": True,
#             "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
#         }
#     }
# }}

def get_schema():
    with open('./user_schema1.json', 'r') as file:
        schema = json.load(file)
    return schema
print(get_schema())
# v.schema = get_schema()
if v.validate({'contact_details': {'phone': '0901123123',
                                   'email': 'john.doe@example.com'}}):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)