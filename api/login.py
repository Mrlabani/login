from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

COOKIES = {
    "ndus": "YvuYYdkpeHuihGw9OEigqSKA9NybL_DX5x74XMDz",
    "ndut_fmt": "4CC0910C280E2FCEAFE54757CB673582F6AD3599E7774017843952D6EC551A16",
    "browserid": "oIGAo4oY1Id2W3x1tciwWVawHj8vEf1jK48QhN6lbQmpu2jagQsDrYYzXOU=",
    "_ga": "GA1.1.1451522782.1745129387",
    "_ga_06ZNKL8C2E": "GS1.1.1745129386.1.0.1745129387.59.0.0",
    "ab_ymg_result": "{\"data\":\"...\",\"key_id\":\"66\",\"sign\":\"e3552bd4\"}",
    "csrfToken": "p1u0wPlI1028kITtG9ygs1tD",
    "__bid_n": "19651d00290991d4974207",
    "ab_sr": "1.0.1_YzdlYzZmNjZj...",
    "lang": "en"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://terabox.com/"
}

@app.get("/api/login")
async def login():
    url = "https://www.terabox.com/api/user/getinfo"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=HEADERS, cookies=COOKIES)
            if response.status_code == 200 and response.json().get("errno") == 0:
                return JSONResponse(content={
                    "status": "success",
                    "user_info": response.json().get("userinfo", {})
                })
            return JSONResponse(content={
                "status": "failed",
                "message": "Invalid or expired cookies"
            }, status_code=403)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
      
