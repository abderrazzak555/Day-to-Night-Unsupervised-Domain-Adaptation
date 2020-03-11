import json
import glob

read_files = glob.glob("/home/abderrazzak/Desktop/training_supervised/testbilder_night-day/test_night_day_val_labels/*.json")
with open("/home/abderrazzak/daytraining/val_test_night_day_Bilder.json", "w") as outfile:
    outfile.write('[{}]'.format(
        ','.join([open(f, "r").read() for f in read_files])))
