# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy==1.26.4", "pip-audit==2.7.3"]
# ///
import numpy as np
rng = np.random.default_rng(42)
print(rng.integers(0, 10, 3).tolist())
