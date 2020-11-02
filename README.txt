Meme roulette :

Formatting Directories and Video :

avoid using spaces within the titles/names of directories/videos as this
will not work with the code because of how the code creates path names
to files within the directory. Instead of using spaces use underscores.

Make sure that all Directories/Video titles are capatalised this is very
important as python will read something like '\new direct' as 'ew direct'
as certain slashes and letter combinations are string literals

Setup :

You will need to pip install MoviePy using the console , the command is :
pip install Moviepy 

The first thing to do is to add an 'os.chdir()' command when you first run
the code as this will be where the 'data_meme_list' and 'data_meme_time' files
are stored and they are accesed by every function within the code.

Then run the update_selection() command to add videos to the files , have a 
seperate folder with only .mp4 videos init otherwise the function will return 
an error.

Functions :

update_selection() :
	This function should be run first as it reads all files within the 
	specified directory then adds them to a list. The specified directory
	should only contain .mp4 files so the code doesnt break , this is also
	the directory that the 'path' argument is referring to. The function 
	will create two .txt files titled 'data_meme_list' and 'data_meme_time'
	theese files are container of all the information , but arent that fragile
	if you edit the data within them and it breaks just run the update_selection()
	function again and they will be rebuilt. Theese files will be created where you
	changed the directory to upon set up. update_selection() takes one argument ,
	the path leading to the video container.

random_shuffle() :
	This function randomly shuffles all the videos specified within the 'data_meme_list'
	and 'data_meme_time' files. The function will wait the duration of the video plus 
	one second , to compensate for loading times (this number can be changed with in
	the update_selection() function). random_shuffle() takes no arguments.

order_shuffle() :
	This function plays the video in list order , the videos are defined within 
	'data_meme_list' and 'data_meme_time'. order_shuffle() takes no arguments.

select_shuffle() :
	This function allows you to play any video from 'data_meme_list'. select_shuffle()
	takes one argument which is the position of the video within the list of videos.

info() :
	This function returns the : average time , time_range , number of files and all the files paths 

	
		