from typing import Annotated
from fastapi import Depends
from schema import STaskAdd
from fastapi import APIRouter
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',

)


@router.post('')
async def add_tasks(
        task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}

@router.get('')
async def get_task():
    tasks = await TaskRepository.find_all()

    return {'data': tasks}
