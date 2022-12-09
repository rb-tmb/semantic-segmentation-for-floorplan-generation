echo "Resizing the images...."
python resize_imgs.py
echo "Starting the Predictions..." 
python3 -u test_v2.py --imgs_inp Resized_images/ --imgs_out Output_images/ --cfg config/ade20k-resnet50dilated-ppm_deepsup.yaml
