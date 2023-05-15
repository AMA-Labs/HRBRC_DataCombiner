Unzip testcsvs.zip to a directory.  

From the directory datacombiner.py is in run:
python datacombiner.py -h to see a description of  all the parameters

Then run:
python datacombiner.py -d ./directory -f1 heartrate.csv -f2 oxygendata.csv -f datalob.csv

where directory is the path you unziped the csv files to.

The system will save combined_sotred.csv to your current directory.

Alternatively run:
python datacombiner.py 

in the directory you unziped the archive to.  When you run the command, it will grab the first oxygen sensor file, heart rate sensor file and HRBRC sensor file and combine them into a new csv called combined_sorted.csv and save it in the directory you are running datacombiner.py


