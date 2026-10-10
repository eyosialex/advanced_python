import numpy as np
rng=np.random.default_rng(42)
house_size=rng.uniform(30,300,100)
room_no=rng.integers(1,6,100)
price=(30+15*house_size+
       2*room_no)
y=price.reshape(100,1)


