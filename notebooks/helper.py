import xarray as xr

def load_datasets(file_paths):
    "Load the six .nc files to return a list of xarray datasets"
    datasets = []
    for path in file_paths:
        ds = xr.open_dataset(path)
        datasets.append(ds)
    return datasets