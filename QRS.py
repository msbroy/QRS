import os, sys, time, csv, subprocess
from datetime import datetime

print("------- Welcome to QR Code Scanner by Biprodeep Roy v1.0 ------")

count=1
output=dict()
def writetocsv(output=dict()):
    s=datetime.now().strftime('%y%m%d_%H%M%S')+".csv"
    csvfilepath=os.path.join("/opt/lampp/htdocs",s)
    with open(csvfilepath, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        head=["ITEM_NUMBER","UID","ITEM_NAME", "WEIGHT", "PRICE","DISCOUNT","GST_RATE","DATE","TIME"]
        writer.writerow(head)
        for key, value in output.items():
            writer.writerow([key, value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7]])
    nfilepath=os.path.join("/opt/lampp/htdocs","myfile.txt")
    with open(nfilepath, 'w') as f:
        f.write(s)
        f.close()

def strtodict(out):
    pos1=out.find(",")
    pos2=out.find(",",pos1+1)
    pos3=out.find(",",pos2+1)
    pos4=out.find(",",pos3+1)
    pos5=out.find(",",pos4+1)
    pos6=out.rfind(",")
    output.update({int(count):(out[0:pos1],out[pos1+1:pos2],out[pos2+1:pos3],out[pos3+1:pos4],out[pos4+1:pos5],out[pos5+1:pos6],str(time.strftime('%d/%m/%Y')),str(time.strftime('%H:%M:%S')))})

while True:
    try: 
        out = str(subprocess.check_output("./stub"))
        out=out[8:out.rfind(',')+1]
        print out
        if(len(out)>+1):
            strtodict(out)
            count+=1
        time.sleep(.5)
    except KeyboardInterrupt:
        print 'QRS Checking Done! Now writing to Registry...'
        time.sleep(0.2)
        # Write to CSV file
        writetocsv(output)
        print 'ALL DONE ! :)\n\n\n'
        break