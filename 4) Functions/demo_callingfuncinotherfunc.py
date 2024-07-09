def area(pi,radius):
   result = pi*radius*radius
   return result

def cost(circle_area,cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost

print(cost(area(10,3.14),2))
