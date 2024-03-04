
cost_per_night=150
daily_rental_cost=50
city_flight=input("Enter the city  destination")
num_nights=int(input("Enter the number of nights staying at the hotel"))
rental_days=int(input("Enter the number of days renting a car"))
hotel_cost(num_nights):
     total_hotel_cost= num_nights * cost_per_night
     return total_hotel_cost
plane_cost(city_flight):
     if city_flight == 'London'
          city_flight_cost=300
     elif city_flight=='New York'
          city_flight_cost=500
     elif city_flight=='paris'
          city_flight_cost=800
     else:
          print("Enter the valid city which is given on chart")  
      
car_rental(rental_days) :  
                 
       total_car_rental_cost=rental_days*daily_rental_cost
       return total_car_rental_cost

#holiday_cost(hotel_cost,plane_cost,car_rental):
       holiday_total_cost=total_hotel_cost+city_flight_cost+total_car_rental_cost
       return holiday_total_cost
print("the hotel cost is",hotel_cost(num_nights))
print("car rent cost is",car_rental(rental_days))
print("plane cost is",plane_cost(city_flight))
#print("total holiday cost is",holiday_cost(t))