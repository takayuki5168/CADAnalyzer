CAD Analyzer
============

[![Build Status](https://travis-ci.org/takayuki5168/CADAnalyzer.svg?branch=master)](https://travis-ci.com/takayuki5168/CADAnalyzer/)

Library for analyzing CAD data (STEP) with FreeCAD

![sample1](figs/sample1.png)

We can do with this library
- extract edges, vertetexes, faces
- plot edges, vertetexes, faces in 3D

### Requirements
- Python2
    - Python3 is not supported
    
- FreeCAD
```
$ sudo apt-get install freecad
```

### Use from Command
- Install python packages of `matplotlib`, `ipython`
```
$ git clone https://github.com/takayuki5168/CADAnalyzer
$ cd CADAnalyzer
$ pip install -r requirements.txt
```
- Execute
```
$ python scripts/cad_analyzer.py -m models/sample.STEP
```

### Use from Python
- Install CADAnalyzer package
```
$ git clone https://github.com/takayuki5168/CADAnalyzer
$ cd CADAnalyzer
$ pip install --user .
```

- Execute
```
$ ipython
In [1]: from cad_analyzer import CADAnalyzer
In [2]: ca = CADAnalyzer()
In [3]: ca.read_file("models/sample.STEP")
In [4]: ca.plot_edge()