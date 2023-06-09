from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
import couchdb

from getRawData import get_database_name as get_data
from Page1 import page1_data_query
from Page4 import page4_data_query
from Page2 import M4API
from Page2 import tweet
from Page3 import page3
from Homepage import home_page_data

app = FastAPI()


# authentication
def login_to_db():
    admin = 'admin'
    password = 'password123456'
    url = f'http://{admin}:{password}@172.26.128.204:5984/'
    db = 'gcc_sentiment_data'
    couch = couchdb.Server(url)
    if db in couch:
        db = couch[db]
        print("Connected to database")
    return db


def login_to_mastodonDB():
    admin = 'admin'
    password = 'password123456'
    url = f'http://{admin}:{password}@172.26.128.137:5984/'
    db = 'mastodon2'
    couch = couchdb.Server(url)
    if db in couch:
        db = couch[db]
    return db


db = login_to_db()
db_mastodon = login_to_mastodonDB()


@app.get("/showdatabase")
def get_database():
    return get_data()


@app.get("/homepage")
def get_homepage_data():
    return home_page_data.query_data(db_mastodon)


@app.get("/page1data")
def get_page_1_data():
    return page1_data_query.query_data(db)


@app.get("/page2data_mastodon")
def get_page_2_data_M():
    return M4API.query_data()


@app.get("/page2data_tweet")
def get_page_2_data_T():
    return tweet.query_data(db)


@app.get("/page3data")
def get_page_3_data():
    return page3.query_data(db)


@app.get("/page4data")
def get_page_4_data():
    return page4_data_query.query_data_page4(db)


class ServiceNotFound(Exception):
    def __init__(self, name: str = "No service found"):
        self.name = name


@app.exception_handler(ServiceNotFound)
async def service_not_found_handler(request: Request, exc: ServiceNotFound):
    return JSONResponse(status_code=404, content={"message": exc.name})


def run():
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000)


if __name__ == '__main__':
    run()
