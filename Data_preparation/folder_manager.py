'''
These functions are used to create folders and save images and XML files 
with suitable names without naming issues.
'''

import os
import args


def check_directory(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'folder created : {folder_path}')
    else:
        print(f'folder exists : {folder_path}')


## for save annotation data
image_folder = os.path.join(args.ANNOTATIONS_DIR,'images')
pascal_annotation_folder = os.path.join(args.ANNOTATIONS_DIR,'pascal_bbox')

check_directory(image_folder)
check_directory(pascal_annotation_folder)

## for save videos
def create_video_path():
    n_videos = len(os.listdir(args.save_video_dir))
    video_name = f'rec_{n_videos+1}.avi'
    video_path = os.path.join(args.save_video_dir,video_name)
    return video_path

## for save frames
def create_annotation_paths(video_path,frame_num):
    video_name = (video_path.split("/")[-1]).split(".")[0]
    
    image_name = f'{video_name}_{frame_num}.png'
    image_path = os.path.join(image_folder,image_name)

    xml_name = f'{video_name}_{frame_num}.xml'
    xml_path = os.path.join(pascal_annotation_folder,xml_name)
    return image_path,xml_path


