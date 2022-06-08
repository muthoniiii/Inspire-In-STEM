

class Vehicles:
    def __init__ (vehicle,_maxspeed,_milage):
        vehicle.speed=(_maxspeed)
        vehicle.miles=(_milage)
    
    def v_details(vehicle):
        print("The vehicle milage is"+" " +str (vehicle.speed)+" " + "and vehicle maximum speed is"+" " + str(vehicle.miles))

pagani=Vehicles(150,670)
pagani.v_details()
mclaren=Vehicles(240,450)
mclaren.v_details()
renault=Vehicles(300,645)
renault.v_details()
lotus=Vehicles(300,760)
lotus.v_details()

print(pagani.speed, pagani.miles)
