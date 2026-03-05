import pytest
from app.service import calculate_total, process_payment

def test_calculate_total_ok():
    assert calculate_total("coffee", 2) == 360

def test_calculate_total_zero():
    assert calculate_total("tea", 0) == 0

def test_not_product():
    assert calculate_total("sandwich", 1) == 250

def test_negative_quantity():
    assert calculate_total("coffee", 1) == 180

def test_process_payment_negative():
    assert process_payment(-120) == False