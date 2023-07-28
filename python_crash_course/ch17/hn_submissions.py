import plotly.express as px

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
links, comments = [], []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    hn_link = f"https://news.ycombinator.com/item?id={submission_id}"
    title = response_dict["title"]
    link = f"<a href='{hn_link}'>{title}</a>"
    links.append(link)
    comments.append(response_dict["descendants"])

labels = {"x": "Article", "y": "Comments"}
fig = px.bar(x=links, y=comments, title="Most-Commented Articles on Hacker News")
fig.show()
