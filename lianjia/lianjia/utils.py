
# 列表去空拼接
def list_strip_join(data):
    res = ''
    for i in data:
        res += i.strip()
    return res