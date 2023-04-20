from manim import *
 
class LCD(Scene):
    def construct(self):
        
        code = '''
        #include <LiquidCrystal.h>
        LiquidCrystal lcd(12, 11, 10, 9, 8, 7);
        class Lc{
        public:
        void LCD_Start();
        void acc_components(float x,float y,float z ); 
        void gyro_angles(float i,float p,float u );
        }; 
         '''
        code2 = '''
        void Lc::LCD_Start(){
            lcd.begin(16, 2);
            lcd.setCursor(15,0);
            lcd.print("Earthquake meter");
            int i=1;
            for(i=1;i<=34;i++){
                lcd.scrollDisplayLeft();
                delay(250); 
            }
            delay(900);
            lcd.clear();
            }
        '''
        code3 = '''
        void Lc::acc_components(float x,float y,float z){
            lcd.setCursor(0,0);
            lcd.print(x);
            lcd.setCursor(10,0);
            lcd.print(y);
            lcd.setCursor(6,1);
            lcd.print(z);
            }
        '''
        rendered_code = Code(code=code,language="c", background="window",font="Monospace",font_size=24,background_stroke_color='#009FBD')
        text = Text("Setting LCD UP").set_color_by_gradient(BLUE,RED).set_height(0.8).next_to(rendered_code,UP)
        rendered_code2 = Code(code=code2,language="c", background="window",font="Monospace",font_size=24,background_stroke_color='#009FBD')
        text2 = Text("As the porgram starts").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP)
        rendered_code3 = Code(code=code3,language="c", background="window",font="Monospace",font_size=24,background_stroke_color='#009FBD')
        text3 = Text("Displaying data").set_color_by_gradient(BLUE,RED).set_height(0.5).next_to(rendered_code2,UP)
        
        self.play(Write(rendered_code),Write(text))
        self.wait()
        self.play(ReplacementTransform(rendered_code,rendered_code2),ReplacementTransform(text,text2))
        self.wait()
        self.play(ReplacementTransform(rendered_code2,rendered_code3),ReplacementTransform(text2,text3))
        self.wait()
        