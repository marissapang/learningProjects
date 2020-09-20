/**
 * @author UCSD MOOC development team and YOU
 * 
 * A class which reprsents a graph of geographic locations
 * Nodes in the graph are intersections between 
 *
 */
package roadgraph;


import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.Consumer;

import geography.GeographicPoint;
import util.GraphLoader;

/**
 * @author UCSD MOOC development team and YOU
 * 
 * A class which represents a graph of geographic locations
 * Nodes in the graph are intersections between 
 *
 */
public class MapGraph {
	//TODO: Add your member variables here in WEEK 3
	private Set<GeographicPoint> vertices;
	private Map<GeographicPoint,ArrayList<GeographicPoint>> edges;
	private int numVertices;
	private int numEdges;
	
	
	/** 
	 * Create a new empty MapGraph 
	 */
	public MapGraph()
	{
		// TODO: Implement in this constructor in WEEK 3
		vertices = new HashSet<GeographicPoint>();
		edges = new HashMap<GeographicPoint,ArrayList<GeographicPoint>>();
		numVertices = 0;
		numEdges = 0;
	}
	
	/**
	 * Get the number of vertices (road intersections) in the graph
	 * @return The number of vertices in the graph.
	 */
	public int getNumVertices()
	{
		//TODO: Implement this method in WEEK 3
		return numVertices;
	}
	
	/**
	 * Return the intersections, which are the vertices in this graph.
	 * @return The vertices in this graph as GeographicPoints
	 */
	public Set<GeographicPoint> getVertices()
	{
		//TODO: Implement this method in WEEK 3
		return vertices;
	}
	
	/**
	 * Get the number of road segments in the graph
	 * @return The number of edges in the graph.
	 */
	public int getNumEdges()
	{
		//TODO: Implement this method in WEEK 3
		return numEdges;
	}

	
	
	/** Add a node corresponding to an intersection at a Geographic Point
	 * If the location is already in the graph or null, this method does 
	 * not change the graph.
	 * @param location  The location of the intersection
	 * @return true if a node was added, false if it was not (the node
	 * was already in the graph, or the parameter is null).
	 */
	public boolean addVertex(GeographicPoint location)
	{
		// TODO: Implement this method in WEEK 3
		if (vertices.contains(location) || location == null) {
			return false;
		} else {
			numVertices += 1;
			vertices.add(location);
			edges.put(location, new ArrayList<GeographicPoint>());
			return true;
		}
	}
	
	/**
	 * Adds a directed edge to the graph from pt1 to pt2.  
	 * Precondition: Both GeographicPoints have already been added to the graph
	 * @param from The starting point of the edge
	 * @param to The ending point of the edge
	 * @param roadName The name of the road
	 * @param roadType The type of the road
	 * @param length The length of the road, in km
	 * @throws IllegalArgumentException If the points have not already been
	 *   added as nodes to the graph, if any of the arguments is null,
	 *   or if the length is less than 0.
	 */
	public void addEdge(GeographicPoint from, GeographicPoint to, String roadName,
			String roadType, double length) throws IllegalArgumentException {

		//TODO: Implement this method in WEEK 3
		if (!(vertices.contains(from)) || !(vertices.contains(to)) || 
				from == null || to == null) {
			throw new IllegalArgumentException();
		} else {
			numEdges += 1;
			
			ArrayList<GeographicPoint> currValue = edges.get(from);
			currValue.add(to);
			edges.put(from, currValue);
		}
				
	}
	

	/** Find the path from start to goal using breadth first search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @return The list of intersections that form the shortest (unweighted)
	 *   path from start to goal (including both start and goal).
	 */
	public List<GeographicPoint> bfs(GeographicPoint start, GeographicPoint goal) {
		// Dummy variable for calling the search algorithms
        Consumer<GeographicPoint> temp = (x) -> {};
        return bfs(start, goal, temp);
	}
		
	/** Find the path from start to goal using breadth first search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @param nodeSearched A hook for visualization.  See assignment instructions for how to use it.
	 * @return The list of intersections that form the shortest (unweighted)
	 *   path from start to goal (including both start and goal).
	 */
	public List<GeographicPoint> bfs(GeographicPoint start, 
			 					     GeographicPoint goal, Consumer<GeographicPoint> nodeSearched)
	{
		// TODO: Implement this method in WEEK 3
		
		// create lists to store the geographic points 
		LinkedList<GeographicPoint> queue = new LinkedList<GeographicPoint>(); // use linked list because we want to remove from front
		List<GeographicPoint> visited = new ArrayList<GeographicPoint>();
		List<GeographicPoint> parents = new ArrayList<GeographicPoint>();
		
		
		queue.add(start);
		visited.add(start);
		parents.add(start);
		
		// We will keep looking for a path until we either 1) go through all the vertices or 2) come to all dead-ends (i.e. no more items in queue)
		while (visited.size() < numVertices && queue.size() > 0) {

			GeographicPoint currVertex = queue.removeFirst();
			List<GeographicPoint> neighbors = edges.get(currVertex);

			for (GeographicPoint n : neighbors) {
				nodeSearched.accept(n);
				if (n.equals(goal)) {
					// if we find our goal, we return the shortest path
					visited.add(n);
					parents.add(currVertex);
					return pathTraceBack(n, visited, parents);
					
				} else {
					// if we don't find our goal, then we add more items into queue and keep searching
					if (!(visited.contains(n))) {
						queue.addLast(n);
						visited.add(n);
						parents.add(currVertex);
					}	
				}
			}		
		}	
		return null;
	}
	
