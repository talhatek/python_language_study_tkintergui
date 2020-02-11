import yaml
import os.path
def read_each_node(a):
  russian_word=[]
  transcription=[]
  hint=[]
  turkish=[]
  YAML_NAME=a+".yml"
  with open(YAML_NAME,"r",encoding="utf-8")as nodes:
    data=yaml.load(nodes, Loader=yaml.FullLoader)
  just=data.get(a)
  for x in data:
    for y in data.get(x):
      for key,value in data.get(x).get(y).items():
        if(key=="hint"):
          hint.append(value)
        elif(key=="russian_word"):
          russian_word.append(value)
        elif(key=="transcription"):
          transcription.append(value)
        elif(key=="turkish"):
          turkish.append(value)
  return russian_word,transcription,hint,turkish

def add_topic(new_one):
  oldies=[]
  entire={}
  with open("topics.yml","r",encoding="utf-8")as nodes:
      data=yaml.load(nodes, Loader=yaml.FullLoader)
   
  for x,y in data.items():
    for z in y:
      oldies.append(z)
  oldies.append(new_one)

  entire['topics']=oldies
 
  with open("topics.yml","w",encoding="utf-8")as nodes:
    yaml.dump(entire,nodes)

def get_topics():
  oldies=[]
  with open("topics.yml","r",encoding="utf-8")as nodes:
      data=yaml.load(nodes, Loader=yaml.FullLoader)
  for x,y in data.items():
    for z in y:
      oldies.append(z)
  return oldies

def get_len(a):
  cnt=0
  YAML_NAME=a+".yml"
  with open(YAML_NAME,"r",encoding="utf-8")as nodes:
    data=yaml.load(nodes, Loader=yaml.FullLoader)
  for x in data:
    for y in data.get(x):
      cnt=cnt+1
  return cnt


def add_node(filename,a,b,c,d):
  fname=filename+".yml"
  if(os.path.isfile(fname)):
    with open(fname,"r",encoding="utf-8")as nodes:
      data=yaml.load(nodes, Loader=yaml.FullLoader)
    print(data)  
    just=data.get(filename)
    queue=get_len(filename)
    just[queue+1]={'hint': a, 'russian_word': b, 'transcription': c, 'turkish': d}
    final=just.copy()
    empty={}
    empty[filename]=final
    with open(fname,"w",encoding="utf-8")as nodes:
      yaml.dump(empty, nodes,allow_unicode=True)
  else:
    add_topic(filename)
    topush={filename:{1:{'hint': a, 'russian_word': b, 'transcription': c, 'turkish': d}}}
    with open(fname,"w",encoding="utf-8")as nodes:
      yaml.dump(topush, nodes,allow_unicode=True)



