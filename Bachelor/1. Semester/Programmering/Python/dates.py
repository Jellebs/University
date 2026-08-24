import datetime as dt

nu = dt.datetime.now().replace(microsecond= 0)



minFødselsdag = dt.datetime(1999,6,5)
iDag = dt.datetime.today().replace(microsecond= 0)
omEnUge = (dt.datetime.today() + dt.timedelta(7)).replace(microsecond= 0)


dageJegHarLevet = dt.datetime.today() - minFødselsdag


#minNæsteFødselsdag()

#iDag = dt.datetime.day()

print(minFødselsdag)
print("Jeg er født en " + str(minFødselsdag.day()))
print(iDag)
print(omEnUge)
print(dageJegHarLevet)

