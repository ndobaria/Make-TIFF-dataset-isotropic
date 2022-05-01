from skimage.io import imread, imsave
import pyclesperanto_prototype as cle
import os

class Voxel_size:
    x = 0.6934
    y = 0.6934
    z = 3.0
	
def makeIsotropic(input_folder_path, output_folder_path):
    file_names = os.listdir(input_folder_path)
    for file_name in file_names:
        if file_name.endswith(".tif"):
            
            #open the imgae
            image = imread(os.path.join(input_folder_path, file_name))
    
            #Rescale the image to make it isotropic
            rescaled = cle.scale(image, factor_x= Voxel_size.x, factor_y= Voxel_size.y, factor_z= Voxel_size.z, auto_size= True)
            
            #Create new isotropic images path
            new_file_name = os.path.splitext(file_name)[0] + '_isotropic.tif'
            output_file_path = os.path.join(output_folder_path, new_file_name)
        
            #Save isotropic images in output_file_path
            imsave(output_file_path, rescaled)
            
            #Saving message
            print('Saving..' + new_file_name)
    return
