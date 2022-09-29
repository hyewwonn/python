id_number = "050524"
year = id_number[:2]
md = id_number[2:]
multi = str(int(year)*int(md))
print(year+"\n"+md+"\n"+multi)
