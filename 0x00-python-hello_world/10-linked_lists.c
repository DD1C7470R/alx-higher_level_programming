#include "lists.h"

/**
 * print_listint - prints all elements of a list
 * @head: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *head)
{
	const listint_t *current;
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
 * add_nodeint - adds a new node at the beginning of a l_node list
 * @head: pointer to a pointer of the start of the list
 * @num: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int num)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->data = num;
	new->next = *head;
	*head = new;

	return (new);
}


/**
 * free_listint - frees a l_node list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

