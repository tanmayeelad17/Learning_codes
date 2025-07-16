country_dict={"US":"Washington",
              "Germany":"Berlin"}
print("Items in dictionary:",country_dict)
print("Length of initial dictionary=",len(country_dict))
country_dict["India"]="Delhi"
print("After adding item:",country_dict)
del country_dict["Germany"]
print("After deleting item:",country_dict)
print("Length of Final dict=",len(country_dict))