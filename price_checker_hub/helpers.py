def build_validation_error(errors):
    error_messages = {}
    for error in errors:
        field_name = error['loc'][0]
        error_msg = error['msg']
        error_messages[field_name] = error_msg
    return {'error': error_messages}
