import requests


url = "https://esports-api.lolesports.com/persisted/gw/getLeagues"
headers = {"x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z"}
params = {"hl": "pt-BR"}

response = requests.get(url, headers=headers, params=params).json()

print(response)