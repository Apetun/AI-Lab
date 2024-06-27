from itertools import permutations

def solve_arithmetic(puzzle):
    # Extract unique letters from the puzzle
    letters = set(''.join(puzzle))
    
    # Check if the number of unique letters is more than 10 (impossible for base-10 arithmetic)
    if len(letters) > 10:
        print("Error: Invalid puzzle. More than 10 unique letters.")
        return None
    
    # Initialize solution to None
    solution = None
    
    # Generate permutations of digits for the letters
    for perm in permutations(range(10), len(letters)):
        # Map letters to digits using the current permutation
        mapping = dict(zip(letters, perm))
        
        # Skip permutations where any leading letter maps to 0
        if mapping[puzzle[0][0]] == 0 or mapping[puzzle[1][0]] == 0 or mapping[puzzle[2][0]] == 0:
            continue
        
        # Convert words to numbers using the mapping
        nums = [int(''.join(str(mapping[c]) for c in word)) for word in puzzle]
        
        # Check if the equation holds true and if it's a valid solution
        if sum(nums[:-1]) == nums[-1]:
            if solution is None or all(nums[i] < solution[i] for i in range(len(nums))):
                solution = nums
    
    # If no solution is found, return None
    if solution is None:
        print("No solution found.")
        return None
    
    # Map letters to their corresponding numbers in the solution
    mapping = {letter: str(num) for letter, num in zip(letters, solution)}
    return mapping

# Lab Exercise 1
puzzle1 = ['CROSS', 'ROADS', 'DANGER']
print("Solving Lab Exercise 1:")
solution1 = solve_arithmetic(puzzle1)
if solution1:
    print("Solution:")
    for letter, num in solution1.items():
        print(f"{letter} = {num}")

# Lab Exercise 2
puzzle2 = ['DONALD', 'GERALD', 'ROBERT']
print("\nSolving Lab Exercise 2:")
solution2 = solve_arithmetic(puzzle2)
if solution2:
    print("Solution:")
    for letter, num in solution2.items():
        print(f"{letter} = {num}")

# Lab Exercise 3
puzzle3 = ['MIT', 'MANIPAL', 'MITMAHE']
print("\nSolving Lab Exercise 3:")
solution3 = solve_arithmetic(puzzle3)
if solution3:
    print("Solution:")
    for letter, num in solution3.items():
        print(f"{letter} = {num}")
else:
    print("No solution found.")