	/** Find the shortest path from the last Node, using visited and parents lists
	 * 
	 * @param endNode The ending node of the path - in this case, same as our goal
	 * @param visited List of locations we have visited
	 * @param parents List where each element is the previous element on our path of the corresponding visisted entry
	 * @return The shortest path
	 */
	private List<GeographicPoint> pathTraceBack(GeographicPoint endNode, List<GeographicPoint> visited, List<GeographicPoint> parents){
		LinkedList<GeographicPoint> shortestPath = new LinkedList<GeographicPoint>();
		
		if (visited.size() != parents.size()) {
			throw new IllegalArgumentException("visited and parent lists cannot be of different lenghts");
		}
		
		GeographicPoint curr;
		GeographicPoint currParent = endNode;
		
		for (int i = visited.size() - 1; i >= 0; i--) {
			curr = visited.get(i);
			if (curr == currParent) {
				shortestPath.addFirst(curr);
				currParent = parents.get(i);			
			}
		}
		return (List<GeographicPoint>) shortestPath;
	}

	/** Find the path from start to goal using Dijkstra's algorithm
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> dijkstra(GeographicPoint start, GeographicPoint goal) {
		// Dummy variable for calling the search algorithms
		// You do not need to change this method.
        Consumer<GeographicPoint> temp = (x) -> {};
        return dijkstra(start, goal, temp);
	}
	
	
	/** Find the path from start to goal using Dijkstra's algorithm
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @param nodeSearched A hook for visualization.  See assignment instructions for how to use it.
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> dijkstra(GeographicPoint start, 
										  GeographicPoint goal, Consumer<GeographicPoint> nodeSearched)
	{
		// TODO: Implement this method in WEEK 4

		int count = 0;
		// create lists to store the geographic points 
		LinkedList<GeographicPoint> queue = new LinkedList<GeographicPoint>(); // use linked list because we want to remove from front
		LinkedList<Double> queueDistance = new LinkedList<Double>();
		LinkedList<GeographicPoint> queueParents = new LinkedList<GeographicPoint>();
		List<GeographicPoint> visited = new ArrayList<GeographicPoint>();
		List<GeographicPoint> parents = new ArrayList<GeographicPoint>();
			
		queue.add(start);
		queueDistance.add(0.0);
		queueParents.add(start);
	
		// We will keep looking for a path until we either 1) go through all the vertices or 2) come to all dead-ends (i.e. no more items in queue)
		while (visited.size() < numVertices && queue.size() > 0) {
			
			GeographicPoint currVertex = queue.removeFirst();
			double currDistance = queueDistance.removeFirst();
			GeographicPoint currParent = queueParents.removeFirst();
			count += 1;
			List<GeographicPoint> neighbors = edges.get(currVertex);
			
			nodeSearched.accept(currVertex);
			
			if (currVertex.equals(goal)) {
				visited.add(currVertex);
				parents.add(currParent);
				System.out.println("Dijkstra count is:" + count);
				return pathTraceBack(currVertex, visited, parents);
			} else {
				if (!(visited.contains(currVertex))) {
					// Add new elements to queue, in ASCENDING order by distance
					for (GeographicPoint n : neighbors) {
						double newDistance = currDistance + currVertex.distance(n);
						
						// insert new distance into queueDistance
						queueDistance.add(newDistance); 
						Collections.sort(queueDistance);
						
						int newIndex = queueDistance.lastIndexOf(newDistance);
						queue.add(newIndex, n);
						queueParents.add(newIndex, currVertex);
					}
					
					visited.add(currVertex);
					parents.add(currParent);
					
					
				}
			}
		}
		
		System.out.println("Dijkstra count is:" + count);
			
		return null;
	}

	/** Find the path from start to goal using A-Star search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> aStarSearch(GeographicPoint start, GeographicPoint goal) {
		// Dummy variable for calling the search algorithms
        Consumer<GeographicPoint> temp = (x) -> {};
        return aStarSearch(start, goal, temp);
	}
	
	/** Find the path from start to goal using A-Star search
	 * 
	 * @param start The starting location
	 * @param goal The goal location
	 * @param nodeSearched A hook for visualization.  See assignment instructions for how to use it.
	 * @return The list of intersections that form the shortest path from 
	 *   start to goal (including both start and goal).
	 */
	public List<GeographicPoint> aStarSearch(GeographicPoint start, 
											 GeographicPoint goal, Consumer<GeographicPoint> nodeSearched)
	{	
		int count = 0;
		// TODO: Implement this method in WEEK 4
		// create lists to store the geographic points 
		LinkedList<GeographicPoint> queue = new LinkedList<GeographicPoint>(); // use linked list because we want to remove from front
		LinkedList<Double> queueDistance = new LinkedList<Double>();
		LinkedList<Double> queueTotalDistance = new LinkedList<Double>();
		LinkedList<GeographicPoint> queueParents = new LinkedList<GeographicPoint>();
		List<GeographicPoint> visited = new ArrayList<GeographicPoint>();
		List<GeographicPoint> parents = new ArrayList<GeographicPoint>();
			
		queue.add(start);
		queueDistance.add(0.0);
		queueTotalDistance.add(0.0);
		queueParents.add(start);
	
		// We will keep looking for a path until we either 1) go through all the vertices or 2) come to all dead-ends (i.e. no more items in queue)
		while (visited.size() < numVertices && queue.size() > 0) {
			
			GeographicPoint currVertex = queue.removeFirst();
			double currDistance = queueDistance.removeFirst();
			queueTotalDistance.removeFirst();
			count += 1;
			GeographicPoint currParent = queueParents.removeFirst();
			List<GeographicPoint> neighbors = edges.get(currVertex);
			
			nodeSearched.accept(currVertex);
			
			if (currVertex.equals(goal)) {
				visited.add(currVertex);
				parents.add(currParent);
				System.out.println("A* count is:" + count);

				return pathTraceBack(currVertex, visited, parents);
			} else {
				if (!(visited.contains(currVertex))) {
					// Add new elements to queue, in ASCENDING order by distance
					for (GeographicPoint n : neighbors) {
						double newDistance = currDistance + currVertex.distance(n);
						double estDistance = n.distance(goal);
						
						
						// insert new distance into queueDistance
						queueTotalDistance.add(newDistance + estDistance); 
						
						Collections.sort(queueTotalDistance);
						
						int newIndex = queueTotalDistance.indexOf(newDistance + estDistance);
						queue.add(newIndex, n);
						queueDistance.add(newIndex, newDistance);
						queueParents.add(newIndex, currVertex);
					}
					
					visited.add(currVertex);
					parents.add(currParent);
					

				}
			}
		}
		
		System.out.println("A* count is:" + count);
		return null;
		
		
	}

	
	
