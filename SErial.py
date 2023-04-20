from manim import *
 
class LCD(Scene):
    def construct(self):
        code = '''
        void setup() {
            Serial.begin(9600);
        }
        float x =0;
        float y =0;
        float z =0;
        void loop() {
            for(float i=0; i<=1; i+=0.001){
                x= sin(2*3.14*i*10)+6*cos(2*3.14*i*30)+3*sin(2*3.14*i*20);
                z= sin(2*3.14*i*10);
                y= sin(2*3.14*i*30);
                Serial.println(x);
                Serial.println(z);
                Serial.println(y);
                delay(1); 
            }}      
         '''
        code2 = '''
        ''com_ard.py''
        import serial
        import time
        import serial.tools.list_ports
        a=serial.tools.list_ports.comports()
        print(a)
        acceleration_listx = []
        acceleration_listy = []
        acceleration_listz = []
        def get_serial():
            #setting communication port with BudRate 
            serialCom = serial.Serial('COM3',9600)
        #reseting arduino for fresh input
        serialCom.setDTR(False)
        time.sleep(1)
        serialCom.flushInput()
        serialCom.setDTR(True)

        k = 1000 #number of samples

        #aquiring data from the serial port
            for i in range(k):
                try:
                    accelorometer_data = serialCom.readline()
                    accelorometer_data = accelorometer_data.decode()
                    accelorometer_data = accelorometer_data.strip('/r/n')
                    #accelorometer_data =float(accelorometer_data)
                    acceleration_listx.append(accelorometer_data)
                    time.sleep(0.001)
                except:
                    print("Error encountered, line was not recorded.")
        serialCom.close()
        #returning data list 
        def accel_listx():
            return acceleration_listx
        '''
        code3 = '''
        import FFT_Sallam as wryyy
        import numpy as np 
        import com_ard as com
        com.get_serial()

        sr = len(com.acceleration_listx)/1
        t = np.arange(0,1,1/(len(com.acceleration_listx)))
        s=com.accel_listx()
        for i in range(len(s)):   
            try:  
                s[i]=float(s[i])
            except:
                s[i]=(float(s[i-10])+float(s[i+10]))/2
                print("Error encountered, couldn't covert to float")
            print(s)  

        wryyy.plot_fft(s,sr,t,"Frequency(hz)","time(s)","amplitude x","amplitude")        
        '''
        #arduino = ImageMobject()
        text0 = Text("Calibrating Communication Channel").set_color_by_gradient(BLUE,RED).set_height(0.8)
        rendered_code = Code(code=code,language="c", background="window",font="Monospace",font_size=20,background_stroke_color='#009FBD')
        text = Text("Arduino C Code").set_color_by_gradient(BLUE,RED).set_height(0.4).next_to(rendered_code,UP)
        rendered_code2 = Code(code=code2,language="python", background="window",font="Monospace",font_size=12,background_stroke_color='#009FBD')
        text2 = Text("Python Code").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP,buff=0.05)
        rendered_code3 = Code(code=code3,language="python", background="window",font="Monospace",font_size=20,background_stroke_color='#009FBD')
        text3 = Text("Displaying Spectrum").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP,buff=0.05)
        output = ImageMobject("images\Figure_1.png").scale(1.2)
        output2 = ImageMobject("images\Figure_2.png").scale(1.2)
        output3 = ImageMobject("images\Figure_3.png").scale(1.2)
        text4 = Text("sin(2*3.14*i*10)+6*cos(2*3.14*i*30)+3*sin(2*3.14*i*20)").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP,buff=0.05) 
        text5 = Text("sin(2*3.14*i*30)").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP,buff=0.05) 
        text6 = Text("sin(2*3.14*i*10)").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP,buff=0.05)        
        
        

        self.play(Write(text0))
        self.wait(2)
        self.play(Write(rendered_code),ReplacementTransform(text0,text))
        self.wait(5)
        self.play(ReplacementTransform(rendered_code,rendered_code2),ReplacementTransform(text,text2))
        self.wait(5)
        self.play(ReplacementTransform(rendered_code2,rendered_code3),ReplacementTransform(text2,text3))
        self.wait(5)
        self.play(Unwrite(text3),Unwrite(rendered_code3))
        self.play(Write(text4),FadeIn(output))
        self.wait(3)
        self.play(ReplacementTransform(output,output2),ReplacementTransform(text4,text5))
        self.wait(3)
        self.play(ReplacementTransform(output2,output3),ReplacementTransform(text5,text6))
        self.wait(3)
        self.play(FadeOut(output3),Unwrite(text6))
        self.wait()
