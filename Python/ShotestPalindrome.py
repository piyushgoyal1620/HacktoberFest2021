# given an string as input return the shortest palindrome
# for more info about problem statement: https://leetcode.com/problems/shortest-palindrome/


def shortestPalindrome(self, input: str) -> str:
        """
        KMP algorithm
        time-space complexity: O(n), O(n)
        """
    if input =="": return input #base case
    pattern = input + input[::-1]
        
    prefix = [-1] * len(pattern)
    j = -1
    for i in range(1, len(pattern)):
      while j >- 1 and pattern[j+1] != pattern[i]:
        j = prefix[j]
      j += 1
      prefix[i] = j

    i = prefix[-1]
    while i >= len(input):
      i = prefix[i]
    return input[i+1:][::-1] + input
