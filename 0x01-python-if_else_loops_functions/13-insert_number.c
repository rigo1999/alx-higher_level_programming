#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Tolulope Fakunle
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *next;

	next = malloc(sizeof(listint_t));
	if (next = NULL)
		return (NULL);
	next->n = number;

	if (node == NULL || node->n >= number)
	{
		next->next = node;
		*head = next;
		return (next);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	next->next = node->next;
	node->next = next;

	return (new);
}
