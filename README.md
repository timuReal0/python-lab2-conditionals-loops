# Python Lab 2 – Conditionals and Loops

Short Python programs written for the second lab of an introductory programming course,
solving simple problems with conditional statements and loops.
Each program reads its input from the keyboard and prints the result.

## Problems

| File | Problem | Example |
|------|---------|---------|
| `pb1.py` | Computes the control digit of a number: its digits are summed repeatedly until a single digit remains. | 1971 → 9 |
| `pb2.py` | Finds the date (day.month.year) from a year and the number of the day in that year, taking leap years into account. | year 2004, day 68 → 8.03.2004 |
| `pb13.py` | Checks whether a number is an Armstrong number, i.e. equal to the sum of its digits, each raised to the number of digits. | 153 → True |
| `pb17.py` | Reads numbers until 0 and counts those whose unit digit is greater than the tens digit. | 329 83 99 918 82 10 2412 0 → 3 |
| `pb20.py` | Builds a new number from the digits found at odd positions, counted from left to right. | 9404 → 90 |
| `pb23.py` | Prints how many digits two numbers have in common, and which ones. | 21348 and 14153 → 3 (digits 1, 3, 4) |

## Notes on the solutions

**pb1.py** – uses the fact that the control digit of a number is equal to the remainder
of its division by 9 (or 9 when the number is a nonzero multiple of 9),
so the digits never have to be summed repeatedly.

**pb23.py** – marks which digits appear in each number in an array with 10 positions,
then compares the two arrays to find the common digits.

## How to run

Requires Python 3.6 or newer.

```
python pb1.py
```

Or open any file in IDLE and press **F5** (Run Module).
