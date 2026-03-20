# tests/test_main.py

import sys
import os

# Allow imports from the src folder without installing the package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import calculate_bmi, bmi_category, pounds_to_kg


# ── Conversion ───────────────────────────────────────────────────

def test_pounds_to_kg():
    assert pounds_to_kg(154) == 69.8532

def test_pounds_to_kg_small():
    assert pounds_to_kg(100) == 45.3592


# ── BMI calculation ──────────────────────────────────────────────

def test_normal_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_bmi_from_pounds():
    # 154 lb converted correctly: 69.8532 kg → BMI 22.82, NOT 50.32
    weight_kg = pounds_to_kg(154)
    assert calculate_bmi(weight_kg, 1.75) == 22.81

def test_zero_height_raises():
    try:
        calculate_bmi(70, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass


# ── Category ─────────────────────────────────────────────────────

def test_category_underweight():
    assert bmi_category(17.0) == "Underweight"

def test_category_normal():
    assert bmi_category(22.86) == "Normal weight"

def test_category_overweight():
    assert bmi_category(27.5) == "Overweight"

def test_category_obese():
    assert bmi_category(32.0) == "Obese"


# ── Manual runner (no pytest required) ───────────────────────────

if __name__ == "__main__":
    tests = [
        test_pounds_to_kg,
        test_pounds_to_kg_small,
        test_normal_bmi,
        test_bmi_from_pounds,
        test_zero_height_raises,
        test_category_underweight,
        test_category_normal,
        test_category_overweight,
        test_category_obese,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {t.__name__}  →  {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
