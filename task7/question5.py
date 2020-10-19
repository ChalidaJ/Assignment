def get_sec(time_str):
    
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


print(get_sec('1:50:00'))
print(get_sec('1:20:00'))
print(get_sec('4:10:00'))