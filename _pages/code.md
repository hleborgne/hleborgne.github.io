---
layout: archive
title: "Code"
permalink: /code/
author_profile: true
classes: wide
---

> most of the code associated to the papers is on github. The link is given with the publication on [the dedicated page](https://hleborgne.github.io/publications/)

## mNRG: comparing several approaches/models through several inhomogeneous benchmarks
The median normalized relative gain (mNRG) was introduced in ou [PAMI 2020 paper](https://arxiv.org/pdf/1712.09708). It allows to compare models or approaches through several benchmarks that can have inhomogeneous metrics (*e.g* classification rate and equal error rate, lhe later being "the lower the better"). In that case, averaging the score over the benchmarks is not a good practice. Youssef Tammazousti identified several criterion to be met to agregate inhomogeneous metrics. mNRG is one of the approaches that addresses most of them (although it is not perfect: see [the paper](https://arxiv.org/pdf/1712.09708)).

Let us assume we have 5 approaches to compare over 4 benchmarks, with the following scores:
```
import numpy as np

IN=np.array([
[0.573, 67.2, 60.8, 68.2],
[0.588, 69.6, 61.7, 70.6],
[0.610, 67.7, 64.7, 71.1],
[0.632, 70.4, 64.3, 73.2],
[0.707, 69.2, 64.7, 71.9]
])
```
The approach on the first line is used as *a reference*. The *theoretical maximal score* must also be provided. We assume it is 1 for the first benchmark and 100 for the other. The agregative score is computed with [the function in mNRG.py](https://hleborgne.github.io/files/mNRG.py) as:

```
from mNRG import mNRG

print(100*mNRG(IN,np.array([1,100,100,100])))
```
The gives the relative merit score of each approach w.r.t the reference: `[ 0.  5.42  8.89 11.79 10.79]` (one chould keep even less significant digits for an article...).
