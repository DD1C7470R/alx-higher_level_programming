#include "lists.h"

/**
 * check_cycle - checks for a loop in a linked list
 * @list: pointer to a linked list
 *
 * Return: 1 if loop exists, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *jump = list;
	listint_t *initial = list;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);

	while (jump != NULL && initial != NULL && jump->next != NULL)
	{
		jump = jump->next->next;
		initial = initial->next;

		if (initial == jump)
			return (1);
	}

	return (0);
}

