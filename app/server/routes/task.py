from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_task,
    delete_task,
    retrieve_task,
    retrieve_tasks,
    update_task,
)
from app.server.models.task import (
    ErrorResponseModel,
    ResponseModel,
    TaskSchema,
    UpdateTaskModel,
)

router = APIRouter()