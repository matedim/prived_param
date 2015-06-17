def powerHorse(v):
    horse=v*1.36
    return horse

def powerVatt(h):
    kvatt=h/1.36
    return kvatt

v=(10000, 9200, 9018,9000, 8050, 7300, 7047, 6560,5800)
n=(8500, 7500,6186, 7380, 7380, 6700, 6397,6020, 5450)
m1=(11400, 10600,10540, 9700, 8600, 7700, 7229,6810, 6180)
m2=(12200, 11400, 11273,10100, 9000, 8020, 7636,7200, 6500)
p=(2000, 3000,4000,5000,5500,6000,6500,7000,7500,8000)

b=[] # take off
nom=[] # max continuos
min30=[] # 30 min OEI
min2_5=[] #2.5 min OEI
power_horse=[] #Output Power in horse

for i in v:
    b.append(int(powerVatt(i)))
for i in n:
    nom.append(int(powerVatt(i)))
for i in m1:
    min30.append(int(powerVatt(i)))
for i in m2:
    min2_5.append(int(powerVatt(i)))
for i in p:
    power_horse.append(int(powerHorse(i)))


print "Take -Off", b
print "Max Continuous", nom
print "30min OEI", min30
print "2.5min OEI", min2_5
print "Output Power in horse",power_horse
