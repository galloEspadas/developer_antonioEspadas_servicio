from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/getProducts")
async def get5Products():
    url = "https://fakestoreapi.com/products?limit=5"
    url_post = "https://fakestoreapi.com/products"
    headers = {
        "content-type": "application/json"
    }
    response = requests.request("GET",url)
    new_response = []
    for i in response.json():
        print(i)
        new_response.append({'tile':i['title']+" Nuevos Titutlos"})
    
    response2 = requests.request('POST',url_post,data=new_response)
    return {"Response":response2.json()}