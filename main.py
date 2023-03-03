from fastapi import FastAPI
from app.routers import api_users


app = FastAPI()



@app.on_event("startup")
async def startup():
    pass




@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(api_users.router, prefix="/api/v1/users")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
