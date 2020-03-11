
import shutil
import os
i=0
for root,dirs, files in os.walk("/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/train_day_labels"):
    for file in files:
        if file.endswith('.json'):

            # if file == '00207869-046fa443.jpg':
                print("true")
                import shutil, os

                with open('/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/lists/testDRIT', 'r') as data:
                   plaintext = data.read()

                plaintext = plaintext.replace('\n', ',')
                plaintext = plaintext.replace('jpg', 'json')


                x=plaintext.split(",")


                for f in x:
                     # shutil.copy('/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/labels/train_day_labels/'+f, '/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/testcopy')
                     os.rename('/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/train_day_labels/'+f, "/home/abderrazzak/Desktop/baba/notation_DRIT_SORTIEREN/" + str(i) + ".json")
                     i=i+1
