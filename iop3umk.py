import numpy as np
import h5py

# Save a 1D or 2D NumPy array to a plain text file
def write_txt(filepath, array):
    np.savetxt(filepath, array)

# Load a NumPy array from a plain text file
def read_txt(filepath):
    return np.loadtxt(filepath)

# Save a NumPy array to an HDF5 checkpoint file
def write_checkpoint(filepath, array, name="data"):
    with h5py.File(filepath, "w") as f:
        f.create_dataset(name, data=array)

# Load a NumPy array from an HDF5 checkpoint file
def read_checkpoint(filepath, name="data"):
    with h5py.File(filepath, "r") as f:
        return f[name][:]

