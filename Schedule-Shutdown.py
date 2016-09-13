# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:44:00 2016

@author: Guilherme Pereira
email: guipinper@gmail.com

"""



import math
import datetime
import os
import tkinter as tk


w = 350
h = 500
raio = w * 0.9 * 0.5
string = str(w) + "x" +str(h)

intrevalos = [x for x in range(15, 360, 30)]
intrevalos_certos = [x for x in range(0, 360, 30)]

x_inicial = 0
y_inicial = 0
horas_marcadas = 10
minutos_marcados = 10

class Example(tk.Frame):     
  
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)            
        self.parent = parent        
        self.initUI()
        
        
    def initUI(self):       
        
        def schedule():
            now = datetime.datetime.now().time()
            total_min_agora = now.hour*60 + now.minute
            total_min_mar = horas_marcadas*60 + minutos_marcados
            falta = 0
            
            if total_min_mar < total_min_agora:
                falta = ((24*60 - total_min_agora) + total_min_mar) * 60
                
            if total_min_mar >= total_min_agora:
                falta = (total_min_mar- total_min_agora) * 60
            os.system("shutdown /s /t %s" %falta)
            
            
            
        def cancel():
            os.system("shutdown /a")
            
        #drags the minuts pointer
        
        def drag_minutos(event):
            global minutos_marcados
            coordy = h*0.5 - event.y
            coordx = event.x - w*0.5
            raio1 = 10
            angulo = math.atan2(coordy, coordx) * 360 / (2*math.pi) 
            
            if angulo < 0:
                angulo = 360 + angulo
            centerx3 = (centerx) + raio*0.8*math.cos(angulo * 2 * math.pi / 360)
            centery3 = (centery) - raio*0.8*math.sin(angulo * 2 * math.pi / 360)
            
            canvas.coords(ponteiro_minutos, [centerx3-raio1, centery3-raio1, centerx3+raio1, 
                                             centery3+raio1])
            canvas.coords(linha_minutos, [centerx, centery, centerx3, centery3])
            
            minutos_marcados = int(((360-(angulo))*60/360) + 15)
            
            if minutos_marcados >= 60:
                minutos_marcados = minutos_marcados - 60
                
            h3.config(text = str(minutos_marcados))
            
                      
            
        def click(event):
            global x_inicial
            global y_inicial
            y_inicial = event.y
            x_inicial = event.x
       
       
       #grad the hours pointer around, and only has the values from hours to be on
        def drag(event):
            global x_inicial
            global y_inicial
            global raio
            global horas_marcadas
            
            fator = 0.9
            hipotenusa = math.sqrt((event.x - w*0.5 )**2 + (h*0.5 - event.y)**2)
            angulo_final = 0
            
            if hipotenusa <= raio*0.8:
                fator = 0.7
                
            if x_inicial != event.x and y_inicial != event.y:
                coordy = h*0.5 - event.y
                coordx = event.x - w*0.5
                angulo = math.atan2(coordy, coordx) * 360 / (2 * math.pi) 
                
                if angulo < 0:
                    angulo = 360 + angulo 
                
                for i in range(len(intrevalos)-1):                    
                    if angulo > intrevalos[i] and angulo <= intrevalos [i+1]:
                       
                        angulo_final = (intrevalos[i] + intrevalos [i+1]) * 0.5 
                      
                        centro_novox = w/2 + fator*raio*math.cos(angulo_final * 2 * math.pi / 360)
                        centro_novoy = h/2 - fator*raio*math.sin(angulo_final * 2 * math.pi / 360)
                        
                        raio1 = 10 
                        
                        canvas.coords(ponteiro_horas, [centro_novox - raio1, centro_novoy - raio1,
                                                       centro_novox + raio1,centro_novoy + raio1])
                                                       
                        canvas.coords(linha_horas,[centerx, centery,
                                                   centro_novox, centro_novoy])
                    
                    
                    if angulo < 15 and angulo >= 0 or angulo > 345 and angulo <= 360:                        
                        angulo_final = 0 
                        raio1 = 10

                        centro_novox = w/2 + fator*raio*math.cos(angulo_final * 2 * math.pi / 360)
                        centro_novoy = h/2 - fator*raio*math.sin(angulo_final * 2 * math.pi / 360)
                                                
                        canvas.coords(ponteiro_horas, [centro_novox - raio1, centro_novoy - raio1,
                                                       centro_novox + raio1, centro_novoy + raio1])
                                                       
                        canvas.coords(linha_horas,[centerx, centery,
                                                   centro_novox, centro_novoy])
              
              
                horas_marcadas =  360 - (angulo_final + 270 )
                
                if horas_marcadas <= 0:
                    horas_marcadas = horas_marcadas + 360
                horas_marcadas = int(horas_marcadas * 12 / 360)
                
                if fator == 0.9:
                    horas_marcadas = horas_marcadas + 12
                horas_mar = str(horas_marcadas)
                
                if horas_marcadas == 24 :
                    horas_marcadas = 0
                    
                if horas_marcadas < 10:
                    horas_mar = "0" + str(horas_marcadas)
                    
                h1.config(text = horas_mar)
                
                x_inicial = event.x
                y_inicial = event.y
     
        self.parent.title("Lines")        
        self.pack(fill="both", expand=1)
        
        centerx = w * 0.5
        centery =  h * 0.5
        
        canvas = tk.Canvas(self,bg = "grey")
        canvas.create_oval(centerx - raio, centery - raio,
                           centerx + raio, centery + raio, fill="black")        
       
        angle_step = int(360 / 12)        
        horas = 1
        inicio = -60
        fim = inicio + 360
        for angle in range(inicio, fim, angle_step):
            angle1 = angle * 2 * math.pi / 360
            canvas.create_text((centerx ) + raio*0.9*math.cos(angle1),
                               (centery ) + raio*0.9*math.sin(angle1), fill="white",
                               font="Times 10 italic bold", text=str(horas + 12))
                                
            canvas.create_text((centerx) + raio*0.7* math.cos(angle1),
                               (centery) + raio*0.7*math.sin(angle1),fill="white",
                               font="Times 10 italic bold", text=str(horas))                      
            horas += 1            
            
        centerx1 = (centerx) + raio*0.9*math.cos(angle1)
        centery1 = (centery) + raio*0.9*math.sin(angle1)
        
        centerx2 = (centerx) + raio*0.8*math.cos(angle1 * 0.5)
        centery2 = (centery) + raio*0.8*math.sin(angle1 * 0.5)
        
        posix = 10
        posiy = 10
               
        ponteiro_horas = canvas.create_oval(centerx1 - posix, centery1 - posiy,
                                            centerx1 + posix, centery1 + posiy ,
                                            tags = "circle", fill = "white")
                                            
        canvas.tag_bind("circle", "<B1-Motion>", func=drag)
        canvas.tag_bind("circle", "<Button-1>", func=click)
        
        linha_horas = canvas.create_line(centerx, centery, centerx1,
                                         centery1, tags = "linha_horas",
                                         fill = "white")
        
        linha_minutos = canvas.create_line(centerx, centery, centerx2,
                                           centery2, tags = "linha_minutos", fill = "white")
                                           
        ponteiro_minutos = canvas.create_oval(centerx2 - posix, centery2 - posiy , 
                                              centerx2 + posix,centery2 + posiy ,
                                              tags = "circle_minutos",fill = "white")
                           
        canvas.tag_bind("circle_minutos","<B1-Motion>", func=drag_minutos)
              
        canvas.pack(fill="both", expand=1)        
        
        b = tk.Button(self,  text="Schedule", width = int(w * 0.1),
                      bg = "black", fg = "white",command = schedule)        
        b.pack()
        b.place(x = w*0.13, y = h*0.85)
        
        b1 = tk.Button(self,  text="Cancel", width = int(w * 0.1),
                       bg = "black", fg = "white",command = cancel)        
        b1.pack()
        b1.place(x = w*0.13, y = h*0.9)
        
        h1 = tk.Label(self, text = "00", font=("Courier", 44), bg = "black", fg = "white")
        h1.pack()
        h1.place(x = w*0.24, y = h*0.03)
        
        h2 = tk.Label(self, text = ":", font=("Courier", 44), bg = "black", fg = "white")
        h2.pack()
        h2.place(x = w*0.44, y = h*0.03)
        
        h3 = tk.Label(self, text = "00", font=("Courier", 44), bg = "black", fg = "white")
        h3.pack()
        h3.place(x = w*0.54, y = h*0.03)


def main():
  
    root = tk.Tk()
    Example(root)
    
    root.geometry(string)
    root.mainloop()  


if __name__ == '__main__':
    main()  
        
    

