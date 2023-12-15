# -*- coding: utf-8 -*-
import json
import redis
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins (*), adjust as needed for production use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Redis 服务器的配置信息，包括主机地址、端口号和密码
redisConfig = {
    "host": "127.0.0.1",
    "port": 6379,
    "password": "123456",
    "db": 0
}

# 创建与 Redis 数据库的连接
redisClient = redis.Redis(**redisConfig)



@app.post("/api/saveCookie")
async def save_cookies(data: Dict):
    url = data['url']
    cookies_list = data['cookies']
    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies_list}
    redisClient.hset('EditThisCookie:cookie', url, json.dumps(cookies_dict))
    return {"message": "Cookies and token saved successfully"}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8060)
