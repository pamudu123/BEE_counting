'''
get_image_paths(dataset_dir): image paths for bee images found with its label.

create_bee_array(n_bees, bee_images_dir) : Creates an array of randomly resized bee images from the given directory.
                                            bee images are randomly resized

Data_Folder_Structure
- Class Label 1
  - image1.png
  - image2.png
  - ..
- Class Label 2
  - image1.png
  - image2.png
  - ..
'''

import args
import random
import os
import cv2


def get_image_paths(dataset_dir):
    # bee image paths
    image_paths = []
    bee_categories = os.listdir(dataset_dir)
    for bee_category in bee_categories:
        bee_category_path = os.path.join(dataset_dir, bee_category)
        bee_image_names = os.listdir(bee_category_path)
        for img_name in bee_image_names:
            bee_image_path = os.path.join(bee_category_path, img_name)
            image_paths.append([bee_category,bee_image_path])
    return image_paths


def create_bee_array(n_bees,bee_images_dir):
    bee_image_paths = get_image_paths(bee_images_dir)
    bee_image_array = []
    for i in range(n_bees):
        print(f'{len(bee_image_paths)} images found on {bee_images_dir} directory')
        select_bee = random.choice(bee_image_paths)
        bee_category = select_bee[0]
        print(bee_category)
        # bee_image_paths.remove(select_bee)

        bee_image = cv2.imread(select_bee[1])
        # bee scale
        # bee_image = cv2.resize(bee_image,(60,120))   # (w,h)
        scale_factor = random.uniform(args.BEE_RESIZE_SCALE_RANGE[0], args.BEE_RESIZE_SCALE_RANGE[1])  

        bee_image_resized = cv2.resize(bee_image, (0,0), fx=scale_factor, fy=scale_factor)
        print(f'{i+1} | {bee_image_resized.shape}')
        bee_image_array.append([bee_category,bee_image_resized])

    random.shuffle(bee_image_array)
    return bee_image_array

   
## sample call ##
# n_bees = random.randint(2,10)
# n_bees = 10
# print(f'n_beess : {n_bees}')
# bee_image_array = create_bee_array(n_bees,args.bee_images_dir)