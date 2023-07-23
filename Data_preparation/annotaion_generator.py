import os
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from PIL import Image

def create_pascal_voc_annotations(image_path, annotations, output_path):
    # Read the image dimensions
    image = Image.open(image_path)
    width, height = image.size
    
    # Create the XML annotation file
    root = Element('annotation')
    
    # Add basic image information
    folder = SubElement(root, 'folder')
    folder.text = os.path.dirname(image_path)
    
    filename = SubElement(root, 'filename')
    filename.text = os.path.basename(image_path)
    
    path = SubElement(root, 'path')
    path.text = image_path
    
    source = SubElement(root, 'source')
    database = SubElement(source, 'database')
    database.text = 'synthesis dataset by Pamudu Ranasinghe'
    
    size = SubElement(root, 'size')
    width_elem = SubElement(size, 'width')
    width_elem.text = str(width)
    
    height_elem = SubElement(size, 'height')
    height_elem.text = str(height)
    
    depth = SubElement(size, 'depth')
    depth.text = '3'  # Number of Channels
    
    segmented = SubElement(root, 'segmented')
    segmented.text = '0'  # Not segmented
    
    # Add object bounding box information for each annotation
    for annotation in annotations:
        xmin, ymin, xmax, ymax = annotation['bbox']
        label = annotation['label']
        
        object_elem = SubElement(root, 'object')
        
        name = SubElement(object_elem, 'name')
        name.text = label
        
        pose = SubElement(object_elem, 'pose')
        pose.text = 'Unspecified'
        
        truncated = SubElement(object_elem, 'truncated')
        truncated.text = '0'  # Not truncated
        
        difficult = SubElement(object_elem, 'difficult')
        difficult.text = '0'  # Not difficult
        
        bndbox = SubElement(object_elem, 'bndbox')
        xmin_elem = SubElement(bndbox, 'xmin')
        xmin_elem.text = str(xmin)
        
        ymin_elem = SubElement(bndbox, 'ymin')
        ymin_elem.text = str(ymin)
        
        xmax_elem = SubElement(bndbox, 'xmax')
        xmax_elem.text = str(xmax)
        
        ymax_elem = SubElement(bndbox, 'ymax')
        ymax_elem.text = str(ymax)
    
    # Write the XML annotation to a file
    xml_str = minidom.parseString(tostring(root)).toprettyxml(indent="    ")
    with open(output_path, "w") as xml_file:
        xml_file.write(xml_str)
    
    print(f"Pascal VOC annotations created at: {output_path}")



#### Function Call ####
# bee_dict =  {
#     'pollen_bee' : 1,
#     'no_pollen_bee' : 0
# }


# image_path = 'dataset_samples/no_pollen/no_pollen_1.png'
# annotations = [
#     {'bbox': (100, 100, 200, 200), 'label': 'pollen_bee'},
#     {'bbox': (300, 300, 400, 400), 'label': 'no_pollen_bee'},
#     # Add more annotations as needed
# ]


# output_path = 'test_annotation.xml'
# create_pascal_voc_annotations(image_path, annotations, output_path)
