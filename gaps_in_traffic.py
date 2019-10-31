from itertools import chain

flatten = chain.from_iterable
LEFT, RIGHT = 1, -1

def join_distances(data, offset=0):
    data = sorted(flatten(((start, LEFT), (stop + offset, RIGHT))
            for start, stop in data))
    c = 0
    for value, label in data:
        if c == 0:
            x = value
        c += label
        if c == 0:
            yield x, value - offset

def widestGap(n, start, finish):
    # Write your code here
    
    # 1) Zip start + finish and convert to a list. Will have [(start1, finish1), (start2, finish2), ..., (startn, finishn)]
    # 2) Join overlaped distances and convert to a list. Will have [(2, 99)] for a list like [(2, 90), (10, 95), (80, 99)]
    distances = list(join_distances(list(zip(start, finish))))
    
    # Calculate the gap before the first distance
    # Difference from 1 to the first start distance
    widest = distances[0][0] - 1
    
    # Calculate the gap after the last distance
    # Difference from the last finish distance and the distance of the road
    last_gap = n - distances[len(distances)-1][1]
    
    # If the last gap is greater than the first gap, it will be the widest
    widest = last_gap if last_gap > widest else widest
    
    # Find the widest gap between distances
    for i in range(len(distances) - 1):
    
        # Gap is the start of the next distance -1 and the finish of the current distance
        gap = (distances[i+1][0] - 1) - distances[i][1]
        
        # If the current gap is greater than the current widest gap, this is the new widest gap
        widest = gap if gap > widest else widest

    return widest
    
def runTestScenario(n, start, finish, expected):

    print('Scenario:')
    print(f'n.......: {n}')
    print(f'start...: {start}')
    print(f'finish..: {finish}')
    print(f'expected: {expected}')
    print('')
    
    try:
        result = widestGap(n, start, finish)
        assert result == expected
        print('Result: passed')
    except AssertionError:
        print(f'Result: failed. Got {result}, expect {expected}')
    
    print('---------------------------------------------')

if __name__ == "__main__":

    print('')
    print('---------------------------------------------')
    
    n = 10
    start = [3, 8]
    finish = [4, 9]
    expected = 3
    
    runTestScenario(n, start, finish, expected)
    
    n = 10
    start = [1, 2, 6, 6]
    finish = [4, 4, 10, 8]
    expected = 1
    
    runTestScenario(n, start, finish, expected)
    
    n = 100
    start =  [22,75,26,45,72,81,47,29,97, 2,75,25,82,84,17,56,32, 2,28,37,57,39,18,11,79, 6,40,68,68,16,40,63,93,49,91,10,55,68,31,80]
    finish = [51,92,59,60,77,95,61,68,98,90,87,39,94,85,67,74,41,65,78,80,85,93,87,82,83,16,89,81,69,72,80,77,99,90,92,95,68,70,75,97]
    expected = 1

    runTestScenario(n, start, finish, expected)