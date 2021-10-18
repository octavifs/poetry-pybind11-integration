import argparse
import concurrent.futures

from poetry_pybind11_integration import py_fib
from pybind11_extension import cpp_fib, cpp_fib_nogil, FibHolder


BENCHMARKED_FUNCTIONS = {
    "py_fib": py_fib,
    "cpp_fib": cpp_fib,
    "cpp_fib_nogil": cpp_fib_nogil,
    "fib_holder_gil": FibHolder,
    "fib_holder_nogil": FibHolder,
}


def run_benchmark(benchmark_fn_name, fib_value, num_threads):
    fib_values = [fib_value] * num_threads
    benchmarked_fn = BENCHMARKED_FUNCTIONS[benchmark_fn_name]
    
    if benchmarked_fn == FibHolder:
        fh = FibHolder(fib_values)
        fib_values = list(range(len(fib_values)))
        if benchmark_fn_name == "fib_holder_gil":
            benchmarked_fn = fh.do_fib
        else:
            benchmarked_fn = fh.do_fib_nogil
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(benchmarked_fn, fib_values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark python vs pybind11 single and multithreaded")
    parser.add_argument("BENCHMARK", choices=BENCHMARKED_FUNCTIONS.keys())
    parser.add_argument("FIB_VALUE", type=int)
    parser.add_argument("NUM_THREADS", type=int)
    args = parser.parse_args()

    run_benchmark(args.BENCHMARK, args.FIB_VALUE, args.NUM_THREADS)
