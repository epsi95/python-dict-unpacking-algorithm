# python-dict-unpacking-algorithm
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
