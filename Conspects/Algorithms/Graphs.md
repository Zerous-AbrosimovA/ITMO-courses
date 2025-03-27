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
# Проверка компонентов сильной связанности
```
function dfs1(v):                                          
   color[v] = 1
   for (v, u) in E
       if not visited[u]
           dfs1(G[v][u])
   Добавляем вершину v в конец списка ord

function dfs2(v):                                          
   component[v] = col
   for (v, u) in E
       if (вершина u еще не находится ни в какой компоненте)                       
           dfs2(H[v][u])

function main():
   считываем исходные данные, формируем массивы G и H
   for u in V                           
       if not visited[u]
           dfs1(u)
   col = 1
   for (по всем вершинам u списка ord[] в обратном порядке)                                                        
       if (вершина u не находится ни в какой компоненте)
           dfs2(u)
           col++
```
