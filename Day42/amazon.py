from bs4 import BeautifulSoup
import requests, os, dotenv

from twilio.rest import Client # type: ignore

dotenv.load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
# content_sid = os.getenv("CONTENT_SID")
twilio_whatsapp = os.getenv("TWILIO_WHATSAPP")
my_whatsapp = os.getenv("MY_WHATSAPP")

url = "https://www.amazon.in/gp/aw/d/B08NC3Q2FQ/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=05ff58259c9d352675aa76260f5bdb2d&hsa_cr_id=0&qid=1752626962&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_lsi4d_asin_0_price&pd_rd_w=BfI8G&content-id=amzn1.sym.cbe1d71a-30e3-45dc-b787-bad221b13c68%3Aamzn1.sym.cbe1d71a-30e3-45dc-b787-bad221b13c68&pf_rd_p=cbe1d71a-30e3-45dc-b787-bad221b13c68&pf_rd_r=ZGTKF1YV9Z2Z3S7X6FFH&pd_rd_wg=HWahG&pd_rd_r=14c11177-4e13-4523-b3c6-94cb90eaeb17&th=1"

try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')    

price = soup.select_one('span.a-price-whole')
price = price.find(recursive=False, string=True)
print(f"Price: Rs {price}")
price_f = float(price.replace(',', '')) if price else 'Price not found'

print(price_f)

if price_f < 31000:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                from_=twilio_whatsapp,
                body=f"The price of the product is Rs {price}. It's a good deal!",
                to=my_whatsapp
            )
    print("message sent:", message.sid)