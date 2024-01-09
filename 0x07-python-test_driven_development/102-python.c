#include <Python.h>

void print_python_string(PyObject *p)
{
    Py_ssize_t len = 0;
    const wchar_t *str = NULL;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf(" [ERROR] Invalid String Object\n");
        return;
    }

    str = PyUnicode_AsUnicode(p);
    len = PyUnicode_GetLength(p);

    printf(" type: %s\n", Py_TYPE(p)->tp_name);
    printf(" length: %ld\n", len);
    printf(" value: %ls\n", str);
}
