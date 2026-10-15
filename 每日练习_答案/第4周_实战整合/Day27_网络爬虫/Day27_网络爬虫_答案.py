# ===== Day27_网络爬虫 参考答案 =====

# 【题1】用 requests 抓取一个网页的标题（需先 pip install requests）。
import requests

url = "https://www.example.com"
resp = requests.get(url, timeout=5)
print("状态码:", resp.status_code)

# 简单提取 <title>
text = resp.text
start = text.find("<title>") + len("<title>")
end = text.find("</title>")
print("网页标题:", text[start:end])

# ==================================================

# 【题2】抓取网页并保存到本地文件。
import requests

url = "https://www.example.com"
resp = requests.get(url, timeout=5)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(resp.text)
print("已保存 page.html")

# ==================================================

# 【题3】带上异常处理的网络请求（超时/连接错误兜底）。
import requests

url = "https://www.example-nonexistent-site.com"
try:
    resp = requests.get(url, timeout=3)
    print("状态码:", resp.status_code)
except requests.exceptions.Timeout:
    print("请求超时")
except requests.exceptions.ConnectionError:
    print("连接失败，请检查网络或网址")

# ==================================================

