import pytest
from src.task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    tm.add_task("Купить молоко")
    assert len(tm.get_tasks()) == 1
    assert tm.get_tasks()[0].title == "Купить молоко"

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Сделать домашнее задание")
    tm.complete_task(0)
    assert tm.get_tasks()[0].done is True

def test_invalid_index():
    tm = TaskManager()
    tm.add_task("Задача")
    tm.complete_task(99)
    assert tm.get_tasks()[0].done is False

# Новые тесты для Части 4
def test_remove_task():
    tm = TaskManager()
    tm.add_task("Задача 1")
    tm.add_task("Задача 2")
    tm.remove_task(0)
    assert len(tm.get_tasks()) == 1
    assert tm.get_tasks()[0].title == "Задача 2"

def test_remove_invalid_index():
    tm = TaskManager()
    tm.add_task("Единственная задача")
    tm.remove_task(5)
    assert len(tm.get_tasks()) == 1

def test_get_pending_tasks():
    tm = TaskManager()
    tm.add_task("Выполненная")
    tm.add_task("В процессе")
    tm.complete_task(0)
    
    pending = tm.get_pending_tasks()
    assert len(pending) == 1
    assert pending[0].title == "В процессе"
    assert pending[0].done is False