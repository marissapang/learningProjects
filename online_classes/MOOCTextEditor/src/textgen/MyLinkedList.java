package textgen;

import java.util.AbstractList;


/** A class that implements a doubly linked list
 * 
 * @author UC San Diego Intermediate Programming MOOC team
 *
 * @param <E> The type of the elements stored in the list
 */
public class MyLinkedList<E> extends AbstractList<E> {
	LLNode<E> head;
	LLNode<E> tail;
	int size;

	/** Create a new empty LinkedList */
	public MyLinkedList() {
		// TODO: Implement this method
		head = new LLNode<E>(null);
		tail = new LLNode<E>(null);
		size = 0;
	}

	/**
	 * Appends an element to the end of the list
	 * @param element The element to add
	 */
	public boolean add(E element ) 
	{
		// TODO: Implement this method
		LLNode<E> newNode = new LLNode<E>(element);
		if (tail.prev == null) { // if LinkedList is empty
			tail.prev = newNode;
			head.next = newNode;
			newNode.prev = head;
			newNode.next = tail;
		} else { // if the LinkedList wasn't empty
			newNode.prev = tail.prev;
			newNode.next = tail;
			tail.prev = newNode;
			newNode.prev.next = newNode;
		}
		// change current tail pointer to point to element for next
		// have element next be the tail node, prev be current end
		return true;
	}

	/** Get the element at position index 
	 * @throws IndexOutOfBoundsException if the index is out of bounds. */
	public E get(int index) 
	{
		// TODO: Implement this method.
		if (index < 0 || index >= this.size()) {
			throw new IndexOutOfBoundsException();
		}
		
		int i = 0;
		LLNode<E> node = head.next;
		while (i < index) {
			node = node.next;
			i++;
		}
		
		return node.data;
	}

	/**
	 * Add an element to the list at the specified index
	 * @param The index where the element should be added
	 * @param element The element to add
	 */
	public void add(int index, E element ) 
	{	
		// TODO: Implement this method

		if (index < 0 || index > this.size()) {
			throw new IndexOutOfBoundsException();
		}
		
		if (element == null) {
			throw new NullPointerException();
		}
		
		// get the index-1, and make next this element, 
		int i = 0;
		LLNode<E> currNode = head;
		
		while (i < index) {
			i++;
			currNode = currNode.next;
		}
		
		LLNode<E> newNode = new LLNode<E>(element);
		
		
		newNode.next = currNode.next;
		newNode.prev = currNode;
		
		currNode.next = newNode;
		
		if (newNode.next == null) {
			tail.prev = newNode;
		} else {
			newNode.next.prev = newNode;
		}
		
		
	
		
		
	}


	/** Return the size of the list */
	public int size() 
	{	
		LLNode<E> currNode = head;
		int count = 0;
		
		while (currNode.next != null) {
			count += 1;
			currNode = currNode.next;
		}
		
		if (count > 0) {
			count -= 1;
		}
		return count;
	}

	/** Remove a node at the specified index and return its data element.
	 * @param index The index of the element to remove
	 * @return The data element removed
	 * @throws IndexOutOfBoundsException If index is outside the bounds of the list
	 * 
	 */
	public E remove(int index) 
	{
		if (index < 0 || index > this.size()) {
			throw new IndexOutOfBoundsException();
		}
		
		int i = 0;
		LLNode<E> currNode = head.next;
		
		while (i < index) {
			i++;
			currNode = currNode.next;
		}
		
		if (currNode.prev != null) {
			currNode.prev.next = currNode.next;
		}
		
		if (currNode.next != null) {
			currNode.next.prev = currNode.prev;
		}
		
		
		
		return currNode.data;
	}

	/**
	 * Set an index position in the list to a new element
	 * @param index The index of the element to change
	 * @param element The new element
	 * @return The element that was replaced
	 * @throws IndexOutOfBoundsException if the index is out of bounds.
	 */
	public E set(int index, E element) 
	{
		if (index < 0 || index >= this.size()) {
			throw new IndexOutOfBoundsException();
		}
		
		if (element == null) {
			throw new NullPointerException();
		}
		
		// TODO: Implement this method
		int i = 0;
		LLNode<E> currNode = head.next;
		while (i < index) {
			i++;
			currNode = currNode.next;
		}
		
		E oldData = currNode.data;
		currNode.data = element;
		
		return oldData;
	}   
}

class LLNode<E> 
{
	LLNode<E> prev;
	LLNode<E> next;
	E data;

	// TODO: Add any other methods you think are useful here
	// E.g. you might want to add another constructor

	public LLNode(E e) 
	{
		this.data = e;
		this.prev = null;
		this.next = null;
	}
	
	public LLNode(E e, LLNode<E> prev, LLNode<E> next) {
		this.data = e;
		this.prev = prev;
		this.next = next;
	}

}
