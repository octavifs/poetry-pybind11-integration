#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int add(int i, int j) {
    return i + j;
}

long fib(long n) {
    if (n < 2) {
        return 1;
    }
    return fib(n-2) + fib(n-1);
}

class FibHolder {
    public:
        FibHolder(const std::vector<int> &fib_values)
            : fib_shit(fib_values) {}
        static FibHolder create(const std::vector<int> &fib_shit) {
            return FibHolder(fib_shit);
        }

        long do_fib(int idx) {
            return fib(fib_shit.at(idx));
        }
    private:
        std::vector<int> fib_shit;
};

namespace py = pybind11;

PYBIND11_MODULE(pybind11_extension, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------
        .. currentmodule:: pybind11_extension
        .. autosummary::
           :toctree: _generate
    )pbdoc";

    m.def("cpp_fib", &fib, R"pbdoc(
        Give fibonnacci sequence value for a given number.
    )pbdoc");

    m.def("cpp_fib_nogil", &fib, py::call_guard<py::gil_scoped_release>(), R"pbdoc(
        Give fibonnacci sequence value for a given number.
    )pbdoc");

    py::class_<FibHolder> fib_holder(m, "FibHolder", R"pbdoc(
        Class that will serialize context to C++, so you can run C++ functions on it later.
    )pbdoc");
    fib_holder
        .def(py::init<>(&FibHolder::create))
        .def("do_fib", &FibHolder::do_fib)
        .def("do_fib_nogil", &FibHolder::do_fib, py::call_guard<py::gil_scoped_release>());
}
