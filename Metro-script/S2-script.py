from s2 import s2

lat, lon, res = 28.45943620933896, 77.07243708889374, 12

s2_address = s2.geo_to_s2(lat, lon, res)
aaa = {}
aaa = s2.s2_to_geo_boundary(s2_address)
#result = aaa[0].replace('[','(')
print(aaa[0])
print(aaa[1])
print(aaa[2])
print(aaa[3])
print(aaa[4])



