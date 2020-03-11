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
for root,dirs, files in os.walk("/home/abderrazzak/BDD/testA"):
    for file in files:
        if file.endswith('.jpg'):

            # if file == 'b1f4491b-846d8cb2.jpg':
                print("true")
                import shutil, os

                with open('/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/lists/testDRIT', 'r') as data:
                   plaintext = data.read()

                plaintext = plaintext.replace('\n', ',')


                x=plaintext.split(",")


                for f in x:
                     shutil.copy('/home/abderrazzak/BDD/testA/'+f, '/home/abderrazzak/Desktop/baba/image_DRIT_SORTIEREN')
