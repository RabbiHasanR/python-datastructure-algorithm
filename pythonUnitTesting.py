def average(L):
    if not L:
        return None
    return sum(L)/len(L)


def test_average():
    test_cases=[
        {
            'name':'simple case 1',
            'input':[1,2,3],
            'expected':2.0
        },
        {
            'name':'simple case 2',
            'input':[1,2,3,4],
            'expected':2.5
        },
        {
            'name':'simple case 3',
            'input':[1,2,3,4,5],
            'expected':3.0
        },
        {
            'name':'list with one item',
            'input':[100],
            'expected':100.0
        },
        {
            'name':'empty list',
            'input':[],
            'expected':None
        }
    ]
    for test_case in test_cases:
        assert test_case['expected']==average(test_case['input']),test_case['name']

