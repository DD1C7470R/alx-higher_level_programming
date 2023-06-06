#include "lists.h"
/**
 * insert_node - insert node into a sorted list
 * @head: head of list
 * @number: number to be inserted
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *new;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			runner->next = new;
			return (new);
		}
		runner = runner->next;
	}

	new->next = NULL;
	runner->next = new;
	return (new);
}

