def opposite(clause):#判断是否有对立语句可以进行抵消
    if '~' in clause:
        return clause.replace('~', '')
    else:
        return '~' + clause