	public static void main(String[] args)
	{
		System.out.print("Making a new map...");
		MapGraph firstMap = new MapGraph();
		System.out.print("DONE. \nLoading the map...");
		GraphLoader.loadRoadMap("data/testdata/simpletest.map", firstMap);
		System.out.println("DONE.");
		
		// You can use this method for testing.  
		
		
		
		/* Here are some test cases you should try before you attempt 
		 * the Week 3 End of Week Quiz, EVEN IF you score 100% on the 
		 * programming assignment.
		 */
		
		MapGraph simpleTestMap = new MapGraph();
		GraphLoader.loadRoadMap("data/testdata/simpletest.map", simpleTestMap);
		
		GeographicPoint testStart = new GeographicPoint(1.0, 1.0);
		GeographicPoint testEnd = new GeographicPoint(8.0, -1.0);
		
		//THESE ARE MY OWN TESTERS
		// List<GeographicPoint> testroute = simpleTestMap.bfs(testStart, testEnd);
		// System.out.println(testroute);
		
		
		/* 
		System.out.println("Test 1 using simpletest: Dijkstra should be 9 and AStar should be 5");
		List<GeographicPoint> testroute = simpleTestMap.dijkstra(testStart,testEnd);
		List<GeographicPoint> testroute2 = simpleTestMap.aStarSearch(testStart,testEnd);
		
		
		MapGraph testMap = new MapGraph();
		GraphLoader.loadRoadMap("data/maps/utc.map", testMap);
		
		
		
		
		// A very simple test using real data
		testStart = new GeographicPoint(32.869423, -117.220917);
		testEnd = new GeographicPoint(32.869255, -117.216927);
		
		
		System.out.println("Test 2 using utc: Dijkstra should be 13 and AStar should be 5");
		testroute = testMap.dijkstra(testStart,testEnd);
		testroute2 = testMap.aStarSearch(testStart,testEnd);
		
		
		// A slightly more complex test using real data
		testStart = new GeographicPoint(32.8674388, -117.2190213);
		testEnd = new GeographicPoint(32.8697828, -117.2244506);
		System.out.println("Test 3 using utc: Dijkstra should be 37 and AStar should be 10");
		testroute = testMap.dijkstra(testStart,testEnd);
		testroute2 = testMap.aStarSearch(testStart,testEnd);
		
		*/ 
		
		/* Use this code in Week 3 End of Week Quiz */
		MapGraph theMap = new MapGraph();
		System.out.print("DONE. \nLoading the map...");
		GraphLoader.loadRoadMap("data/maps/utc.map", theMap);
		System.out.println("DONE.");

		GeographicPoint start = new GeographicPoint(32.8648772, -117.2254046);
		GeographicPoint end = new GeographicPoint(32.8660691, -117.217393);
		
		
		List<GeographicPoint> route = theMap.dijkstra(start,end);
		List<GeographicPoint> route2 = theMap.aStarSearch(start,end);

		
		
	}
	
}
