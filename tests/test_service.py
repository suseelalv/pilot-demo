import pytest
from service import TaskService


def test_add_task():
    service = TaskService()
    task = service.add_task("Prepare release notes", "high", "2026-05-30")

    assert task.id == 1
    assert task.title == "Prepare release notes"
    assert task.priority == "high"
    assert task.completed is False
    assert task.due_date == "2026-05-30"


def test_complete_task():
    service = TaskService()
    task = service.add_task("Write tests")

    result = service.complete_task(task.id)

    assert result is True
    assert service.list_tasks("completed")[0].id == task.id


def test_list_tasks_by_status():
    service = TaskService()
    t1 = service.add_task("Task 1")
    t2 = service.add_task("Task 2")
    service.complete_task(t2.id)

    pending = service.list_tasks("pending")
    completed = service.list_tasks("completed")

    assert len(pending) == 1
    assert len(completed) == 1
    assert pending[0].id == t1.id
    assert completed[0].id == t2.id


def test_summary():
    service = TaskService()
    service.add_task("Task 1")
    t2 = service.add_task("Task 2")
    service.complete_task(t2.id)

    result = service.summary()

    assert result["total"] == 2
    assert result["completed"] == 1
    assert result["pending"] == 1


def test_invalid_priority():
    service = TaskService()

    with pytest.raises(ValueError):
        service.add_task("Bad priority task", "urgent")