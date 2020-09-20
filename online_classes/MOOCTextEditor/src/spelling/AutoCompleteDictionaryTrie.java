package spelling;

import java.util.List;
import java.util.Set;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedList;

/** 
 * An trie data structure that implements the Dictionary and the AutoComplete ADT
 * @author You
 *
 */
public class AutoCompleteDictionaryTrie implements  Dictionary, AutoComplete {

    private TrieNode root;
    private int size;
    

    public AutoCompleteDictionaryTrie()
	{
		root = new TrieNode();
	}
	
	
	/** Insert a word into the trie.
	 * For the basic part of the assignment (part 2), you should convert the 
	 * string to all lower case before you insert it. 
	 * 
	 * This method adds a word by creating and linking the necessary trie nodes 
	 * into the trie, as described outlined in the videos for this week. It 
	 * should appropriately use existing nodes in the trie, only creating new 
	 * nodes when necessary. E.g. If the word "no" is already in the trie, 
	 * then adding the word "now" would add only one additional node 
	 * (for the 'w').
	 * 
	 * @return true if the word was successfully added or false if it already exists
	 * in the dictionary.
	 */
	public boolean addWord(String word)
	{	
		//TODO: Implement this method.
		
		if (word == "" || word == null) {
			return false;
		}
		String lowWord = word.toLowerCase();
		TrieNode currNode = root;
		if (isWord(lowWord)) {
			return false;
		} else {
			// iterate through each character in word
			for (int i = 0; i < lowWord.length() - 1; i++) {
				char c = lowWord.charAt(i);
				
				TrieNode child = currNode.getChild(c);
				if (child == null) { // if the child branch doesn't exist
					// add a child to the node
					currNode.insert(c);
					// set current node to the new child node
					currNode = currNode.getChild(c);
				} else { // if the child branch already exists
					// go to the next node
					currNode = child;
				}		
			}
			
			char lastC = lowWord.charAt(lowWord.length()-1);
			TrieNode lastChild = currNode.getChild(lastC);
			if (lastChild == null) {
				currNode.insert(lastC);
				currNode = currNode.getChild(lastC);
				currNode.setText(lowWord);
				currNode.setEndsWord(true);;
			} else {
				currNode = lastChild;
				currNode.setText(lowWord);
				currNode.setEndsWord(true);
			}
			return true;
		}
	    
	}
	
	/** 
	 * Return the number of words in the dictionary.  This is NOT necessarily the same
	 * as the number of TrieNodes in the trie.
	 */
	public int size()
	{
	    //TODO: Implement this method
		return countIfChildrenAreWords(root);
	}
	
	private int countIfChildrenAreWords(TrieNode node) {
		int count = 0;
		TrieNode childNode;
		
		if (node.getValidNextCharacters().isEmpty()) {
			return count;
		}
		
		for (char c : node.getValidNextCharacters()) {
			childNode = node.getChild(c);
			if (childNode.endsWord()) {
				count += 1;
			}
			count += countIfChildrenAreWords(childNode);
		}
		return count;
	}
	
	
	/** Returns whether the string is a word in the trie, using the algorithm
	 * described in the videos for this week. */
	@Override
	public boolean isWord(String s) 
	{
		if (s == "" || s == null) {
			return false;
		}
	    // TODO: Implement this method
		
		String lowS = s.toLowerCase();
		TrieNode currNode = root;
		
		// iterate through each character in word
		for (int i = 0; i < lowS.length()-1; i++) {
			char c = lowS.charAt(i);
			
			TrieNode child = currNode.getChild(c);
			if (child == null) { // if the child branch doesn't exist
				// then we return NOT a word
				return false;
				// set current node to the new child node	
			} else {
				currNode = currNode.getChild(c);
			}
		}
		
		char lastC = lowS.charAt(lowS.length()-1);
		TrieNode lastChild = currNode.getChild(lastC);
		if (lastChild == null) {
			return false;
		} else if (lastChild.endsWord() == false) {
			return false;
		} else {
			return true;
		}			
	}
	
	

	/** 
     * Return a list, in order of increasing (non-decreasing) word length,
     * containing the numCompletions shortest legal completions 
     * of the prefix string. All legal completions must be valid words in the 
     * dictionary. If the prefix itself is a valid word, it is included 
     * in the list of returned words. 
     * 
     * The list of completions must contain 
     * all of the shortest completions, but when there are ties, it may break 
     * them in any order. For example, if there the prefix string is "ste" and 
     * only the words "step", "stem", "stew", "steer" and "steep" are in the 
     * dictionary, when the user asks for 4 completions, the list must include 
     * "step", "stem" and "stew", but may include either the word 
     * "steer" or "steep".
     * 
     * If this string prefix is not in the trie, it returns an empty list.
     * 
     * @param prefix The text to use at the word stem
     * @param numCompletions The maximum number of predictions desired.
     * @return A list containing the up to numCompletions best predictions
     */@Override
     public List<String> predictCompletions(String prefix, int numCompletions) 
     {
    	 // TODO: Implement this method
    	 // This method should implement the following algorithm:
    	 // 1. Find the stem in the trie.  If the stem does not appear in the trie, return an
    	 //    empty list
    	 // 2. Once the stem is found, perform a breadth first search to generate completions
    	 //    using the following algorithm:
    	 //    Create a queue (LinkedList) and add the node that completes the stem to the back
    	 //       of the list.
    	 //    Create a list of completions to return (initially empty)
    	 //    While the queue is not empty and you don't have enough completions:
    	 //       remove the first Node from the queue
    	 //       If it is a word, add it to the completions list
    	 //       Add all of its child nodes to the back of the queue
    	 // Return the list of completions
    	 TrieNode currNode = root;
    	 for (int i=0; i < prefix.length(); i++) {
    		 char c = prefix.charAt(i);
    		 if (currNode.getChild(c) != null) { // if the trie exist, we keep going
    			 currNode = currNode.getChild(c);
    		 } else { // if path doesn't exist, we return empty list
    			 List<String> emptyList = new ArrayList<String>();
    			 return emptyList;
    		 } 
    	 }
    	 
    	 // if we get to the end of the prefix, then we stop searching
    	 int count = 0;
    	 LinkedList<TrieNode> trackingList = new LinkedList<TrieNode>();
    	 List<String> completionsList = new ArrayList<String>();
    	 trackingList.add(currNode);
    	    	 
    	 while (count < numCompletions && trackingList.size() > 0) { // only need to search until we get enough
    		 // get all children from current node, and look through them one at a time
    		 currNode = trackingList.get(0);
    		 if (trackingList.size() == 0) {
    			 return completionsList;
    		 }
    		 
    		 // check if currNode is a word
    		 if (currNode.endsWord()) {
    			 count += 1;
    			 completionsList.add(currNode.getText());
    		 }
    		 
    		 for (char c : currNode.getValidNextCharacters()) {
    			 trackingList.addLast(currNode.getChild(c));
    		 }
    		 
    		 trackingList.removeFirst();
    	 }
    	 
         return completionsList;
     }
     


 	// For debugging
 	public void printTree()
 	{
 		printNode(root);
 	}
 	
 	/** Do a pre-order traversal from this node down */
 	public void printNode(TrieNode curr)
 	{
 		if (curr == null) 
 			return;
 		
 		System.out.println(curr.getText());
 		
 		TrieNode next = null;
 		for (Character c : curr.getValidNextCharacters()) {
 			next = curr.getChild(c);
 			printNode(next);
 		}
 	}
 	

	
}