# Day 1 Progress

Topic: Arrays
🎯 Focus Companies: Google, Amazon, Microsoft, Meta
✅ Today’s Sub-Topics (IN DEPTH)

1️⃣ Max / Min Element in Array
2️⃣ Subarrays (Basic Understanding)


1.max,min
Find the maximum and minimum element in an array.
📖 Explanation

The array stores multiple numbers.

max(a) scans the array once and returns the largest value.

min(a) scans the array once and returns the smallest value.

No extra space is used.

⏱️ Interview Insight

Time Complexity: O(n)

Space Complexity: O(1)

🎤 How to Explain in Interview

“I traverse the array once using built-in functions to find the maximum and minimum values efficiently.”



2.subarryas
Print all possible subarrays of an array.

📖 Explanation

A subarray is a continuous part of an array.

Outer loop selects the starting index.

Inner loop selects the ending index.

a[i:j] prints the subarray from index i to j-1.

⏱️ Interview Insight

Time Complexity: O(n²)

Used as a base for:

Maximum subarray sum

Sliding window

Kadane’s algorithm

🎤 How to Explain in Interview

“I fix a starting index and expand the ending index to generate all continuous subarrays.”

🎤 FAANG Interview Round (Professional Answers)

Q1. What is an array?
A: An array is a linear data structure that stores elements in contiguous memory locations.

Q2. Difference between subarray and subsequence?
A: A subarray is continuous, while a subsequence may skip elements.

Q3. Why is max/min O(n)?
A: Every element must be checked at least once.

Q4. Where are subarrays used?
A: In sliding window problems, stock buy/sell, and maximum sum problems.