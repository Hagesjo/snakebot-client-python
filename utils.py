def logging_format(input_dict, depth=1, outp=""):
    for key, value in input_dict.items():
        if type(value) == dict:
            outp += logging_format(value, depth + 1)
        else:
            outp += "{}{} = {}\n".format("\t" * depth, key, value)
    return outp
