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
```
function dfs(v):
  time = time + 1
  enter[v] = time
  ret[v] = time 
  for всех u смежных с v
    if (v, u) — обратное ребро
      ret[v] = min(ret[v], enter[u])
    if вершина u — белая
      dfs(u)
      ret[v] = min(ret[v], ret[u]) 
      if ret[u] > enter[v] 
        ребро (v, u) — мост
```
# Поиск циклов для ориентированного графа
```
func dfs(v: vertex):             
  color[v] = grey             
  for (u: vu ∈ E)
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
