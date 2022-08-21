import geocoder
import time



cont="y"

while cont == "y":
    
    IPinput = input("Enter IP To Search: ")

    ip = geocoder.ip(IPinput)

    #Get City, Coutry and Coordinates   
    print("\nCity: " + ip.city)
    print("Country: "+ip.country)
    print(ip.latlng)
    print("\n")

    #Generate google maps link 
    print("https://www.google.com/maps/@"+str(ip.lat)+","+str(ip.lng) +",12z"   )

    cont = input("Do you want to continue? (y/n)")

