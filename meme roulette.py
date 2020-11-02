import os , time , math
from random import randint
from moviepy.editor import VideoFileClip

class meme_roulette():


      def __load_meme_select__():
        meme_select = []
        with open ('data_meme_list') as meme_list:
          for lines in meme_list :
            meme_select.append(lines.rstrip('\n'))
        return meme_select

      def __load_meme_select_time__():
        meme_select_time = []
        with open ('data_meme_time') as meme_time:
          for lines in meme_time:
            meme_select_time.append(int(lines.rstrip('\n')))                           
        return meme_select_time                           
                    
      def update_selection(path):

        write_data_clear = open('data_meme_list','w')
        write_time_clear = open('data_meme_time','w')

        write_data_clear.truncate(0)
        write_time_clear.truncate(0)

        write_data_clear.close()
        write_time_clear.close()
        path = str(path)
        current_memes = os.listdir(path)
        for memes in range(0,len(current_memes)):
          
          path_meme = (path + current_memes[memes]).replace(' ','')
          meme = VideoFileClip(path_meme)
          time_stamp = math.floor(meme.duration) + 1
          
          write_data = open('data_meme_list','a')
          write_time = open('data_meme_time','a')

          write_data.write(str(path_meme) + '\n')
          write_time.write(str(time_stamp) + '\n')
          print (memes ,' out of ',len(current_memes) - 1,' added to system')
          
        write_data.close()
        write_time.close()
                         
         
      def random_shuffle():
        meme_select = meme_roulette.__load_meme_select__()
        meme_select_time = meme_roulette.__load_meme_select_time__()
        
        print("shuffling out of : ",len(meme_select),"\n")

        while True:
          selector = randint(0,(len(meme_select)-1))
          print("Time : ",meme_select_time[selector]," File Path : ",meme_select[selector])
          os.startfile(meme_select[selector])
          time.sleep(meme_select_time[selector])
          
      def order_shuffle():
        meme_select = meme_roulette.__load_meme_select__()
        meme_select_time = meme_roulette.__load_meme_select_time__()
        
        for meme in range(0,len(meme_select)):
                          print("Time : ",meme_select_time[meme]," File Path : ",meme_select[meme])
                          os.startfile(meme_select[meme])
                          time.sleep(meme_select_time[meme])
                        
          
      def select_meme(position):
        try:
          meme_select = meme_roulette.__load_meme_select__()
        
          os.startfile(meme_select[position])
        except IndexError :
          print('Attempting to play file out of range try playing video within range between 0 to',len(meme_select) -1 )

      def info():
        meme_select = meme_roulette.__load_meme_select__()
        meme_select_time = meme_roulette.__load_meme_select_time__()
        
        print(" Time Range : ", max(meme_select_time) - min(meme_select_time))
        print(" Time Average : ", sum(meme_select_time)/(len(meme_select_time))+1)
        print("\n Files in Index : ",len(meme_select))
        print(" Files List : ")
        for meme in range(0,len(meme_select)):
          print("",meme_select[meme],'-- Position : ',meme)
