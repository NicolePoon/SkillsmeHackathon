import sys
import time
start_time = time.time()

def get_weight_uv(grid_list, u, v, n, m):
    
    if v == u-(m+1)-1:
        try:
            weight = int(grid_list[(u // (m+1))-1][(u % (m+1))-1])
        except:
            return float("inf")
        if (u // (m+1))-1 == -1 or (u % (m+1))-1 == -1 :
            return float("inf")
        return weight 
            
    elif v == u-(m+1)+1:
        try:
            weight = int(grid_list[(u // (m+1))-1][((u+1) % (m+1))-1])
        except:
            return float("inf")
        if (u // (m+1))-1 == -1 or ((u+1) % (m+1))-1 == -1:
            return float("inf")
        return weight
            
    elif v == u+(m+1)-1:
        try:
            weight = int(grid_list[u // (m+1)][(u % (m+1))-1])
        except:
            return float("inf")
        if (u % (m+1))-1 == -1:
            return float("inf")
        return weight
            
    elif v == u+(m+1)+1:
        try:
            weight = int(grid_list[u // (m+1)][((u+1) % (m+1))-1])
        except:
            return float("inf")
        if ((u+1) % (m+1))-1 == -1:
            return float("inf")
        return weight
        
            
    elif v == u+1:
        try:
            weight1 = int(grid_list[(u // (m+1))-1][((u+1) % (m+1))-1])
        except:
            weight1 = float("inf")
        if (u // (m+1))-1 == -1 or ((u+1) % (m+1))-1 == -1:
            weight1 = float("inf")
        try:    
            weight2 = int(grid_list[(u // (m+1))][((u+1) % (m+1))-1])
        except:
            weight2 = float("inf")
        if ((u+1) % (m+1))-1 == -1:
            weight2 = float("inf")
            
        return min(weight1, weight2)    
            
    elif v == u-1:
        try:
            weight1 = int(grid_list[(u // (m+1))-1][(u % (m+1))-1])
        except:
            weight1 = float("inf")
        if (u // (m+1))-1 == -1 or (u % (m+1))-1 == -1:
            weight1 = float("inf")
        try:
            weight2 = int(grid_list[(u // (m+1))][(u % (m+1))-1])
        except:
            weight2 = float("inf")
        if (u % (m+1))-1 == -1:
            weight2 = float("inf")
            
        return min(weight1, weight2)
                
            
    elif v == u-(m+1):
        try:
            weight1 = int(grid_list[(u // (m+1))-1][(u % (m+1))-1])
        except:
            weight1 = float("inf")
        if (u // (m+1))-1 == -1 or (u % (m+1))-1 == -1:
            weight1 = float("inf")
        try:
            weight2 = int(grid_list[(u // (m+1))-1][((u+1) % (m+1))-1])
        except:
            weight2 = float("inf")
        if (u // (m+1))-1 == -1 or ((u+1) % (m+1))-1 == -1:
            weight2 = float("inf")
            
        return min(weight1, weight2)
            
    elif v == u+(m+1):
        try:
            weight1 = int(grid_list[(u // (m+1))][(u % (m+1))-1])
        except:
            weight1 = float("inf")
        if (u % (m+1))-1 == -1:
            weight1 = float("inf")
            
        try:
            weight2 = int(grid_list[(u // (m+1))][((u+1) % (m+1))-1])
        except:
            weight2 = float("inf")
        if ((u+1) % (m+1))-1 == -1:
            weight2 = float("inf")
                
        return min(weight1, weight2)
    else:
        return float("inf")


def get_min_dist(a_list, color_list, node):
    previous_mini = float("inf")
    current_mini = float("inf")
    mini_index = node
    for i in range(len(a_list)):
        if i != node and color_list[i] != "black":
            current_mini = min(previous_mini, a_list[i])
            if current_mini !=previous_mini:
                mini_index = i
                previous_mini = current_mini
    return mini_index


def dijkstra(grid_list, node, num_vertices, n, m):
    color = []
    dist = []
    color_black = 0
    for i in range(num_vertices):
        color.append("white")
        #print(i)
        path_length = get_weight_uv(grid_list, node, i, n, m) 
        dist.append(path_length)
    dist[node] = 0
    color[node] = "black"
    color_black += 1
    #print(color)
    #print(dist)
    
    while color_black < len(color):
        u = get_min_dist(dist, color, node) # no change
        color[u] = "black"
        color_black += 1
        for i in range(len(color)):
            if color[i] == "white":
                dist[i] = min(dist[i], dist[u] + get_weight_uv(grid_list, u, i, n, m)) # THIS FUNCTION!!! need to change, only have grid_list
    return dist


def prepare_data(a_list, n, m):
    start_node = n*(m+1)
    end_node = m
    total_vertices = (m+1)*(n+1)
    dist_list = dijkstra(a_list, start_node, total_vertices, n, m)
    return dist_list
    

def main():
    is_n_m = True
    for line in sys.stdin:
        line = line.strip()
        if is_n_m == False:
            count += 1
            row_list = line.split()
            grid_list.append(row_list)
            
        if is_n_m == True:
            num_list = line.split()
            rows = int(num_list[0])
            cols = int(num_list[1])
            if rows == 0 and cols == 0:
                break
            is_n_m = False
            count = 0
            grid_list = []
        
        if count == rows:
            is_n_m = True
            distance_list = prepare_data(grid_list, rows, cols)
            #print(grid_list)
            #print(distance_list)
            print(distance_list[cols])
        
            
    
main()
print("--- %s seconds ---" % (time.time() - start_time))
         


