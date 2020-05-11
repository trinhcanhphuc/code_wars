public class Finder {
  private final static int INF = Integer.MAX_VALUE;
  private static int[][] graph;

  public static int pathFinder(String maze) {
    initGraph(maze);
    goTo(0, 0, 0);
    return (graph[graph.length - 1][graph.length - 1] == INF) ? -1 : graph[graph.length - 1][graph.length - 1];
  }

  private static void initGraph(String maze){
    String[] lines = maze.split("\n");
    graph = new int[lines.length][lines.length];
    for(int i=0; i<lines.length; i++)
      for(int j=0; j<lines.length; j++)
        graph[i][j] = (lines[i].charAt(j)=='W')?-1:INF;
  }

  private static void goTo(int i, int j, int step){
    if(i==-1 || i==graph.length || j==-1 || j==graph.length || graph[i][j] <= step)
      return;
    graph[i][j] = step;
    goTo(i, j-1, step+1);
    goTo(i, j+1, step+1);
    goTo(i+1, j, step+1);
    goTo(i-1, j, step+1);
  }

  public static void main(String[] args){
    String c = "......\n"+
    "......\n"+
    "......\n"+
    "......\n"+
    "......\n"+
    "......";
    System.out.println(pathFinder(c));
  }
}