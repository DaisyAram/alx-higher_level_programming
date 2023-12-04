#include <stdio.h>
#include <Python.h>
#include <stdlib.h>
/**
 * print_python_list_info -  function that prints some basic info
 * about Python lists
 * @p: python list
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int item;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (item = 0; item < Py_SIZE(p); item++)
	printf("Element %d: %s\n", item, Py_TYPE(PyList_GetItem(p, item))->tp_name);

}
