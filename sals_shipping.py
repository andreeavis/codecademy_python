sals_shipping.py
def cost_ground(weight):
  if weight <= 2:
    return 20 + (1.50 * weight)
  elif weight <= 6:
    return 20 + (3 * weight)
  elif weight <= 10:
    return 20 + (4 * weight)
  else:
    return 20 + (4.75 * weight)

print(cost_ground(8.4))

cost_premium = 125

def cost_drone(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight <= 6:
    return weight * 9.00
  elif weight <= 10:
    return weight * 12.00
  else:
    return weight * 14.25
  
print(cost_drone(1.5))

def cost_ship(weight):
  if (cost_ground(weight) < cost_premium) and (cost_ground(weight) < cost_drone(weight)):
    print("Your package will ship using ground shipping, it will cost $ " + str(cost_ground(weight)))
  elif (cost_drone(weight) < cost_premium) and (cost_drone(weight) < cost_ground(weight)):
    print("Your package will ship using ground shipping it will cost $ " + str(cost_drone(weight)))
  else:
    print("Your package will ship using ground shipping it will cost $ " + str(cost_premium))
    
print(cost_ship(4.8))
print(cost_ship(41.5))
  
  
  
  
  
  
  
  
  
  