# DFS
``` 
function doDfs(G[n]: Graph): 
   color = array[n, white]
   function dfs(u: int):
      color[u] = gray           
      for v: (u, v) in G                   
         if color[v] == white
            dfs(v)
      color[u] = black         	   
   for i = 1 to n             
      if color[i] == white                
         dfs(i)
```
# TopSort
```
function topSort():
  // Перед запуском проверить, что граф ацикличский
  fill(visited,false)
  for v∈V(G)
      if not visited[v]
           dfs(v)
  ans.reversed()
function dfs(u):
  visited[u]=true
  for uv∈E(G)
      if not visited[v]
          dfs(v)
  ans.append(u)
```
# Поиск мостов

Пусть fup[u] - наим глубина такоей вершины, которая доступна из вершины u по пути древесных ребер с не более чем одним обратным ребром в конце\
Кандидатами в мосты могут быть только древесные ребра\
fup[u] > d[v] <=> между ними мост 
```
globals: g, fup, d, bridges
===
Read graph
d[] := [-1, -1,..., -1]
fup[] := [-1, -1,..., -1]
edges := []
for u in V:
   if d[u] == -1:
      dfs(u, u, 0)
===
dfs(u, parent, depth):
   d[u] = fup[u] = depth
   for v in g[u]:
      if (v != parent):
         if d[v] == -1: // (u, v) - tree edge
            dfs(v, u, depth+1)
            fup[u] = min(fup[u], fup[v])
            if d[u] < fup[v]:
               bridges.push({u, v})
         else: // (u, v) - backward edge
            fup[u] = min(fup[u], d[v])
```
# Поиск циклов для ориентированного графа
```
func dfs(v: vertex):             
  color[v] = grey             
  for (u : g[v])
      if (color[u] == white)
          dfs(u)
      if (color[u] == grey)
          print("Cycle!")
  color[v] = black
```
# Алгоритм точек сочленения
Если ребро мост из этого не следуется, что вершины - точки сочленения\
Если r - корень дерева DFS, то r - точка сочленения <=> кол-во её детей в дереве DFS >= 2\
Если же r - не корень, то она точка сочленения <=> существует такой сын v в дереве DFS: fup[v] >= d[u]\
```
dfs(u, parent, depth):
   fup[u] = d[u] = depth
   cut = false
   childCount = 0
   for v in g[u]:
      if v != parent:
         if d[v] == -1:
            childCount++
            dfs(v, u, depth+1)
            fup[u] = min(fup[u], fup[v])
            if u != parent && fup[v] >= d[u]:
               cut = true
         else:
            fup[u] = min(fup[u], d[v])
   if cut || (u == parent && childCount > 1):
      cuts.append(u)
```
# Проверка компонентов сильной связанности
Алгоритм Касарагио:
1) Делаем "псевдо-topsort"
2) Транспонируем граф
3) Запускаем серию DFS в выписанном в п.1 порядке на транспонированом графе
4) Каждое дерево DFS из п.3 - КСС и она получена в порядке topsort конденсации
```
function dfs1(v):                                          
   visited[v] = true
   for u : g[v]:
       if not visited[u]
           dfs1(u)
   ord.append(v)

function dfs2(v):                                          
   component[v] = col
   for u : transposed[v]
       if (u not in component)                       
           dfs2(u)

function main():
   считываем исходные данные, формируем массивы g и transposed
   for u in g[v]                           
       if not visited[u]
           dfs1(u)
   col = 1
   for (u : reversed(ord)):                                                        
       if (u not in component):
           dfs2(u)
           col++
```
# Поиск наикратчайшего пути от точки до точки на поле
``` java
import java.util.*;

public class Main {
    private static final int[] DR = {-1, 0, 1, 0};
    private static final int[] DC = {0, 1, 0, -1};
    private static final String[] DIR = {"N", "E", "S", "W"};
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        char[][] f = new char[n][];
        State start = null;
        State finish = null;
        for (int i = 0; i < n; i++) {
            f[i] = scanner.next().toCharArray();
            for (int j = 0; j < m; j++) {
                if (f[i][j] == 'S') {
                    start = new State(i, j);
                } else if (f[i][j] == 'F') {
                    finish = new State(i, j);
                }
            }
        }

        int[][] d = new int[n][m];
        int[][] p = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(d[i], Integer.MAX_VALUE);
            Arrays.fill(p[i], -1);
        }
        assert start != null;
        assert finish != null;
        p[start.row][start.col] = Integer.MAX_VALUE;
        d[start.row][start.col] = 0;

        Queue<State> q = new ArrayDeque<>();
        q.add(start);
        while (!q.isEmpty() && d[finish.row][finish.col] == Integer.MAX_VALUE) {
            State cur = q.poll();
            for (int i = 0; i < 4; i++) {
                int row = cur.row + DR[i];
                int col = cur.col + DC[i];
                if (row >= 0 && row < n && col >= 0 && col < m && f[row][col] != '#'
                        && d[row][col] == Integer.MAX_VALUE) {
                    d[row][col] = d[cur.row][cur.col] + 1;
                    p[row][col] = i;
                    q.add(new State(row, col));
                }
            }
        }
        if (d[finish.row][finish.col] == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(d[finish.row][finish.col]);
            ArrayList<String> ans = new ArrayList<>();
            State cur = finish;
            while (p[cur.row][cur.col] != Integer.MAX_VALUE) {
                int i = p[cur.row][cur.col];
                cur.row -= DR[i];
                cur.col -= DC[i];
                ans.add(DIR[i]);
            }
            for (String s : ans.reversed()) {
                System.out.println(s);
            }
        }
    }

    private static final class State {
        private int row;
        private int col;

        public State(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}
```
# релаксация графа
```
relax(u, v):
   if d[v] > d[u] + w(u, v):
      d[v] = d[u] + w(u, v);
```
# Алгоритм Форда-Бельмана
Данный алгоритм работает для взв графов с отриц дугами, но без ц.о.в, достижимых из S
```
d = [inf, inf,...];
d[s] = 0;
p = [-1, -1,...];
p[s] = s
for n-1 раз:
   for (u, v) in E:
      if (d[u] != inf && d[v] > d[u] + w(u, v)):
         d[v] = d[u] + w(u, v)
         p[v] = u
```
# Алгоритм SPFA
```
d = [inf, inf,...];
d[s] = 0;
p = [-1, -1,...];
p[s] = s
q.push(s)
while !q.empty():
   u = q.poll()
   for (u, v) in E:
      if (d[v] > d[u] + w(u, v)):
         d[v] = d[u] + w(u, v)
         p[v] = u
         q.push(v)
```
# Алгоритм Дейкстры
Алгоритм работает для графов с весвми >= 0
```
d = [inf, inf, ...]
d[s] = 0
visied = [false, false, ...]
while true:
   найдем u = вершина вне облака с мин знач d
   if не сущ u || d[u] = inf:
      break
   visited[u] = true
   for (u, v) in E:
      if d[v] > d[u] + w(u, v):
         d[v] = d[u] + w(u, v)
```
# Алгоритм Флойда
Инвариант: после t-ой итерации массив d такой, что D[u][v] <= d[u][v] <= d[t][u][v]
```
d[n][n]
for i in V, for j in V: d[i][j] = inf
for i in V: d[i][i] = 0

for (u, v) in E:
   d[u][v] = min(d[u][v], w(u, v))
for t in V:
   for u in V:
      for v in V:
         if (d[u][t] < inf && d[t][v] < inf && d[u][v] > -inf):
            d[u][v] = min(d[u][v], d[u][t]+d[t][v])
```
Если после прохождения алгоритма d[u][u] < 0, то есть ц.о.в, проходящий через u
