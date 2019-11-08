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
    
### Installation
- Install `FreeCAD`
```
$ sudo apt-get install freecad
```
- Install python packages of `matplotlib`, `ipython`
```
$ pip install -r requirements.txt
```

### Usage
```
$ git clone https://github.com/takayuki5168/CADAnalyzer
$ cd CADAnalyzer
$ python scripts/cad_analyzer.py
```