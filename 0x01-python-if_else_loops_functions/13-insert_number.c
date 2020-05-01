#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: value in singly linked list
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *t = *head, *t2;

	if (head == NULL)
	{
		return (NULL);
	}
	node = malloc(sizeof(listint_t));
	if (node == NULL)
	{
		return (NULL);
	}

	node->n = number;
	if (t == NULL || t->n >= number)
	{
		node->next = t, *head = node;
		return (node);
	}
	t2 = t->next;
	while (t && t2 && (t2->n < number))
	{
		t = t->next, t2 = t->next;
	}

	t->next = node, node->next = t2;
	return (node);
}
