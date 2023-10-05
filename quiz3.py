def solution(S):
    letter_counts = {}

    for letter in S:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    odd_count = 0
    for count in letter_counts.values():
        if count % 2 == 1:
            odd_count += 1

    return odd_count



def reverse_words(S):
    words = S.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


# Test the solution function
print(solution("iankiguru"))