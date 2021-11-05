valid = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
def solution(num):
    conv = []
    for n in valid:
        if num >= n:
            x, y = divmod(num, n)
            num = y
            for i in range(x):
                conv.append(valid.get(n))
    conv = ''.join(conv)
    return conv