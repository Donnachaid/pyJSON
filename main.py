import json
import oFs

file = json.load(open('bank.json'))
#print(json.dumps(file[0].keys(), indent=4))
oFs.printDict(file[0],0,0)