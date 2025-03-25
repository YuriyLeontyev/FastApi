from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from routers import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
   await delete_tables()
   print("База очищена")
   await create_tables()
   print("База готова")
   yield
   print("Switch_Off")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)




