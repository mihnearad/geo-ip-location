import geocoder
import time



cont= 1

while cont == 1:
    
    IPinput = input("Enter IP To Search: ")

    ip = geocoder.ip(IPinput)

    #Get City, Country and Coordinates   
    print("\nCity: " + ip.city)
    print("Country: "+ip.country)
    print(ip.latlng)
    print("\n")

    #Generate google maps link 
    print("https://www.google.com/maps/@"+str(ip.lat)+","+str(ip.lng) +",12z"   )

    user_input = input("\nDo you want to continue? (y/n) -->")

    #exit if answer is no
    if user_input == "n":
        cont=cont+1
        
    
        
