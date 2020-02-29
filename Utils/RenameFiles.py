
# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 

dirpath = "C:/Users/Shweta/Documents/MCA/SEM6/Zargun/Datasets/PET"
  
# Function to rename multiple files 
def main(): 
    i = 1
      
    for filename in os.listdir(dirpath): 
        dst ="pet" + str(i) + ".jpg"
        src = dirpath + filename 
        dst = dirpath + dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 