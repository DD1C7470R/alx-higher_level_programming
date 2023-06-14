#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints a list
 * @p: the python object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	char *item_type = NULL;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		item_type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, item_type);
	}
}


/**
 * print_python_bytes - prints bytes for python
 * @p: the python object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t i;
	char *bytes_data = PyBytes_AsString(p);

	if (!bytes_data)
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_data);

	printf("  first %ld bytes: ", (size < 10 ? size + 1 : 10));
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", bytes_data[i]);
		if (i + 1 < size && i + 1 < 10)
		{
			printf(" ");
		}
	}
	printf("\n");
}

