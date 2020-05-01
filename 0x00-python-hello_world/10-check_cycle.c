#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - will check if a linked list has a cycle
 * @list: variable
 * Return: 0
 */
int check_cycle(listint_t *list)
{

	listint_t *i = list, *t = list->next;

	if (list == NULL)
	{
		return (0);
	}

	while (i != t && t != NULL)
	{
		i = i->next;
		t = t->next;
		if (t == NULL)
		{
			break;
		}
		t = t->next;
	}
	if (i == t)
	{
		return (1);
	}
	else
	{
		return (0);
	}
}
