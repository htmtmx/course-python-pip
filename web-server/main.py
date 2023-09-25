import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5]


@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
            <html>
                <head>
                    <title>Contact</title>
                </head>
                <body>
                    <h1>Contact</h1>
                    <p>Phone: 123456789</p>
                    <p>Email:
                        <a href="mailto:mail@mail.com">
                        </a>
                        </p>
                </body>
            </html>
        """


@app.get('/categories')
def get_categories():
    return {'1': 'Category 1', '2': 'Category 2'}

def run():
    store.get_categories()
        
        
if __name__ == '__main__':
    run()