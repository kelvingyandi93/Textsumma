from typing import Union
from sum import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI() 

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Link(BaseModel): 
    name: str
    size: float

@app.post("/links") 
async def create_item(link: Link): 
    result = predict(link.name, link.size)
    return {"result" : result} 


