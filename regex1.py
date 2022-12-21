import sys; args = sys.argv[1:]
idx = int(args[0])-30

myRegexLst = [
  r"/^0$|^10[01]$/",
  r"/^[01]*$/",
  r"/^[01]*0$/",
  r"/\b\w*[aieou]\w*[aieou]\w*/i",
  r"/^1[01]*0$|^0$/",
  r"/^[01]*1{2}0[01]*$/",
  r"/^.{2,4}$/is",
  r"/^\d{3}\s*[-]?\s*\d{2}\s*[-]?\s*\d{4}\s*$/",
  r"/^.*?d\w*\b/im",
  r"/^0[01]*0$|^1[01]*1$|^[01]$|^$/"]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

#Joaquim Das 3 2022