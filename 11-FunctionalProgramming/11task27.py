#27.	Students obtained the following test results (in points, from 0 to 100):
#test_results = [
#    {"name":"Peter","result":27},
#    {"name":"Anna","result":63},
#    {"name":"Robert","result":92},
#    {"name":"Paul","result":46},
#    {"name":"Barbara","result":52}]
#Write a program that displays students whose scores are between 50 and 70 points. Use an anonymous function and filter() function.

#nie wiem


test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

outp=""
for i in range(len(test_results)):
    if test_results[i]["result"]>=50 and test_results[i]["result"]<=70:
        outp += test_results[i]["name"] +","
print(outp)

filtered = []
for i in range(len(test_results)):
    sample = test_results[i]
    b = list(sample.items())
    print(b)
    a = list(sample.values())
    print(a)
    ans = dict(filter(lambda x: (x[1]>=50 and x[1]<=70),sample.values()))
    filtered.append(ans)
print(ans)