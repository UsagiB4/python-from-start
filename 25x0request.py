import requests as rq

randomReq = rq.get('https://w3schools.com/')
print(randomReq.ok)  # returns True if The status code is less than 200

responseReq = randomReq.request
print(responseReq)
print(randomReq.reason)

reqStat = randomReq.status_code  # returns status code
print(reqStat == 200)  # returns True if the status code is 200
print(reqStat)

reqUrl = randomReq.url  # returns the requested url
print(reqUrl)

reqHeader = randomReq.headers  # returns Header
print(reqHeader)

reqContent = randomReq.content  # returns content of the webpage.
# print(reqContent)  # Output might be large. that's why this section is commented.
