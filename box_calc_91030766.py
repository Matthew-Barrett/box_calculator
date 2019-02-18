x = int(input("total_number_of_parcels:"))
large_boxes = x//5
medium_boxes = x%5//3
small_boxes = x%5%3//1

print (large_boxes, "large boxes")
print (medium_boxes, "medium boxes")
print (small_boxes, "small boxes")
