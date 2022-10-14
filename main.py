import crawler
import os
from os import link, stat
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import math
import requests
import json


app = FastAPI()

@app.get("/")
def hello():
    return {"message" : "running"}