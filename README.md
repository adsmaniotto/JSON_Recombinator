# JSON_Recombinator
A simple JSON recombinator in Python, inspired by [Avant's Data Engineering Recombinator Challenge](https://github.com/avantcredit/data-engineer-interview). The script accepts a JSON file in the command line, and outputs a JSON with keys mapped to a list of values.

Example of CLI terminal using a list of lists:
```
> python json_recombinator.py list_list.json`
Input: [ ["a","b","c"], [1,2,null], [null,3,4], [5,null,6] ]
Output: {'a': [1, None, 5], 'b': [2, 3, None], 'c': [None, 4, 6]}
```

Example using a list of dictionaries:
```
> python json_recombinator.py list_obj.json
Input: [ { "a":1, "b":2 }, { "b":3, "c":4 }, { "c":6, "a":5 } ]
Output: {'a': [1, None, 5], 'b': [2, 3, None], 'c': [None, 4, 6]}
```
