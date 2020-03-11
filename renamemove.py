# def main():
#     f= open("lists/test_night.txt","r")
#     f1= f.readlines()
#     for x in f1:
#         print(x)
#
#
# if __name__=="__main__":
#     main()
import shutil
import os
i=0
for root,dirs, files in os.walk("/home/abderrazzak/Desktop/NAME"):
    for file in files:
        if file.endswith('.png'):

            # if file == 'b1f4491b-846d8cb2.jpg':
                print("true")
                import shutil, os

                with open('/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/lists/testDRIT', 'r') as data:
                   plaintext = data.read()


                plaintext = plaintext.replace('\n', ',')


                x=plaintext.split(",")




                for f in x:
                     # print(x[i])
                     # i=i+1
                     # shutil.copy('/home/abderrazzak/BDD/testA/'+f, '/home/abderrazzak/Desktop/baba/image_DRIT_SORTIEREN')
                     # os.rename("C:/darth_vader/" + filename, "C:/darth_vader/" + str(i) + ".jpg")
                     os.rename('/home/abderrazzak/Desktop/NAME/'+str(i)+".png", "/home/abderrazzak/Desktop/baba/image_DRIT_FAKE/" + str(x[i]) )
                     # os.rename('/home/abderrazzak/NAME/'+f, "/home/abderrazzak/Desktop/baba/image_DRIT_SORTIEREN/" + str(i) + ".png")
                     i=i+1
