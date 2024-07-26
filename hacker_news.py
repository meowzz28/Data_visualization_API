from operator import itemgetter
import requests
import plotly.express as px

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:20]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    try:
        c = response_dict['descendants']
    except KeyError:
       continue
    else:
        submission_dict = {
            'title': response_dict['title'][:50],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

article_links, comments = [], []
for submission_dict in submission_dicts:
    article_name = submission_dict['title']
    article_url = submission_dict['hn_link']
    article_link = f"<a href='{article_url}'>{article_name}</a>"
    article_links.append(article_link)
    comments.append(submission_dict['comments'])
title = 'Top Stories on Hacker News'
labels = {'x': 'Article Name', 'y':'No. of Comments'}
fig = px.bar(x=article_links,y=comments, title=title,labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()