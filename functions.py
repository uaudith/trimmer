from subprocess import Popen , PIPE
import subprocess
from IPython.display import HTML, clear_output
import time
import ipywidgets as widgets
from IPython.display import display
def ad():
  
  print('''

                               _____          _           _       _                       
                       _   _  |___ /    ___  (_)   __ _  | |__   | |_                     
   _____ _____ _____  | | | |   |_ \   / _ \ | |  / _` | | '_ \  | __|  _____ _____ _____ 
  |_____|_____|_____| | |_| |  ___) | |  __/ | | | (_| | | | | | | |_  |_____|_____|_____|
                       \__,_| |____/   \___| |_|  \__, | |_| |_|  \__|                    
                                                  |___/                                   

  ''')

def tformat(times):
  hour=0
  minutes=0
  if times>=3600:
    hour=times//3600
    times= times -hour*3600
  if times >= 60:
    minutes=times//60
    times=times-minutes*60
  return '{} hours {} minutes and {} seconds'.format(hour,minutes,times)
outname=''
def trim(path,start,duration):
  global outname
  loadingBtn = widgets.Button(description = "Generating",
                          disabled = True,
                          button_style = 'info', # 'success', 'info', 'warning', 'danger' or '' 
                          tooltip = "Uploading",
                          icon = 'check')

  fname=path.split('/')[-1]
  #outname=(' ').join(fname.split('.')[:-1])+' '+tformat(duration)+'  from '+tformat(start)+'.'+fname.split('.')[-1]
  outname=fname
  p=Popen(['ffmpeg' ,'-ss', str(start), '-i', path ,'-t', str(duration) ,'-c', 'copy', 
          outname],
          stdout=PIPE,
          stderr=PIPE)
  while True:
    if not p.poll == None:
      clear_output(wait=True)
      path=video_path.split('/')
      path[-1]=''
      pathstr = '/'.join(str(part)for part in path)

      p2 = Popen(["mv", outname,pathstr], stdout=subprocess.PIPE)
      #get_ipython().system_raw('cp "{}" "{}"'.format(outname,pathstr))
      break


def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  y= [x.decode('ascii').split(',')[0][2:] for x in result.stdout.readlines() if "Duration" in x.decode('ascii')]
  dins=int(y[0].split(':')[1:][0])*3600+int(y[0].split(':')[1:][1])*60+float(y[0].split(':')[1:][2])
  return y , dins

def abutton(name):
  button = widgets.Button(description=str(name))
  output = widgets.Output()
  display(button, output)
  return button

def htmltext(text):
  return display(HTML("<center><h3 style=\"font-family:Trebuchet MS;color:#0000FF;\">{}</h3><br></center>".format(text)))
