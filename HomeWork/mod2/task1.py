s = input()

comma_pos = s.find(',')

a_str = s[:comma_pos].strip()
##jhjhjhjhjhj
b_str = s[comma_pos+1:].strip()
a = int(a_str)
b = int(b_str)
print(a % b)