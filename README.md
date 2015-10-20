This code was written to assist with selecting 'positive' regions of images to train an cascade image detector. To use a cascade image detector, you must first train the detector by closely cropping the 'positive' regions of a photograph to show the object of interest. The rest of the image may be used as a 'negative' training image. This GUI lets you combine both tasks. You simply draw a rectangle around the object of interest by selecting diagonal corners of a rectangle and click 'Next' to save these positive and negative images. All images are saved in their original size, though the image is presented resized according to a scaling factor you  may have a repository of photographs of an image you want to identify, but you need to crop those photographs to as close as possible to the item of interest. You can do that with this simple UGUI, set in `imageeditor.py`. Similarly, in this file you can set the directory to store the positive and negative images.

Here's what the GUI looks like:

![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/whale_tk.png)

Use the `Reset` button to start the selection over with a given image. Use the `Next` button to indicate that selection is complete and images can be saved. That will save the following images: 1 'positive' showing the item as cropped as you chose to make it:

![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/positive.jpg)

and 4 'negative' images showing irrelevant background that does not contain an item of interest. These images are obtained by cutting out a left, right, top, and bottom rectangle relative to the 'positive' region, so as you see below, these 4 'negative' images will contain duplicate regions.

![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative1.jpg)
![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative2.jpg)
![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative3.jpg)
![ "data image"](https://github.com/sunnysideprodcorp/CascadeImagesorter/blob/master/sample-images/negative4.jpg)

To get started, fill in values for the following constants defined at the top of `imageeditor.py`:
```
IMAGE_DIRECTORY = 
POSITIVE_DIRECTORY = 
NEGATIVE_DIRECTORY = 
IMAGE_RESIZE_FACTOR = 
```
That should be sufficient to chug along. Also make sure to keep the file directories consistent between different work sessions if you are processing the same batch of photos. The `FileFeed` class will ensure that you avoid repeat editing by only selecting image files that have not already been processed.

Here's a brief rundown of the three classses used:

* `ImageEditor` is the `Tkinter` interface that presents a resized image and manages the region selection tools. It has an `ImageFeed` attribute to manage all`Image` module related activities and a `FileFeed` attribute to manage file selection. `FileFeed` forwards appropriate filenames directly to `ImageFeed`.

* `ImageFeed` manages all operations relating to manipulating an image file directly, particularly saving appropriate regions of photos to the appropriate directory as determined by a `FileFeed` attriute. `ImageFeed` also image scaling for convenient presentation and file type conversaion to move image file contents onto the `Tkinter` canvas.

* `FileFeed` determines what file to retrieve as well as appropriate positive and negative directory locations. As mentioned, above, `FileFeed` avoids duplicated work when files are edited in multiple sessions by referencing the image repository file names against positive/negative directory file names.

