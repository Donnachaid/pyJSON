def printDict(dictToPrint,flagForSingle,ignoreHeaders):
  ss = 'name'
  obj1 = {}
  obj2 = []
  obj3 = []
  headers = []
  obj1Keys = []
  colLen = 0

  if flagForSingle == None:
    flagForSingle = 0

  if ignoreHeaders == None:
    ignoreHeaders = 0

  if flagForSingle == 0:
    for i in range(0, len(dictToPrint.keys())):
      obj1 = dictToPrint[dictToPrint.keys()[i]]
      obj1Keys = obj1.keys()
      colLen = max(len(obj1Keys), colLen)

      for x in range(0, len(obj1Keys)):
        obj2.append(obj1[obj1Keys[x]])

      obj3.append(obj2)
      obj2 = []

  else:
    obj1 = dictToPrint
    obj1Keys = obj1.keys()
    colLen = max(len(obj1Keys), colLen)

    for  x in range(0, len(obj1Keys)):
      obj2.append(obj1[obj1Keys[x]])

    obj3.append(obj2)
    obj2 = []


  print(obj3)


def printDictSelected(dictToPrint,colsToPrint)

  var ss = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName)
  var obj1 = {}
  var obj2 = []
  var obj3 = []
  var headers = []
  var obj1Keys = []
  var colLen = 0
  for (var i = 0; i < Object.keys(dictToPrint).length; i++)
  {
    obj1 = dictToPrint[Object.keys(dictToPrint)[i]]
    obj1Keys = colsToPrint

    for (var x = 0; x < obj1Keys.length; x++)
    {
      obj2.push(obj1[obj1Keys[x]])
    }
    obj3.push(obj2)
    obj2 = []
  }

  for (var i = 0; i < colsToPrint.length; i++)
  {
    ss.getRange(startRow,i+startCol).setValue(colsToPrint[i])
  }

  ss.getRange(startRow+1,startCol,obj3.length,colsToPrint.length).setValues(obj3)

}