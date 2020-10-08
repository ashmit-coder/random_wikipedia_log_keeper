import wikipedia
import requests
import shutil,os
lst = wikipedia.random(pages=1)

page = wikipedia.page(lst)

conts = page.summary
fil = open(f"{lst}.txt","w+")
spilt = conts.split(".")
fil.write("\n")
for x in spilt:
    fil.write(x)
    fil.write("\n")
fil.write(f"\nFor further info go to \n {page.url}\n")
fil.close()
shutil.move(f"{lst}.txt", "articles")