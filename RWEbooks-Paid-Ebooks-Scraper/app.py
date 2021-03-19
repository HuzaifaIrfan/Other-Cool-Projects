import os 
import requests


print("Read and Write Publications Lahore paid Ebooks scraper.")

# code = int(input("Enter rwebooks code (written in preview url): "))
# first_page = int(input("Enter starting page number (default to page 1): ") or "1")
# last_page = int(input("Enter ending page number (written in product description, or what you want): "))

code=222
first_page=1
last_page=5

main_dir = f"RWEbooks/{code}"
if not os.path.exists(main_dir):
    os.makedirs(main_dir)
    
    print(f'Created Dir {main_dir}')
else:
    
    print(f'Dir Already Exists {main_dir}')



print(f'Downloading Pages of Book Code {code} Page {first_page} to {last_page}')


page=first_page

while page <= last_page:
    url = f"https://rwebooks.com/bookpage.php?fid={code}&pn={page}"

    headers = {
        'Content-Type': 'image/png',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'referer': 'https://rwebooks.com/bookpage.php?fid=691&pn=10',
        'sec-fetch-site': 'same-origin'

    }

    print(f'Downloading Page No. {page}')

    response = requests.get(url, headers=headers)

    print(f'Downloaded Page No. {page}')

    file = open(f"{main_dir}/{page}.png", "wb")
    file.write(response.content)
    file.close()

    print(f'Saved Page No.{page}')
    page += 1 


print(f'Downloaded Pages of Book Code {code} Page {first_page} to {last_page} in Dir {main_dir}')