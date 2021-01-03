# InstaDaily - Hours of scrolling, SIMPLIFIED!



InstaDaily is your daily dose of happiness, motivation, love, comedy, fetched straight from Instagram's servers, to your screens. It saves your hours of scrolling to get you that perfect photo you were searching for.

  - Highly curated content (Because I want the content to be as good as you <3)
  - No limit on usage (Yes, its free. Always!)
  - Secure (I will not steal your password. Ever. God Promise.)
  
![LOGO](https://i.ibb.co/RvfZ7dt/Webp-net-resizeimage.jpg)

# Features

  - You can search for any hashtag and retrieve the best of the content in it.
  - You can also mention the number of images you want to see on each run.
  - I'll never make you see the same image twice. Promise.


You can also (few upcoming features):
  - Clear the cached, previously fethced and shown images, with just a click.
  - Save the images you love permanently just by saying 'yes'. {I understand its always hard to let go of something you love.}  (upcoming).








### Installation
> PreRequisite: Anaconda, Python3 and pip installed and working.

- All the needed dependencies are saved in requirements.txt
- Follow these steps to run InstaDaily.


Step1: Clone the repo
```sh
#For Git Bash Users:
$ cd "Path you want to clone this repo to"
$ git clone https://github.com/vsengar26/InstaDaily.git
```
```sh
#For Non Git Bash Users:
-> Click the Green Colored Download Code button on top right of this page. 
-> Extract the contents of the downloaded file to the location you want to.
```

Step2: Installing the dependencies

Open Anaconda prompt and run the commands

```sh
> cd "path to parent directory"
> pip install -r requirements.txt

#OR

> pip install -r "path to requirements.txt file"
```

Step3: Uninstalling win-unicode-console

win-unicode-console is not compatible with InstaLoader and thus causes difficulties in taking inputs. To uninstall it simply run the following command in Anaconda Prompt.

```sh
> pip uninstall win-unicode-console
```

Step4: Changing the original instaloader.py file


- Copy the Instaloader.py file in the repo.
- Navigate to the address given in Instaloader_Path.txt file (you can copy and paste the path to the address bar of your computer as well.)
- Replace the original instaloader.py file.

Step5: Set your Instagram's username and password in the **details.txt** file. Further instructions are written in the file itself.

> We are ready to hop on to using InstaDaily for the first time. Excited enough?

# Usage

### Fetching the results

Step1: Running the python file.
```sh
#Open Anaconda prompt and navigate to the parent directory

> cd "path to parent directory"

> python main.py -t "#HASHTAGYOUWANTTOSCRAPE" -n "NUMBER OF IMAGES"
#OR
> python main.py --hashtag "#HASHTAGYOUWANTTOSCRAPE" -count "NUMBER OF IMAGES"
```

You can also run directly from anywhere also using,
```sh
> python {path/to/parent/directory}/main.py -t "#HASHTAGYOUWANTTOSCRAPE" -n "NUMBER OF IMAGES"

#OR

> python {path/to/parent/directory}/main.py --hashtag "#HASHTAGYOUWANTTOSCRAPE" --count "NUMBER OF IMAGES"
```
**ALL WITHOUT DOUBLE QUOTES "  "**

**ENTER HASHTAG WITHOUT '#'**

Step2: To move on to the next image, simply close you picture browser's window in which the image is currently being shown. It will re-open again with the new image.

**NOTE:** At any moment you want to close the program, simply close the anaconda prompt. However, it's not recommended as the records of shown images won't update for the session.

### To free up space

> The images fetched are downloaded into your system's internal storage.

Firstle, Edit the **Click_To_Clean** file using notepad and add the paths required in the space provided.

Now to free up the space: Double click on the **Click_To_Clean** file. This will remove all the previously downloaded images but will not affect the records and, you wont see the same image again, as promised :)



### Arguments

You can find the list of arguments used while running the file below.

| Argument | Description | Required? |
| ------ | ------ | ------ |
| **-t** OR **--hashtag** | The hashtag you want to look | YES |
| **-n** OR **--count** | Number of top images you want to view (default is **5**) | NO


### Further Considerations
Please have note that the number of images you give shall be considered by the program as final and you wont have the option to change the number in between as long as the life of program.

Program runs on a complex architecture which studies several posts (sometimes even thousands), and then return you the number of posts you wished for. So fetching might take some time especially, when you use this program repeatedly with the same hashtag in very small duration of intervals.

> Reminding again that the program shows you a manually controlled slideshow of images in your default image viewer. So after an image is shown, you need to close the viewer and then next image will be shown untill program shows you the number of images you asked for. In certain special cases, it will re-fetch the images with some less rigorous params, it will tell you the same when it does, so the content quality might decrease in such ocassions.









---



**Feel free to connect me on LinkedIn: https://www.linkedin.com/in/contactvishnu/**
**Feedbacks help me to improve**: https://forms.gle/ZPYbGBejShXGyrdX9
Check out InstaLoader GitHub: https://github.com/instaloader/instaloader

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
