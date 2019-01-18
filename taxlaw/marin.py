url = 'https://apps.marincounty.org/RecordersIndexSearch?XHideDisclaimer=True' # after accepting disclaimer
base_url = 'https://apps.marincounty.org'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.content, "html.parser")
action_url = soup.find('form', id="T").get('action')
data = {"TDT" : "Tax Lien", # doc title
        "TSD" : "08012018",
        "TED" : "12312018",
        }
form_url = "{}{}".format(base_url, action_url)
print("Form url is {}".format(form_url))
post = requests.post(form_url, data=data) # wrong format?  need to finish data?
# webbrowser.open(post.url)
print(BeautifulSoup(post.content))
