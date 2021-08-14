"""This will contains adhoc functions"""


def check_if_param_exists(params, required_params):

    # check if param is missing and check if data type is correct
    for key, val in required_params.items():
        if key not in params:
            return key + ' is required parameter'
        else:
            try:
                required_params[key] = required_params[key](params[key])
            except:
                return key + ' should be of type ' \
                       + str(
                    str(required_params[key]).replace("class", "").replace("<", "").replace(">", "").replace("\\",
                                                                                                             "").replace(
                        "'", "")).strip()

    return required_params
