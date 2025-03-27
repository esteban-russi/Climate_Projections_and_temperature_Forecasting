import os
import nbformat
from nbconvert import ExecutePreprocessor

# List of specific notebooks to run
NOTEBOOKS_TO_RUN = [
    "01_eda-final.ipynb",
    "02_combine_datasets.ipynb",
    "03_LSTM.ipynb",
    "04_LSTM_with_extend_dataset.ipynb"
]

def run_notebook(notebook_path, timeout=600):
    """Executes a Jupyter notebook and saves the output."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=timeout, kernel_name='python3')

    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        print(f"✅ Successfully executed: {notebook_path}")

    except Exception as e:
        print(f"❌ Error executing {notebook_path}: {e}")

def run_selected_notebooks(folder_path="notebooks"):
    """Runs only the specified Jupyter notebooks in the given folder."""
    for notebook_name in NOTEBOOKS_TO_RUN:
        notebook_path = os.path.join(folder_path, notebook_name)
        if os.path.exists(notebook_path):
            run_notebook(notebook_path)
        else:
            print(f"⚠️ Notebook not found: {notebook_path}")

if __name__ == "__main__":
    run_selected_notebooks("notebooks")  # Change "notebooks" to the correct folder if needed