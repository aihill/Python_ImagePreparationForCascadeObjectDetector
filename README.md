This code was written to assist with selecting 'positive' regions of images to train an image classifier. The idea is that you may have a repository of photographs of an image you want to identify, but you need to crop those photographs to as close as possible to the item of interest. You can do that with this simple UGUI, which also saves the 'negative' images that dont contain the item in case you need background/negative images for your training mechanisms.

The GUI is built with a few lines of Tkinter to produce a screen that looks like so. You produce the cropping rectangle by clicking on two points that will become diagonal corners of the cropping rectangle:


![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/whale_tk.png)

That will save the following images: 1 'positive' showing the item as cropped as you chose to make it:

![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/positive.jpg)

and 4 'negative' images showing irrelevant background that does not contain an item of interest:

![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative1.jpg)
![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative2.jpg)
![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative3.jpg)
![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative4.jpg)


