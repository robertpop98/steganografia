#creazione disegno
amp=500                                                                
lar=500                                                                
img=createImage(lar,amp,RGB)
#pixel immagine vuota
img.loadPixels() 
#fl, linea nera                                                       
ln=0
#variabile che conta i quadrati                                                                  
q=0                                                                   
def setup():
    size(lar,amp)                                                     
    creaImg()                                                                   
def creaImg():
    global p,y,x,lar,amp,ln,q,z
#apertura file da steganografare    
    input=createInput("Input")                                           
    content=""                                       
    p=0  
#lettura e controllo valori da steganografare                                                                    
    while q<=10:                                                        
        val1 = input.read()                                            
        val2 = input.read()                                             
        val3 = input.read()                                             
        if val2==-1:                                                    
            val2=255                                                    
        if val3==-1:                                                    
            val3=255                                                    
        if val1==-1:                                                    
            if q==0:
                break
            else:
                for z in range (10-q):
                    for x in range (50):
                        for y in range (50):
#colorazione pixel nero
                            img.pixels[p+y+(lar*x)]=color(0,0,0)        
                            ln=1
        else:                                                             
            q+=1
            for x in range (50):
                for y in range (50):
#colorazione pixel
                    img.pixels[p+y+(lar*x)]=color(val1,val2,val3)         
        p=p+50                                                                
        if(p%lar==0):
            p=p+lar*49                                                       
            q=0                                                              
            if ln==1:                                                       
                break
    img.updatePixels()
#stampa immagine                                                         
    image(img,0,0)
#salva immagine                                                            
    save("Mistery.tiff")                                                          
    
