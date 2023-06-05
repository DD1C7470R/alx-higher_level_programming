#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct link_list - singly linked list
 * @data: integer
 * @next: points to the next node
 */
typedef struct link_list
{
	int data;
	struct link_list *next;
} listint_t;

size_t print_listint(const listint_t *head);
listint_t *add_nodeint(listint_t **head, const int num);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */

