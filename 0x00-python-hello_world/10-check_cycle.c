#include "lists.h"
/**
 * check_cycle - checks if  a singly linked list has a cycle in it
 * @list: list
 *
 * Return: 0 if no cycle , else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL || list->next == NULL)
	{
	return (0);
	}
	while (slow && fast && fast->next)
	{
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
	{
	return (1);
	}
	}
	return (0);
}
