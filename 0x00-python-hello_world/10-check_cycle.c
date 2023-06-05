#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: pointer to a linked list
 *
 * Return: 1 if loop exists, 0 if not
 */
int check_cycle(l_node *list)
{
	l_node *jump = list;
	l_node *initial = list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	while (jump->next != NULL)
	{
		jump = jump->next->next;
		initial = initial->next;

		if (initial == jump)
			return (1);
	}
	return (0);
}

