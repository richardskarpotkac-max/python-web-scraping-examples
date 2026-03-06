import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

df.to_csv("posts.csv", index=False)

print("API data exported to posts.csv")
