# Generating Haunted House Images
## Using StyleGAN2 ADA

This fun project was to train StyleGAN algorithm to generated Haunted House images. 

I chose StyleGAN2 ADA (Adaptive Discriminator Augmentation) developed by Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, Timo Aila ([article](https://arxiv.org/abs/2006.06676)), because the model can produce good results using only a few throusand training images, often matching StyleGAN2 results according to the authors.

In reality though, I ended up with only 150 reasonable training images that I could scrap from the web. However, considering the limited GPU resources using Google Colab I decided that the size of the dataset was enough to achieve my main goal: going through the training process from scratch. 

As expected, the output quality wasn't so realistic due to very small training dataset but nonetheless the output images carry the spookiness and creppiness very well! 

![output-summary](https://github.com/sooolee/StyleGAN2-haunted-house/blob/main/images-readme/output-summary.png)

## Data Scraping and Preprocessing

* To scrap the data from the web, I used Website-Image-Scraper built by [JJLIMMM](https://github.com/JJLimmm/Website-Image-Scraper). Initial downloads were just over 500, but aftering cleaning out the duplicates, cartoonish images, and other unusable images, the dataset was reduced to 150. 

* The original images varied in sizes. In order to feed them to StyleGan, they needed to be cropped into squares. Also considering the GPU resources, they were resized to 512x512. `process_img.py` was used for this preprocessing. 

## File Structure

Following file structure was used:

- [images](https://drive.google.com/drive/folders/1UQyKToqd3XU2Yf6ymu-aNFf2ceqmWM3q) - Raw images after preprocessing.
- [datasets](https://drive.google.com/drive/folders/1-5GiS5e4QFuYVsXKvHJPj4yW-MSEIULg) - The raw images were ran through `dataset_tool.py` as recommended by the authors and placed in this folder (even after initial preprocessing).
- [experiments](https://drive.google.com/drive/folders/1-XlNSwj17wK2hzY6bM9cOOKlo8LqFtJR) - Checkpoints and logs during the runs are recorded here. Checkpoints in pickle files were saved frequently to avoid losing data due to Colab disconnections.
- [outputs](https://drive.google.com/drive/folders/1g_JlKig0IzLOitaiaTgyufpXv-y1q5vb) - The output images.

## Training

- The model was cloned.

```
!git clone https://github.com/NVlabs/stylegan2-ada-pytorch.git
```

- I referenced jeffheaton's [YouTube](https://www.youtube.com/watch?v=L3JLzoe-dJU) and [Notebook](https://github.com/jeffheaton/present/blob/master/youtube/gan/colab_gan_train.ipynb) examples for running this model on Google Colab. :thumbsup: Credits go to jeffheaton.

## Outputs and Results

- As shown above, the output examples are far from realistic photos but catch well the spookiness of haunted house. Considering the very small training dataset (150 images), this was a pleasant surprise to me. 

- A total of 720 steps were ran resulting in 18 checkpoints (one checkpoint per 40 steps).

- Based on visual inspection, the outputs at around 520 steps seem to be slightly better than the rest of them. 

- However, looking at the logs, "fid50k_full" score already started being plataued around 320 - 360 steps. The lowest (best) score was 101.7 at 640 steps.

## What's Next?

- Increasing the dataset size would be definitly improve the output quality. 
- This training was done with default values for all output-impacting hyperparameters. It would be worth trying different values for some hyperparameters such as:
    - `--mirror=1` amplifies the dataset with x-flips. Often beneficial, even with ADA.
    - `--gamma=10` overrides R1 gamma. Trying a couple of different values for each new dataset is recommended.
    - `--aug=ada --target=0.7` adjusts ADA target value (default: 0.6).
    - `--augpipe=blit` enables pixel blitting but disables all other augmentations.
    - `--augpipe=bgcfnc` enables all available augmentations (blit, geom, color, filter, noise, cutout).

## Using Stable Diffusion to Improve Images

- Just for fun, I fed one of the output images from StyleGAN2 into Stable Diffusion v2 with a simple prompt 'haunted houses'. I got the following results. Pretty cool!

![sd-summary](https://github.com/sooolee/StyleGAN2-haunted-house/blob/main/images-readme/sd-summary.png)