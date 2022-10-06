from pybind11_extension import FibHolder, cpp_fib, cpp_fib_nogil


def test_cpp_fib():
    assert cpp_fib(5) == 8


def test_cpp_fib_no_gil():
    assert cpp_fib_nogil(6) == 13


def test_fib_holder():
    numbers = [*range(1, 10)]
    holder = FibHolder(numbers)
    assert numbers[5] == 6
    assert holder.do_fib(5) == 13
