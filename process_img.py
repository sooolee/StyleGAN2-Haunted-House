from PIL import Image
import os



def process_imgs(path):
    """ 
    If the images are not square, crop the images to square, 
    then if the images are bigger then 512, resize to the max of 1/4 or 512. 
    """

    def crop_img(img):
        if img.size[0] > img.size[1]:
            cut = (img.size[0] - img.size[1]) / 2
            img = img.crop((cut, 0, cut, 0))
        elif img.size[0] < img.size[1]:
            cut = (img.size[1] - img.size[0]) / 2
            img = img.crop((0, cut, 0, cut))
        return img
    
    def resize_img(img):
        if img.size[0] > 512:
            scale = max(img.size[0]/4, 512)
            img = img.resize((scale, scale))
        return img
    
    imgs = os.listdir(path)
    imgs.remove('.DS_Store')

    for img in imgs:
        f_img = Image.open(path+img)
        if f_img.size[0] != f_img.size[1]:
            f_img = crop_img(f_img)
            f_img = resize_img(f_img)
            f_img.save(path+img)
        elif f_img.size[0] == f_img.size[1]:
            f_img = resize_img(f_img)
            f_img.save(path+img)