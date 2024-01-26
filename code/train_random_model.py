import numpy as np
import random
import gzip
import random
import pickle
from ms.hotdog_model import HotdogModel

hotdog_model = HotdogModel()

# Save the model
with gzip.open('model/hotdog_model.pkl.gz', 'wb') as f:
    pickle.dump(hotdog_model, f)


