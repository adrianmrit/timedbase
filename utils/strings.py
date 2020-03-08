def super_clean_str(string):
    """Clean a string from anything else other than alphanumeric characters and return it on lowercase

    Arguments:
        string {String} -- String to be cleaned

    Returns:
        String -- Cleaned string
    """
    return ''.join(x for x in string if x.isalnum()).lower()

def super_clean_price(string):
    return ''.join(x for x in string if x.isalnum() or x=='.')