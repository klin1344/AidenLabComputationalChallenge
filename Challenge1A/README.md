#Aiden Lab Computational Challenge: 1A


###Challenge:
You are given an array bucket_sizes (e.g. [3, 11, 21]) and a target_value (e.g. 492).
The resulting answer should be a 1 or 0 (alternatively true and false)
1 (true) - if the buckets can be used to reach the target value
0 (false) - if they cannot

- You can reuse buckets. 
- You will not be subtracting buckets, simply adding them.
- You are not guaranteed that there are only 2 or 3 buckets, you could be given 15 buckets, or 100 buckets, etc. The examples provided are not an exhaustive list of possible tests.
- You may replace the 1 and 0 with true and false respectively if the language of your choice allows it
- You are not required to know what particular group of buckets was used. The only question is whether the target size can be reached or not.
- target_value can be assumed to be less than 2,147,483,647 (i.e. no need to use longs / you do not need to worry about int overflow for this challenge)


###Solution:
Because buckets can be reused an arbitrary number of times, not used, and arranged in any way, the problem can be solved by the summing [Cartesian products](https://en.wikipedia.org/wiki/Cartesian_product), which are defined as "a mathematical operation that returns a set (or product set or simply product) from multiple sets. That is, for sets A and B, the Cartesian product A × B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B."

We need to find the Cartesian product of length `lower_bound` to a specified `upper_bound` value for a given sequence of numbers.  The `upper_bound` is the greatest possible length that the buckets can be arranged in, and `lower_bound` is the smallest possible length that the buckets can be arranged in.  We find `lower_bound` by dividing the target by the largest bucket, and 'upper_bound` by dividing the target by the smallest bucket.


###How To Use:
Run the solution using Python 2.7.  The program looks for two call-line arguments: `<target>` and `<buckets>`.
`<target>` should be a number, e.g., 128
`<buckets>` should be a list of numbers, separated by commas, should not contain spaces, and should have an opening and closing brace, e.g., `[1,2,3,4]`

####Examples:
#####Arguments
`python sol1a.py 50 [2,4,6]`
#####Output:
`True`

#####Arguments
`python sol1a.py 976 [2,7,9,9]`
#####Output:
`True`

#####Arguments
`python sol1a.py 1 [2,3,5,9]`
#####Output:
`False`

#####Arguments
`python sol1a.py 9 [2,2,2,11]`
#####Output:
`False`
