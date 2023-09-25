import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print(type(categories))
    for categorie in categories:
        print(categorie['name'])

if __name__ == '__main__':
    get_categories()