from flask import Flask,redirect,url_for,request,render_template
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

@app.route('/<pnr>')
def pnr_info(pnr):
   url="https://www.railyatri.in/pnr-status/"
   url+=pnr
   source=requests.get(url).text
   soup = BeautifulSoup(source,'lxml')
   details=soup.find(id='status')
   details2=soup.find('div',class_='pnr-search-result-info')
   f = open("templates/index1.html", "w")
   tags = details2.find_all('p',class_="pnr-normal-font")
   tags2 = details2.find_all('p',class_="pnr-bold-txt")
   tags3 = details2.find_all('span',class_="pnr-bold-txt")
   f.write(tags[0].text)
   f.write(":")
   f.write(tags2[0].text)
   f.write("<br>")
   f.write(tags[1].text)
   f.write(":")
   f.write(tags2[1].text)
   f.write("<br>")
   f.write(tags[2].text)
   f.write(":")
   f.write(tags2[2].text)
   f.write("<br>")
   f.write(tags[3].text)
   f.write(":")
   f.write(tags3[0].text)
   f.write(tags3[1].text)
   f.write("<br>")
   f.write(tags[4].text)
   f.write(":")
   f.write(tags2[3].text)
   f.write("<br>")
   f.write(tags[5].text)
   f.write(":")
   f.write(tags2[4].text)
   f.write("<br>")
   f.write(tags[6].text)
   f.write(":")
   f.write(tags2[5].text)
   f.write("<br>")
   tag4 = details.find_all('p',class_="pnr-normal-font")
   tag5 = details.find_all('p',class_="pnr-bold-txt")
   tag6 = details.find_all('span',class_="confrm-problity-txt")
   f.write("<table><tr><th>")
   f.write(tag4[0].text)
   f.write("</th><th>")
   f.write(tag4[1].text)
   f.write("</th><th>")
   f.write(tag4[2].text)
   f.write("</th></tr>")
   j=-1
   for i in range(0,len(tag6)):
       j+=1
       f.write("<tr><td>")
       f.write(tag5[j].text)
       f.write("</td><td>")
       f.write("&nbsp")
       j+=1
       f.write(tag5[j].text)
       f.write("</td><td>")
       f.write(tag6[i].text)
       f.write("</td></tr>")
   f.write("</table>")
   f.close()
   return render_template('index1.html')

@app.route('/login',methods=['GET','POST'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      
      return redirect(url_for('pnr_info',pnr = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('pnr_info',pnr = user))

if __name__ == '__main__':
   app.run(debug=True)
