## update_blogPost.py
import feedparser

blog_url = "https://jamong-5.tistory.com/rss"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
    if idx > MAX_NUM:
        break
    feed_date = entrie['published_parsed']
    latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=300&section=header&text=JAMONG%205&fontSize=90" />
</div>
<div align="right">
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjennifer060697&count_bg=%23708FD3&title_bg=%23515151&icon=ghostery.svg&icon_color=%23E7E7E7&title=HITS%21%21&edge_flat=false"/>
</div>

<h2 align="center">☾⋆⁺LINK⁺⋆☾</h2>
<div align="center">
  <a href="https://jamong-5.tistory.com/"><img src="https://img.shields.io/badge/TechBlog-09B3AF?style=flat-square&logo=Tistory&logoColor=white&link=https://jamong-5.tistory.com/"/></a>
<!--   <a href="https://www.kaggle.com/jamong5"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=Kaggle&logoColor=white&link=https://www.kaggle.com/jamong5"/></a> -->
  <a href="mailto:oennifer060697@gmail.com"><img src="https://img.shields.io/badge/Email-FF4785?style=flat-square&logo=Gmail&logoColor=white&link=mailto:oennifer060697@gmail.com"/></a>
</div>

<!-- <h2 align="center">☾⋆⁺Available⁺⋆☾</h2>
<div align="center">
  <img src="https://img.shields.io/badge/Python-00B1E7?logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/C++-00599C?logo=C%2B%2B&logoColor=white"/>
  <img src="https://img.shields.io/badge/C-000000?logo=C&logoColor=white"/>
</div> -->

<br><br>

<div align="center">
  <img src = "https://github-readme-stats.vercel.app/api?username=jennifer060697&theme=great-gatsby&show_icons=true">
  <t>&nbsp;&nbsp;&nbsp;&nbsp;</t>
  <img src = "http://mazassumnida.wtf/api/v2/generate_badge?boj=jennifer0606">
  <t>&nbsp;&nbsp;&nbsp;&nbsp;</t>
  <img src = "https://github-readme-stats.vercel.app/api/top-langs/?username=jennifer060697&layout=compact">
</div>

<br><br>

#### 🌱 I’m currently learning ...
- Pytorch
- MMDectection, YOLO
- SQL
- JAVA

<br><br>
#### 🌱 My Latest Posts

"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
