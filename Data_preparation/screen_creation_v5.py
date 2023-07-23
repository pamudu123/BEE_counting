import numpy as np
import cv2
import random
import os

# import custome files
import args
from bee_factory import Bee
from image_transparent import image_overlay
from bee_corner import bee_corner_correction
from create_bee_image_array import create_bee_array
import folder_manager
from annotaion_generator import create_pascal_voc_annotations


frame_height = args.VIDEO_HEIGHT
frame_width = args.VIDEO_WIDTH

image = np.ones((frame_height, frame_width, 3), dtype=np.uint8) * 255
image[:, :] = args.BAGROUND_COLOUR  

# Add a small horizontal bar at the top of the image
bar_height = args.BAR_HEIGHT
image[:bar_height, :] = args.BAR_COLOUR


### Video ###
duration = args.DURATION
save_frequency_frames = args.SAVE_FREQUENCY * args.FPS_RATE

for c in range(args.N_VIDEOS):
    print("*"*50)
    video_path = folder_manager.create_video_path()
    print(f'{c+1} | {video_path}')
    print("*"*50)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Video codec
    video_writer = cv2.VideoWriter(video_path, fourcc,  args.FPS_RATE, (frame_width, frame_height))
    num_frames = duration *  args.FPS_RATE  # Total number of frames

    # bees initialize
    n_bees = random.randint(args.RANDOM_BEES_RANGE[0],args.RANDOM_BEES_RANGE[1])
    print(f'n_beess : {n_bees}')
    bee_image_array = create_bee_array(n_bees,args.BEE_IMAGES_DIR)

    bee_position_array = []
    for i in range(n_bees):
        bee_image_resized = bee_image_array[i][1]
        bee_image_height, bee_image_width = bee_image_resized.shape[:2]
        
        bee = Bee(bg_h=frame_height, bg_w=frame_width, bee_h=bee_image_height, bee_w=bee_image_width)
        print(bee)
        bee_position_array.append(bee)


    for frame_count in range(num_frames):
        bee_data = []
        background_image = image.copy()
        for i,bee in enumerate(bee_position_array):
            bee_image_resized = bee_image_array[i][1]
            bee_category = bee_image_array[i][0]

            bee_image_height, bee_image_width = bee_image_resized.shape[:2]
            pos_x , pos_y  = bee.update_bee_position()

            annotate_dict = {'bbox':(pos_x,pos_y,pos_x+bee_image_width,pos_y+bee_image_height) , 'label' : bee_category}
            bee_data.append(annotate_dict)
            
            ## check pos_x and pos_y within range
            bee_image_resized = bee_corner_correction(bee_image_resized,pos_x,pos_y, bg_h=frame_height, bg_w=frame_width, bee_h=bee_image_height, bee_w=bee_image_width)
            try:
                if bee_image_resized.shape[0] <= 0 or bee_image_resized.shape[1] <= 0:
                    new_frame = background_image   
                elif pos_x<=0:    
                    pos_x = 0
                    new_frame = image_overlay(background_image, bee_image_resized, location=(pos_x , pos_y), min_thresh=0, is_transparent=False)
                elif pos_y<=0:
                    pos_y = 0
                    new_frame = image_overlay(background_image, bee_image_resized, location=(pos_x , pos_y), min_thresh=0, is_transparent=False)
                else:
                    new_frame = image_overlay(background_image, bee_image_resized, location=(pos_x , pos_y), min_thresh=0, is_transparent=False)
            except Exception as e:
                print(f'{e}')
                continue

        # save annotations
        if frame_count%save_frequency_frames == 0:
            # save_image
            print(bee_data)
            img_path,xml_path = folder_manager.create_annotation_paths(video_path,frame_count)
            cv2.imwrite(img_path, new_frame)
            create_pascal_voc_annotations(img_path, bee_data, xml_path)


        cv2.imshow("Genearted Frame", new_frame)
        cv2.waitKey(1)

        video_writer.write(new_frame)

    video_writer.release()
cv2.destroyAllWindows()
