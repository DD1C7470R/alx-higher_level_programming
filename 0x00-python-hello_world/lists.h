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
} l_node;

size_t print_list(const l_node *head);
l_node *add_node(l_node **head, const int num);
void free_list(l_node *head);
int check_cycle(l_node *list);

#endif /* LISTS_H */

