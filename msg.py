from flask import request
new_msg = request.values.get('Body', '').lower()
