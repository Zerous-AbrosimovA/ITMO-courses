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
Алгоритм Касарагио:\
1) Делаем "псевдо-topsort"
2) Транспонируем граф
3) Запускаем серию DFS в выписанном в п.1 порядке на транспонированом графе
4) Каждое дерево DFS из п.3 - КСС и она получена в порядке topsort конденсации
```
function dfs1(v):                                          
   color[v] = 1
   for u : g[v]:
       if not visited[u]
           dfs1(u)
   Добавляем вершину v в конец списка ord

function dfs2(v):                                          
   component[v] = col
   for u : gr[v]
       if (вершина u еще не находится ни в какой компоненте)                       
           dfs2(u)

function main():
   считываем исходные данные, формируем массивы g и H
   for u in g[v]                           
       if not visited[u]
           dfs1(u)
   col = 1
   for (u : reversed(ord)):                                                        
       if (u not in component):
           dfs2(u)
           col++
```
