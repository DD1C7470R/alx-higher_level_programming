#include "lists.h"

/**
 * print_list - prints all elements of a list
 * @head: pointer to head of list
 * Return: number of nodes
 */
size_t print_list(const l_node *head)
{
	const l_node *current;
	unsigned int num; /* number of nodes */

	current = head;
	num = 0;
	while (current != NULL)
	{
		printf("%i\n", current->data);
		current = current->next;
		num++;
	}

	return (num);
}

/**
 * add_node - adds a new node at the beginning of a l_node list
 * @head: pointer to a pointer of the start of the list
 * @num: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
l_node *add_node(l_node **head, const int num)
{
	l_node *new;

	new = malloc(sizeof(l_node));
	if (new == NULL)
		return (NULL);

	new->data = num;
	new->next = *head;
	*head = new;

	return (new);
}


/**
 * free_list - frees a l_node list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_list(l_node *head)
{
	l_node *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

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

