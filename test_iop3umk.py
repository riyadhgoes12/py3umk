import os
import numpy as np
from iop3umk import write_txt, read_txt, write_checkpoint, read_checkpoint

# Create sample 2D array
arr = np.array([[1.5, 2.5], [3.5, 4.5]])

# Test text I/O
write_txt("test.txt", arr)
assert np.allclose(arr, read_txt("test.txt")), "Text I/O failed!"

# Test checkpoint I/O
write_checkpoint("test.h5", arr)
assert np.allclose(arr, read_checkpoint("test.h5")), "Checkpoint I/O failed!"

# Clean up temporary test files
os.remove("test.txt")
os.remove("test.h5")

print("All tests passed successfully!")
