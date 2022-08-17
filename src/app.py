from fastapi import FastAPI
from routes.user import user
import uvicorn

app = FastAPI(
    title="USER APIs",
    description="This api is for managing users with CRUD",
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)
app.include_router(user)

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 4000)