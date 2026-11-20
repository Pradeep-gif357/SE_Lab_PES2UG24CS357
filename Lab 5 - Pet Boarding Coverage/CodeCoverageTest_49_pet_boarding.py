
import pytest

from pet_boarding import (
    boarding_fee,
    admission_ok,
    checkout_status,
)


# ---------------- BOARDING FEE TESTS ----------------

def test_within_included_days():
    assert boarding_fee("dog", 1, False) == 0
    assert boarding_fee("cat", 3, False) == 0
    assert boarding_fee("rabbit", 4, False) == 0


def test_invalid_pet_type():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("bird", 3, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("dog", -1, False)


def test_standard_boarding_fees():
    assert boarding_fee("dog", 3, False) == 30
    assert boarding_fee("cat", 4, False) == 20
    assert boarding_fee("rabbit", 5, False) == 20


def test_premium_kennel():
    assert boarding_fee("dog", 3, True) == 0
    assert boarding_fee("cat", 4, True) == 0
    assert boarding_fee("rabbit", 5, True) == 20


def test_more_than_ten_extra_days():
    assert boarding_fee("dog", 13, False) == 495
    assert boarding_fee("dog", 14, False) == 540
    assert boarding_fee("cat", 14, False) == 330


def test_premium_with_extra_days():
    assert boarding_fee("dog", 4, True) == 30
    assert boarding_fee("cat", 5, True) == 20


# ---------------- ADMISSION TESTS ----------------

def test_regular_admission():
    assert admission_ok(4, 2, False) is True
    assert admission_ok(4, 1, False) is False


def test_puppy_admission():
    assert admission_ok(0, 3, False) is False
    assert admission_ok(1, 2, False) is True


def test_senior_admission():
    assert admission_ok(12, 3, True) is True
    assert admission_ok(12, 2, True) is False


# ---------------- CHECKOUT STATUS TESTS ----------------

def test_checkout_open():
    assert checkout_status(15, False, False) == "open"
    assert checkout_status(30, True, False) == "open"
    assert checkout_status(50, True, True) == "open"


def test_checkout_late():
    assert checkout_status(14, False, False) == "late"
    assert checkout_status(15, True, False) == "late"
    assert checkout_status(35, True, True) == "late"


def test_checkout_closed():
    assert checkout_status(-1, False, False) == "closed"
    assert checkout_status(14, True, False) == "closed"
    assert checkout_status(19, True, True) == "closed"


def test_checkout_boundaries():
    assert checkout_status(15, False, False) == "open"
    assert checkout_status(0, False, False) == "late"
    assert checkout_status(50, True, True) == "open"
    assert checkout_status(20, True, True) == "closed"
