# generated by fastapi-codegen:
#   filename:  sprints.yaml
#   timestamp: 2024-11-15T21:53:53+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field


class Status(Enum):
    closed = 'closed'
    current = 'current'


class TimeInterval(BaseModel):
    class Config:
        extra = Extra.forbid

    from_: Optional[datetime] = Field(None, alias='from')
    to: Optional[datetime] = None


class State(Enum):
    Normal = 'Normal'


class Priority(Enum):
    High = 'High'
    Low = 'Low'
    Middle = 'Middle'
    Crit = 'Crit'


class Type(Enum):
    Defect = 'Defect'
    Task = 'Task'
    History = 'History'
    SubTask = 'SubTask'


class Status2(Enum):
    Closed = 'Closed'
    Testing = 'Testing'
    Analyse = 'Analyse'
    Created = 'Created'
    OnHold = 'OnHold'
    Locality = 'Locality'
    DeclineByOwner = 'DeclineByOwner'
    Done = 'Done'
    InProgress = 'InProgress'
    Approving = 'Approving'
    STFinished = 'STFinished'
    ST = 'ST'
    Fixing = 'Fixing'
    Development = 'Development'
    Waiting = 'Waiting'
    ReadyToDevelop = 'ReadyToDevelop'


class Resolution(Enum):
    Done = 'Done'
    Decline = 'Decline'
    DeclineByOwner = 'DeclineByOwner'


class ChangeType(Enum):
    CREATED = 'CREATED'
    FIELD_CHANGED = 'FIELD_CHANGED'


class History(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    property_name: str
    date: str
    version: int
    change_type: Optional[ChangeType] = None
    change: str


class SprintsUploadPostRequest(BaseModel):
    files: Optional[List[bytes]] = None


class SprintsListFilter(BaseModel):
    class Config:
        extra = Extra.forbid

    ids: List[str]
    dates: TimeInterval


class SprintWithoutTask(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    name: str
    status: Status
    dates: TimeInterval


class Tiket(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    name: str
    area: str
    state: State
    priority: Priority
    number: str
    estimation: Optional[int] = Field(None, description='Estimate time in seconds')
    spent: Optional[int] = Field(None, description='Spent time in seconds')
    type: Type
    status: Status2
    resolution: Optional[Resolution] = None
    workgroup: Optional[str] = None
    parent_ticket_id: Optional[str] = None
    create_date: datetime
    created_by: str
    update_date: datetime
    updated_by: Optional[str] = None
    assigne: Optional[str] = None
    owner: Optional[str] = None
    due_date: Optional[date] = None
    history_actions: List[History]


class SprintsListResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    sprints: List[SprintWithoutTask]


class Sprint(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str
    name: str
    status: Status
    dates: TimeInterval
    tickets: List[Tiket]
