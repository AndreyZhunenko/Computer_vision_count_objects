import numpy as np
import matplotlib.pyplot as plt

def create_image():
    my_image = np.zeros((20, 20))

    my_image[1:-1, -2] = 1
    
    my_image[1, 1:5] = 1
    my_image[1, 7:12] = 1
    my_image[2, 1:3] = 1
    my_image[2, 6:8] = 1
    my_image[3:4, 1:7] = 1
    
    my_image[7:11, 11] = 1
    my_image[7:11, 14] = 1
    my_image[10:15, 10:15] = 1
    
    my_image[5:10, 5] = 1
    my_image[5:10, 6] = 1
    return my_image

def negate(B):
    return B.copy() * -1

def neighbours8(y, x):
    return (
            (y-1, x-1),
            (y-1, x),
            (y-1, x+1),
            (y, x+1),
            (y, x-1),
            (y+1, x+1),
            (y+1, x),
            (y+1, x-1)
    )

def search(LB, label, y, x):
    LB[y, x] = label
    neighbours = neighbours8(y, x)
    for ny, nx in neighbours:
        if LB[ny, nx] == -1:
            search(LB, label, ny, nx)
            

def recursive_labeling(B):
    LB = negate(B)
    label = 0
    for y in  range(LB.shape[0]):
        for x in range(LB.shape[1]):
            px = LB[y, x]
            if px == -1:
                label += 1
                search(LB, label, y, x)
                
    return LB

def count_objects(my_labeled_picture):
    count = my_labeled_picture.max();
    return count
    
    
    

image = np.load("ps.npy.txt")

labeled_image = recursive_labeling(image)

final_count = count_objects(labeled_image)
print("count objects = ", final_count)

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled_image)
plt.show()
