# simple-mpl-hand

I wanted a simple 3D hand model to visualize hand movements in python without the need for external models or software, so I built this.

It's super simple and has room for optimization, but it gets the job done.

![hand moving](hand.gif)


#### Installation:

Navigate to the directory and run
```
pip install .
```
or if you want to keep it editable
```
pip install -e .
```

#### Plot a hand:
```python
from simple_mpl_hand import Hand
hand = Hand()
hand.draw(idx_flexion=0, mrs_flexion=0.5, thumb_flexion=1.0)
```