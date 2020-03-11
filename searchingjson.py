
import shutil
import os
for root,dirs, files in os.walk("/home/abderrazzak/Desktop/BDD/bdd100k_labels/bdd100k/labels/100k/val"):
    for file in files:
        if file.endswith('.json'):

            # if file == '00207869-046fa443.jpg':
                print("true")
                import shutil, os

                with open('lists/train_day.txt', 'r') as data:
                   plaintext = data.read()

                plaintext = plaintext.replace('\n', ',')
                plaintext = plaintext.replace('jpg', 'json')


                x=plaintext.split(",")


                for f in x:
                     shutil.copy('/home/abderrazzak/Desktop/BDD/bdd100k_labels/bdd100k/labels/100k/val/'+f, '/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/testcopy')
