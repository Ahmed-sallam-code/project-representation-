from manim import *
 
class MPU(Scene):
    def construct(self):
        code='''
        #include <Adafruit_MPU6050.h>
        #include <Adafruit_Sensor.h>
        #include <Wire.h>
        Adafruit_MPU6050 mpu;
        void setup() {
            while (!mpu.begin()) {
                Serial.println("MPU6050 not connected!");
                delay(1000);
            }
        Lc obj;
        obj.LCD_Start();    
        }
        '''
        code2 = '''
        sensors_event_t event;

        void loop() {
            mpu.getAccelerometerSensor()->getEvent(&event);
            Lc ob;
            ob.acc_components(event.acceleration.
            x,event.acceleration.y,event.acceleration.z);
    
            Serial.println(event.acceleration.x);
            Serial.println(event.acceleration.y);
            delay(500);

        '''
        rendered_code = Code(code=code,language="c", background="window",font="Monospace",font_size=24,background_stroke_color='#009FBD')
        text = Text("Setting MPU Up").set_color_by_gradient(BLUE,GREEN).set_height(0.8).next_to(rendered_code,UP)
        rendered_code2 = Code(code=code2,language="c", background="window",font="Monospace",font_size=24,background_stroke_color='#009FBD')
        text2 = Text("MPU SetUp").set_color_by_gradient(BLUE,GREEN).set_height(0.5).next_to(rendered_code2,UP)

        self.play(Write(rendered_code),Write(text))
        self.wait()
        self.play(ReplacementTransform(rendered_code,rendered_code2),ReplacementTransform(text,text2))
        self.wait()
