hexalph = """!"#$%&'()*+,-./0123456789:'<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
def hexto64(hex_string) :
    n = list(hex_string.lower())
    n.reverse()
    nlist = []
    