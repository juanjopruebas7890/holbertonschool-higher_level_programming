#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * palind_rec - Will iterate in a list using recursion
 * @head: variable
 * @tail: variable
 * Return: 0
 */
int palind_rec(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
	{
		return (1);
	}

	if (palind_rec(head, tail->next) == 1 && (*head)->n == tail->n)
	{
		(*head) = (*head)->next;
		return (1);
	}
	else
	{
		return (0);
	}
}

/**
 * is_palindrome - Will check if a linked list is palindrome
 * @head: variable
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	if ((*head)->next == NULL)
	{
		return (1);
	}
	return (palind_rec(head, *head));
}
