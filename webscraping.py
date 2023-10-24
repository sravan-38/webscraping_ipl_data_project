import requests
import pandas
from bs4 import BeautifulSoup 
response = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DPOCO&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_6d4a2f3d-ccc6-437f-8808-a65f84c117b1_5.O1WYX08RHODP&ppt=clp&ppn=mobile-phones-store&ssid=a6p32j7fts0000001691832642564&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlBPQ08iXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&otracker=clp_metro_expandable_2_6.metroExpandable.METRO_EXPANDABLE_POCO_mobile-phones-store_O1WYX08RHODP_wp3&fm=neo%2Fmerchandising&iid=M_99f15828-c4d7-42c3-a0e2-0374a8dfb0f5_6.O1WYX08RHODP&ppt=hp&ppn=homepage&ssid=ukb6imfzow0000001693577977045")
# print(response)
scoup = BeautifulSoup(response.content,"html.parser")
# print(scoup)
names = scoup.find_all("div",class_="_4rR01T")
# print(names)
name =[]
for i in names[0:10]:
    d = i.get_text()
    name.append(d)
print(name)

prices = scoup.find_all('div',class_="_30jeq3 _1_WHN1")
price = []
for i in prices[0:10]:
    price.append(i.get_text())
print(price)

ratings = scoup.find_all('span',class_="_2_R_DZ")
rate = []
for i in ratings[0:10]:
    rate.append(i.get_text())
print(rate)


images = scoup.find_all("img",class_="_396cs4")
image = []
for i in images[0:10]:
    image.append(i["src"])
print(image)


# links = scoup.find_all("a",class_="_1fQZEK")
# link = []
# for i in links[0:10]:
#     d = "https://www.flipkart.com/ "+i['href']
#     link.append(i['href'])
# # print(link)
df = pandas.DataFrame()
# print(df)
data = {
    "names":pandas.Series(name),
    "ratings":pandas.Series(rate),
    "prices":pandas.Series(price),
    "images":pandas.Series(image),
    # "links":pandas.Series(link),
}
print(data)

df = pandas.DataFrame(data)
print(df)

df.to_csv("mobiles.csv")
print(df)
