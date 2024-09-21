def longest_unique_substring(s):
    left = 0
    right = 0
    seen_chars = set()
    max_len = 0
    start_index = 0

    while right < len(s):
        if s[right] not in seen_chars:
            seen_chars.add(s[right])
            right += 1
            if right - left > max_len:
                max_len = right - left
                start_index = left
        else:
            seen_chars.remove(s[left])
            left += 1

    return s[start_index:start_index + max_len], max_len


s = "abcbcgh"
result, length = longest_unique_substring(s)
print(f"Chuỗi con dài nhất không có ký tự trùng lặp là: '{result}' với độ dài: {length}")
