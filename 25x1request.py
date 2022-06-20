# request with API
import requests as req
userName = "UsagiB4"
apiUri = f"https://api.github.com/users/{userName}"
gitReq = req.get(apiUri)
gitContent = gitReq.content  # this will show the content into byte format
print(type(gitContent))
textContent = gitReq.text  # this will return the content into string format
print(textContent)

jsonContent = gitReq.json()
print(type(jsonContent))  # this will return the api contents as a json data. which we can easily access.
print(jsonContent['html_url'])  # as it's an dictionary, we can easily access the values with keys.

