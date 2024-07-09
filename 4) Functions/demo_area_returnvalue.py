def area(pi,radius):
   result = pi*radius*radius
   return result

def cost(circle_area,cost_per_sqm):
    total_cost = circle_area*cost_per_sqm
    return total_cost

calculated_area = area(10,3.14)
tc = cost(calculated_area,2)
print(tc)
