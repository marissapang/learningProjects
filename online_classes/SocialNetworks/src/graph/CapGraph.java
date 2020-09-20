/**
 * 
 */
package graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

// import geography.GeographicPoint;

/**
 * @author Your name here.
 * 
 * For the warm up assignment, you must implement your Graph in a class
 * named CapGraph.  Here is the stub file.
 *
 */
public class CapGraph implements Graph {

	/* (non-Javadoc)
	 * @see graph.Graph#addVertex(int)
	 */
	
	private HashSet<Integer> vertices;
	private Map<Integer,HashSet<Integer>> edges;
	private int numVertices;
	private int numEdges;
	
	// attributes for search tracking
	private HashSet<Integer> visited;
	private List<Integer> finished;
	private HashSet<Integer> currComp; 
	
	
	public CapGraph() {
		vertices = new HashSet<Integer>();
		edges = new HashMap<Integer,HashSet<Integer>>();
		numVertices = 0;
		numEdges = 0;
	}
	
	public int getNumVertices(){
		return numVertices;
	}
	
	
	public HashSet<Integer> getVertices(){
		return vertices;
	}
	
	
	public void setVerticesAndResetEdges(HashSet<Integer> newSet){
		vertices = newSet;
		edges = new HashMap<Integer,HashSet<Integer>>();
		for (int v : newSet) {
			edges.put(v, new HashSet<Integer>());
		}
	}
	
	@Override
	public void addVertex(int num) {
		if (vertices.contains(num)) {
			// do nothing
		} else {
			numVertices += 1;
			vertices.add(num);
			edges.put(num, new HashSet<Integer>());
		}

	}
	
	public int getNumEdges(){
		return numEdges;
	}
	
	public Map<Integer,HashSet<Integer>> getEdges(){	
		return edges;
	}
	public HashSet<Integer> getNeighbors(int node){	
		return edges.get(node);
	}
	
	public List<Integer> getNonVisitedNeighbors(int node, HashSet<Integer> visited){
		List<Integer> nonVisited = new ArrayList<Integer>();
		
		HashSet<Integer> neighbors = getNeighbors(node);
		for (int n: neighbors) {
			if (!visited.contains(n)) {
				nonVisited.add(n);
			}
		}
		
		return nonVisited;
	}

	/* (non-Javadoc)
	 * @see graph.Graph#addEdge(int, int)
	 */
	@Override
	public void addEdge(int from, int to) {
		if (!(vertices.contains(from)) || !(vertices.contains(to)) ) {
			// throw new IllegalArgumentException("Vertices does not exist or is null");
			return;
		} else {
			numEdges += 1;
			
			HashSet<Integer> currValue = edges.get(from);
			currValue.add(to);
			edges.put(from, currValue);
		}
	}

	
	public CapGraph transposeGraph() {
		CapGraph gT = new CapGraph();
		gT.setVerticesAndResetEdges(vertices);
		
		Map<Integer, HashSet<Integer>> graphEdges = getEdges();
		
		for (int node : graphEdges.keySet()) {
			HashSet<Integer> neighbors = graphEdges.get(node);
			
			for (int n : neighbors) {
				gT.addEdge(n, node);
			}
		}
		return gT;
	}
	
	private Graph getSubGraph(HashSet<Integer> selectedVertices) {
		CapGraph subGraph = new CapGraph();
		subGraph.setVerticesAndResetEdges(selectedVertices);
		
		for (int n : selectedVertices) {
			
			HashSet<Integer> nEdges = getNeighbors(n);
			
			for (int edge : nEdges) {
				if (selectedVertices.contains(edge)) {
					subGraph.addEdge(n,  edge);
				}
			}
		}	
		return subGraph;
	}
	
	/* (non-Javadoc)
	 * @see graph.Graph#getEgonet(int)
	 */
	@Override
	public Graph getEgonet(int center) {
		// return error if the center does not exist
		Graph egonet = new CapGraph();
		if (!getVertices().contains(center)) {
			// throw new IllegalArgumentException("Vertex does not exist or is null");
			return egonet;
		}
		
		// for center, get all neighbors 
		egonet.addVertex(center);
		
		HashSet<Integer> neighbors = getNeighbors(center);
		
		// add all neighbors and the edges between them and center
		for (int n : neighbors) {
			egonet.addVertex(n);
			egonet.addEdge(center, n);
		}
		
		// add all the edges between the neighbors
		for (int n : neighbors) {
			
			HashSet<Integer> nEdges = getNeighbors(n);
			for (int edge : nEdges) {
				if (neighbors.contains(edge)) {
					egonet.addEdge(n,  edge);
				}
			}
		}	
		return egonet;
	}

	/* (non-Javadoc)
	 * @see graph.Graph#getSCCs()
	 */
	@Override
	public List<Graph> getSCCs() {
		
		// attributes for tracking
		List<Graph> SCCs = new ArrayList<Graph>(); // returns list of all SCCs
		
		List<Integer> verticesList = new ArrayList<>(getVertices()); // list of nodes to visit
		
		visited = new HashSet<Integer>(); // track nodes we have visited
		finished = new ArrayList<Integer>(); // tracks "finished" in order
		
		
		// 1. Loop through vertices recursively
		for (int i = 0; i < verticesList.size(); i++) {
			if (!visited.contains(verticesList.get(i) )) {
				depthSearchHelper(verticesList.get(i));
			}
		}
		
		// 2. Set up transposed graph and clear visited
		visited = new HashSet<Integer>();
		CapGraph gT = transposeGraph();
		
		// 3. Pop elements from finished to get to final lists
		
		while (finished.size() > 0) {
			int node = finished.remove(finished.size()-1);
			
			if (visited.contains(node)) {
				continue;
			}
			
			currComp = new HashSet<Integer>();
			SCCHelper(node, gT);
			SCCs.add(getSubGraph(currComp));
		}
		
		return SCCs;
	}
	
	private void SCCHelper(int node, CapGraph gT) {
		if (visited.contains(node)) {
			return;
		}
		
		visited.add(node);
		currComp.add(node);
		
		List<Integer> validNeighbors = gT.getNonVisitedNeighbors(node, visited);
		
		if (validNeighbors.size() != 0) {
			for (int n : validNeighbors) {
				SCCHelper(n, gT);
			}
		} else {
			currComp.add(node);
		}
	}
	
	private void depthSearchHelper(int node) {
		
		if (visited.contains(node)) {
			return;
		}
		
		visited.add(node);
		
		List<Integer> validNeighbors = getNonVisitedNeighbors(node, visited);
		
		if (validNeighbors.size() != 0) {
			for (int n : validNeighbors) {
				depthSearchHelper(n);
				finished.add(node);
			}
		} else {
			finished.add(node);
		}
	}
	

	/* (non-Javadoc)
	 * @see graph.Graph#exportGraph()
	 */
	@Override
	public HashMap<Integer, HashSet<Integer>> exportGraph() {
		
		HashMap<Integer, HashSet<Integer>> exportedGraph = new HashMap<Integer, HashSet<Integer>>();
		
		for (int key : getVertices()) {
			exportedGraph.put(key, getNeighbors(key));
		}
		return exportedGraph;
	}

}
