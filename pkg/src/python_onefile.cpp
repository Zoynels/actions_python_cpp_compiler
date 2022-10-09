#pragma once
#define _SILENCE_CXX17_UNCAUGHT_EXCEPTION_DEPRECATION_WARNING
#include <pybind11/pybind11.h>
#include <pybind11/chrono.h>
#ifdef _DEBUG
#undef _DEBUG
#include <Python.h>
#define _DEBUG
#else
#include <Python.h>
#endif
#include <iostream>

const char* echo(const char* ping) {
	std::cout << "echo: std::cout" << std::endl;
	std::printf("%s", "echo: std::printf\n");
	std::puts("echo: std::puts"); // also writes '\n' afterward
	fprintf(stdout, "echo: fprintf::stdout\n");
	fprintf(stderr, "echo: fprintf::stderr\n");
	PyRun_SimpleString("print('print(\"via PyRun_SimpleString\")')"); // shows in jupyter, but msg should be escaped

	return ping;
}

PYBIND11_MODULE(cpp_module_test, m) {
	m.attr("__version__") = "0.0.1";
	m.def("echo", &echo);
}


