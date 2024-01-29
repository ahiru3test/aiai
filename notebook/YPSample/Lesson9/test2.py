#以下はPythonのコード
import re
 
def str_search(ptr,str_):
    colorRED = '\033[91m'
    colorEND = '\033[0m'
    pattern = re.compile(ptr)
    res = pattern.search(str_)
    if res is not None:
        r = res.span()
        str1 = str_[0:r[0]]
        str2 = str_[r[0]:r[1]]
        str3 = str_[r[1]:]
        restr =  "{}{}{}{}{}".format(str1,colorRED ,str2 ,colorEND, str3)
        return restr
    else:
        return str_
if __name__ == "__main__":
    ptr = "^TXT"
    str_ = "TXTTT"
    ret = str_search(ptr, str_)
    print(ret)
 