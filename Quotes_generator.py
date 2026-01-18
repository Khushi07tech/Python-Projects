import requests
base_url = "https://zenquotes.io/api"
def get_quote():
    url = f"{base_url}/random"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()[0]
    else:
        print("It's not you, it's us☹")
        print(f"😖Error: {response.status_code}")
        return None

def fetch_quotes (num_quotes):
    quote_list = []
    for _ in range(num_quotes):
        quote = get_quote()
        if quote:
            quote_list.append(quote)
    return quote_list

def print_quotes(quote):
        print(f"🔮Quote = {quote['q']}")
        print(f"✨Author = {quote['a']}")
        print("🎀✨🎆⭐👑💕🎀✨🎆⭐👑")

def print_quote_list(quote_list):
    for q in quote_list:
        for key, value in q.items():
            if key == "h":
                continue
            else:
                print(f"{key} ~ {value}")
        print ()

def get_user_input ():
    while True:
        try:
            return int(input("Enter the number of quotes: "))
        except ValueError:
            print ("Please enter a valid number")

#=========== MAIN FLOW ===========

num_quotes = get_user_input()

quotes = fetch_quotes(num_quotes)
for quote in quotes:
    print_quotes(quote)

see_quote_list = input("Want to see the quote's list(y/n): ").lower()
if see_quote_list != "y" and see_quote_list != "n":
    print ("Invalid Input")
elif see_quote_list == "n":
    print ("OKIEE!🎀")
else:
    print_quote_list(quotes)