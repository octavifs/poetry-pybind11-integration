# Example on pybind11 integration with Poetry

This project is an example on how to setup a [*pybind11*](https://pybind11.readthedocs.io/en/stable/) build with [*Poetry*](https://python-poetry.org/).

Lookup at the `build.py` and `pyproject.toml` files for reference. The source code of the C++ extension is under the `pybind11_extension` folder [[link to explanation](https://octavifs.com/post/pybind11-builds-in-poetry/)].

Additionally, the repo contains a few samples and benchmarks on how to use pybind11 to release the GIL and achieve true parallellism in Python with multithreading. Useful if you want to execute CPU bound tasks [[link to explanation](https://octavifs.com/post/pybind11-multithreading-parallellism-python/)].
