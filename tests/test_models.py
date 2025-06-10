import pytest
from pydantic import ValidationError
from app.models import Habit, Entry, Rule, RuleType, HabitType

def test_valid_habit_binary():
    habit = Habit(
        id="h1",
        name="Drink Water",
        type=HabitType.binary,
        rule=Rule(type=RuleType.is_done),
    )
    assert habit.id == "h1"
    assert habit.type == HabitType.binary

def test_valid_habit_numeric():
    habit = Habit(
        id="h2",
        name="Steps",
        type=HabitType.numeric,
        rule=Rule(type=RuleType.greater_equal, value=10000),
    )
    assert habit.rule.value == 10000

def test_invalid_habit_missing_rule_value():
    with pytest.raises(ValidationError):
        Habit(
            id="h3",
            name="Pushups",
            type=HabitType.numeric,
            rule=Rule(type=RuleType.greater_equal),  # value missing
        )

def test_invalid_habit_missing_name():
    with pytest.raises(ValidationError):
        Habit(
            id="h4",
            name="",
            type=HabitType.binary,
            rule=Rule(type=RuleType.is_done),
        )

def test_valid_entry():
    entry = Entry(
        id="e1",
        habit_id="h1",
        date="2024-06-01",
        value=True,
    )
    assert entry.value is True

def test_invalid_entry_bad_date():
    with pytest.raises(ValidationError):
        Entry(
            id="e2",
            habit_id="h1",
            date="01-06-2024",
            value=True,
        )

def test_invalid_entry_missing_id():
    with pytest.raises(ValidationError):
        Entry(
            id="",
            habit_id="h1",
            date="2024-06-01",
            value=True,
        ) 