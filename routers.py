from fastapi import APIRouter,Depends
from typing import Annotated
from schemas import STask, STaskAdd,STaskId
from repository import TaskRepository

router = APIRouter(
    prefix = '/tasks',
    tags = ['Таски'],

)

@router.post("")
async def add_task(
    task: Annotated[STaskAdd,Depends()],
) -> STaskId:
    new_task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": new_task_id}


@router.get("")
async def get_tasks() ->list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks