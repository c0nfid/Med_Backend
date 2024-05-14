from fastapi import FastAPI
import uvicorn

from items.views import router as items_router

app = FastAPI()
app.include_router(items_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
