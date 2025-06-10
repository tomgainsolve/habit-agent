from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator, model_validator

class HabitType(str, Enum):
    binary = "binary"
    numeric = "numeric"
    categorical = "categorical"

class RuleType(str, Enum):
    is_done = "is_done"
    greater_equal = ">="
    equal = "=="
    in_set = "in"

class Rule(BaseModel):
    type: RuleType
    value: Optional[Union[int, str, List[str]]] = None

    @model_validator(mode="after")
    def check_value_required_for_non_is_done(self):
        if self.type != RuleType.is_done and self.value is None:
            raise ValueError("value is required for this rule type")
        return self

class Habit(BaseModel):
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    type: HabitType
    category: Optional[str] = None
    rule: Rule
    color: Optional[str] = None

class Entry(BaseModel):
    id: str = Field(..., min_length=1)
    habit_id: str = Field(..., min_length=1)
    date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")  # YYYY-MM-DD
    value: Optional[Union[bool, int, str]] = None 