/**
 * 
 */
package textgen;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Before;
import org.junit.Test;

/**
 * @author UC San Diego MOOC team
 *
 */
public class MyLinkedListTester {

	private static final int LONG_LIST_LENGTH =10; 

	MyLinkedList<String> shortList;
	MyLinkedList<Integer> emptyList;
	MyLinkedList<Integer> longerList;
	MyLinkedList<Integer> list1;
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
		// Feel free to use these lists, or add your own
	    shortList = new MyLinkedList<String>();
		shortList.add("A");
		shortList.add("B");
		emptyList = new MyLinkedList<Integer>();
		longerList = new MyLinkedList<Integer>();
		for (int i = 0; i < LONG_LIST_LENGTH; i++)
		{
			longerList.add(i);
		}
		list1 = new MyLinkedList<Integer>();
		list1.add(65);
		list1.add(21);
		list1.add(42);
		
	}

	
	/** Test if the get method is working correctly.
	 */
	/*You should not need to add much to this method.
	 * We provide it as an example of a thorough test. */
	@Test
	public void testGet()
	{
		//test empty list, get should throw an exception
		try {
			emptyList.get(0);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
			
		}
		
		// test short list, first contents, then out of bounds
		assertEquals("Check first", "A", shortList.get(0));
		assertEquals("Check second", "B", shortList.get(1));
		
		try {
			shortList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			shortList.get(2);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		// test longer list contents
		for(int i = 0; i<LONG_LIST_LENGTH; i++ ) {
			assertEquals("Check "+i+ " element", (Integer)i, longerList.get(i));
		}
		
		// test off the end of the longer array
		try {
			longerList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			longerList.get(LONG_LIST_LENGTH);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		}
		
	}
	
	
	/** Test removing an element from the list.
	 * We've included the example from the concept challenge.
	 * You will want to add more tests.  */
	@Test
	public void testRemove()
	{
		shortList.add("C");
		int a = list1.remove(0);
		assertEquals("Remove: check a is correct ", 65, a);
		assertEquals("Remove: check element 0 is correct ", (Integer)21, list1.get(0));
		assertEquals("Remove: check size is correct ", 2, list1.size());
		
		String b = shortList.remove(1);
		assertEquals("Remove: check b is correct ", "B", b);
		assertEquals("Remove: check element 1 is correct ", "C",shortList.get(1));
		assertEquals("remove: check element 0 goes to 1 ", "C", shortList.head.next.next.data);
		
		
		emptyList.add(0, 1);
		emptyList.remove(0);
		
		assertEquals("empty list should only have 1 element", 0, emptyList.size());
		
		
		// check to see we can't remove out of bound indices
		try {
			shortList.remove(10);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		}
	}
	
	/** Test adding an element into the end of the list, specifically
	 *  public boolean add(E element)
	 * */
	@Test
	public void testAddEnd()
	{
        // TODO: implement this test
		// test to see if the size is correct
		// test to see if the end index is correct
		// test ot see if end index is linked correct to the one before
		// test to see if end index is linked to end
		shortList.add("C");
		emptyList.add(3);
		
		// make sure size is right
		assertEquals("Short list size", 3, shortList.size());
		assertEquals("Empty list size", 1, emptyList.size());
		
		// correctly linked to tail node
		assertEquals("Short list last value", "C", shortList.tail.prev.data);
		assertEquals("Empty list last value", 3, (int) emptyList.tail.prev.data);
		
		// correctly linked to previous
		assertEquals("Short list second to last value", "B", shortList.tail.prev.prev.data);
	}

	
	/** Test the size of the list */
	@Test
	public void testSize()
	{
		// TODO: implement this test
		int a = shortList.size();
		int b = emptyList.size();
		int c = longerList.size();
		assertEquals("Short list size ", 2, a);
		assertEquals("Longer list size ", 10, c);
		assertEquals("Empty list size ", 0, b);
	}

	
	
	/** Test adding an element into the list at a specified index,
	 * specifically:
	 * public void add(int index, E element)
	 * */
	@Test
	public void testAddAtIndex()
	{
        // TODO: implement this test
		shortList.add(2, "E");
		shortList.add(2, "D");
		shortList.add(2, "C");
		emptyList.add(10);
		
		// make sure size is right
		assertEquals("Short list size", 5, shortList.size());
		assertEquals("Empty list size", 1, emptyList.size());
		
		// test to see if we added at beginning and end it works
		assertEquals("Empty list element at 0", 10, (int) emptyList.head.next.data);
		assertEquals("Short list final element", "E", shortList.tail.prev.data);
		
		
		// test to see if we add at random index what right place
		assertEquals("Short list element at i=2", "C", shortList.get(2));
		assertEquals("Short list element at i=3", "D", shortList.get(3));
		
		// check to see we can't add out of bound indices
		try {
			shortList.add(10, "Z");
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		}
		
		// null pointer exception
		try {
			shortList.add(1, null);
			fail("Check null pointer");
		}
		catch (NullPointerException e) {
		}
		
	}
	
	/** Test setting an element in the list */
	@Test
	public void testSet()
	{	
		shortList.add(2, "C");
		
		// check to see we can't remove out of bound indices
		try {
			shortList.set(10, "Z");
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
				}
		// null pointer exception
		try {
			shortList.set(1, null);
			fail("Check null pointer");
		}
		catch (NullPointerException e) {
		}
		
		String a = shortList.set(1, "Z");
		assertEquals("Old letter at index 1 ", "B", a);
		assertEquals("New letter at index 1 ", "Z", shortList.get(1));
		
		String b = shortList.set(0, "X");
		assertEquals("Old letter at index 0 ", "A", b);
		assertEquals("New letter at index 0 ", "X", shortList.get(0));
		
	    
	}
	
	
	// TODO: Optionally add more test methods.
	
}
