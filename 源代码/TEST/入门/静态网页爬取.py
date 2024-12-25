import requests
from bs4 import BeautifulSoup

from 源代码.TEST.入门.common import NoteContent

URL = "https://www.ptt.cc/bbs/Stock/index.html"
Header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
          }



def get_web_page(url):
    try:
        response = requests.get(url, headers=Header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            note_list = []

            all_note_elements = soup.select("div.r-ent")
            for note_element in all_note_elements:
                soup2 = BeautifulSoup(note_element.prettify(), "lxml")
                note_content = NoteContent()
                # title
                if len(soup2.select("div.r-ent div.title > a")) > 0:
                    note_content.title = soup2.select("div.r-ent div.title > a")[0].text.strip()
                    note_list.append(note_content)
                else:
                    note_content.title = ""
                    note_list.append(note_content)
                # date
                if len(soup2.select("div.r-ent div.date")) > 0:
                    note_content.publish_date = soup2.select("div.r-ent div.date")[0].text.strip()
                    note_list.append(note_content)
                else:
                    note_content.publish_date = ""
                    note_list.append(note_content)
                # author
                if len(soup2.select("div.r-ent div.author")) > 0:
                    note_content.author = soup2.select("div.r-ent div.author")[0].text.strip()
                    note_list.append(note_content)
                else:
                    note_content.author = ""
                    note_list.append(note_content)
                # detail_link
                if len(soup2.select("div.r-ent div.title > a ")) > 0:
                    note_content.detail_link = soup2.select("div.r-ent div.title > a")[0]["href"]
                    note_list.append(note_content)
                else:
                    note_content.detail_link = ""
                    note_list.append(note_content)

        return note_list

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None





if __name__ == '__main__':
    orgin_html = """
    <div class="r-ent">
    			<div class="nrec"><span class="hl f2">4</span></div>
    			<div class="title">
    				<a href="/bbs/Stock/M.1733872985.A.016.html">[新聞] 戒嚴風波牽連 韓軍工股恐掉單、股價集體</a>
    			</div>
    			<div class="meta">
    				<div class="author">cjol</div>
    				<div class="article-menu">

    					<div class="trigger">&#x22ef;</div>
    					<div class="dropdown">
    						<div class="item"><a href="/bbs/Stock/search?q=thread%3A%5B%E6%96%B0%E8%81%9E%5D&#43;%E6%88%92%E5%9A%B4%E9%A2%A8%E6%B3%A2%E7%89%BD%E9%80%A3&#43;%E9%9F%93%E8%BB%8D%E5%B7%A5%E8%82%A1%E6%81%90%E6%8E%89%E5%96%AE%E3%80%81%E8%82%A1%E5%83%B9%E9%9B%86%E9%AB%94">搜尋同標題文章</a></div>

    						<div class="item"><a href="/bbs/Stock/search?q=author%3Acjol">搜尋看板內 cjol 的文章</a></div>

    					</div>

    				</div>
    				<div class="date">12/11</div>
    				<div class="mark"></div>
    			</div>
    </div>"""

    html_content = get_web_page(URL)
    for note in html_content:
        print(note)
