from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
from ai71 import AI71 
import uvicorn
import gradio as gr
from fastapi import FastAPI
from gradio.themes.base import Base
from setup import *
from prompt_template import *
from system_module import *

app = FastAPI()

""" POST API CALL """

@app.get("/post-solutioning-generator")
def post_solutioning_generator(session_id,startup_name,idea):
    solutioning_generator(session_id, startup_name, idea)
    return {"message":"successful"}

@app.get("/post-persona-profiling-builder")
def post_persona_profiling_builder(session_id,startup_name,idea):
    persona_profiling_builder(session_id, startup_name, idea)
    return {"message":"successful"}

@app.get("/post-market-analysis-generator")
def post_market_analysis_generator(session_id,startup_name,idea):
    market_analysis_generator(session_id, startup_name, idea)
    return {"message":"successful"}

@app.get("/post-mvp-builder")
def post_mvp_builder(session_id,startup_name,idea):
    mvp_builder(session_id, startup_name, idea)
    return {"message":"successful"}

@app.get("/post-feedback-analyzer")
def post_feedback_analyzer(session_id,filepath):
    feedback_analyzer(session_id, filepath)
    return {"message":"successful"}

""" RETRIEVE API CALL """

@app.get("/retrieve-solutioning-generator")
def get_solutioning_generator(session_id):
    return [i for i in collection.find({"module":"solutioning generator","session_id":session_id})][-1]

@app.get("/retrieve-persona-profiling-builder")
def get_persona_profiling_builder(session_id):
    return [i for i in collection.find({"module":"persona profiling builder","session_id":session_id})][-1]

@app.get("/retrieve-market-analysis-generator")
def get_market_analysis_generator(session_id):
    return [i for i in collection.find({"module":"market analysis generator","session_id":session_id})][-1]

@app.get("/retrieve-mvp-builder")
def get_mvp_builder(session_id):
    return [i for i in collection.find({"module":"mvp builder","session_id":session_id})][-1]

@app.get("/retrieve-feedback-analyzer")
def get_feedback_analyzer(session_id):
    return [i for i in collection.find({"module":"feedback analyzer","session_id":session_id})][-1]
