# simple-mpl-hand

I wanted a simple 3D hand model to visualize hand movements in python without the need for external models or software, so I built this.

It's super simple and has room for optimization, but it gets the job done.


SimpleHand:
![hand moving](hand_v2.gif)

SuperSimpleHand:
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
from simple_mpl_hand import SimpleHand
hand = SimpleHand()
hand.set_flex(th=0, idx=0, mid=0.5, ri=0.4, pi=0.3)
hand.draw()
plt.show()
```