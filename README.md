# price-analysis-and-grid-operations
Project featuring fundamental programming exercises in string manipulation, list operations, financial data analysis, and 2D grid processing. It includes an interactive stock price analyzer with menu based tools, and a set of grid functions for creating, copying, modifying, and analyzing matrix style data.

A three-part Python project covering 2D grid manipulation, an interactive stock price analyzer, and a set of fundamental string and list utility functions.

---

## Project Structure

| File | Responsibility |
|---|---|
| `grid_operations.py` | 2D grid creation, traversal, and manipulation |
| `stock_price_analyzer.py` | Interactive CLI tool for analyzing stock price lists |
| `string_and_list_utilities.py` | Core string and list operations built from scratch |

---

## Part 1 — Grid Operations (`grid_operations.py`)

A collection of functions for creating and manipulating 2D lists (grids), including random generation, value counting, copying, and column analysis.

### Usage

```python
from grid_operations import *

# Create a blank 3x4 grid of zeros
g = create_grid(3, 4)

# Create a grid filled with random integers 0-9
g = random_grid(3, 4)
print_grid(g)
# [[3, 7, 1, 0],
#  [5, 2, 9, 4],
#  [0, 6, 3, 8]]

# Create a grid where each cell equals its column index
col_index_grid(3, 4)
# [[0, 1, 2, 3],
#  [0, 1, 2, 3],
#  [0, 1, 2, 3]]

# Count values in range
num_between(g, 3, 7)     # number of cells with value between 3 and 7

# Deep copy a grid
g2 = copy(g)

# Double each cell, capped at a maximum value
double_with_cap(g, cap=10)

# Sum of even numbers in a specific column
sum_evens_in_col(g, colnum=2)
```

### Functions

| Function | Description |
|---|---|
| `create_grid(rows, cols)` | Returns a blank 2D list of zeros |
| `print_grid(grid)` | Prints the grid in 2D formatted form |
| `random_grid(rows, cols)` | Returns a grid filled with random integers 0–9 |
| `col_index_grid(rows, cols)` | Returns a grid where each cell equals its column index |
| `num_between(grid, n1, n2)` | Counts cells with values in range `[n1, n2]` |
| `copy(grid)` | Returns a deep copy of the grid |
| `double_with_cap(grid, cap)` | Doubles each cell in place; caps at `cap` if exceeded |
| `sum_evens_in_col(grid, col)` | Returns the sum of even values in a given column |

---

## Part 2 — Stock Price Analyzer (`stock_price_analyzer.py`)

An interactive command-line program for analyzing a list of daily stock prices. The user inputs a price list and can run various analyses through a menu-driven interface.

### Usage

```
python stock_price_analyzer.py
```

Then call `tts()` in the Python shell:

```python
from stock_price_analyzer import tts
tts()
```

**Example session:**
```
(0) Input a new list of prices
(1) Print the current prices
(2) Find the latest price
(3) Find the average price
(4) Find the max price and its day
(5) Find the min single-day change and its day
(6) Test a threshold
(7) Your investment plan
(8) Quit

Enter your choice: 0
Enter a new list of prices: [12.5, 15.0, 11.0, 18.5, 14.0]

Enter your choice: 7
 Buy on day 0 at price 12.5
Sell on day 3 at price 18.5
Total profit: 6.0
```

### Functions

| Function | Description |
|---|---|
| `avg_price(prices)` | Returns the mean price across all days |
| `max_day(prices)` | Returns the index of the highest price day |
| `min_change_day(prices)` | Returns the index of the day with the smallest price change from the previous day |
| `any_above(prices, n)` | Returns `True` if any price exceeds the threshold `n` |
| `find_tts(prices)` | Returns `[buy_day, sell_day, profit]` for the optimal buy/sell pair |
| `tts()` | Main interactive loop |

### Investment Strategy Note

`find_tts()` uses a brute-force O(n²) approach — it checks every possible buy/sell day pair to find the maximum profit. This is correct but could be optimized to O(n) using a single-pass algorithm for large datasets.

---

## Part 3 — String & List Utilities (`string_and_list_utilities.py`)

A set of fundamental string and list operations implemented from scratch without using Python's built-in shortcuts.

### Usage

```python
from string_and_list_utilities import repeat, contains, add, replace

# Repeat a string n times
repeat('ab', 3)           # 'ababab'
repeat('hi', 0)           # ''

# Check if a character exists in a string
contains('hello', 'e')    # True
contains('hello', 'z')    # False

# Element-wise addition of two lists (zero-pads the shorter one)
add([1, 2, 3], [10, 20])       # [1, 12, 23]
add([5], [1, 2, 3])            # [6, 2, 3] → pads [5] to [0, 0, 5]

# Replace all occurrences of a value in a list (in place)
vals = [1, 2, 3, 2, 1]
replace(vals, old=2, new=99)
# vals is now [1, 99, 3, 99, 1]
```

### Functions

| Function | Description |
|---|---|
| `repeat(s, n)` | Returns a string with `n` copies of `s` concatenated |
| `contains(s, c)` | Returns `True` if character `c` appears in string `s` |
| `add(vals1, vals2)` | Returns element-wise sum of two lists; zero-pads the shorter one on the left |
| `replace(vals, old, new)` | Replaces all occurrences of `old` with `new` in `vals` (in place) |

---

## Requirements

- Python 3.x
- No external libraries required

---

## Limitations

- `stock_price_analyzer.py` — `find_tts()` uses O(n²) brute force; inefficient for large price lists
- `stock_price_analyzer.py` — prices are entered via `eval()`, which executes arbitrary input; not safe for untrusted environments
- `grid_operations.py` — `double_with_cap()` modifies the grid in place without returning it, which may be unexpected
- `string_and_list_utilities.py` — `replace()` modifies the list in place and returns `None`; callers must not expect a return value
