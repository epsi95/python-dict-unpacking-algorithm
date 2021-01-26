# python-dict-unpacking-algorithm
## assuming
1. No `set` or `tuple` datastructure in the original data
2. no `<` or `>` sign in the original data

Convert
```python
{"Key1.Key2.Key3(someparameter)": 
  {"balh.Key1": [{'a1.a2':1, 'b':2}]}}
```

to

```python
{'Key1': 
  {'Key2': {'Key3(someparameter)': 
      {'balh': 
            {'Key1': [{'a1': 
                        {'a2': 1},
                       'b': 2}]}}}}}
```
