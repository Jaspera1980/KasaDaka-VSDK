
# coding: utf-8

# In[89]:


import wave


# In[90]:


dir = "/home/jasper/Documents/Group_6/"

infiles = [
    "Welcome_to_PoultryVet.wav",
    "Please_select_your_animal.wav",
    "for.wav",
    "chickens.wav",
    "press.wav",
    "1.wav",
    "for.wav",
    "fowls.wav",
    "press.wav",
    "2.wav",
    "for.wav",
    "ducks.wav",
    "press.wav",
    "3.wav",
    "for.wav",
    "turkeys.wav",
    "press.wav",
    "4.wav"    
]

outfile = "menu_1.wav"


# In[91]:


data= []
for wav in infiles:
    infile = dir+wav
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for x, y in enumerate(data):
    output.writeframes(data[x][1])
output.close()

