def convert(s: str, numRows: int) -> str:

    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list of strings to represent each row
    rows = [''] * numRows
    current_row = 0
    down = True  # Start by moving down

    for char in s:
        # Add the current character to the current row
        rows[current_row] += char

        # Check if we need to move down or up
        if down:
            if current_row < numRows - 1:
                current_row += 1
            else:
                # Switch to moving up
                down = False
                current_row -= 1
        else:
            if current_row > 0:
                current_row -= 1
            else:
                # Switch to moving down
                down = True
                current_row += 1
        print(rows)

    # Combine all rows to form the final zigzag string
    return ''.join(rows)

# Example usage
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))  # Output: "PINALSIGYAHRPI"
