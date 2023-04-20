from manim import* 
from numpy import sin

class main_idea(Scene):
    def construct(self):
        r=ValueTracker(0)

        plane = ComplexPlane().add_coordinates()
        MPU =always_redraw(lambda: Rectangle(width=3, height=2,fill_color=PURPLE_C,fill_opacity=1,color=GOLD_C).shift(r.get_value()*RIGHT))
        text = Text("MPU").set_color_by_gradient(BLUE,GREEN).set_height(0.4).add_updater(lambda x,: x.move_to(MPU.get_center()))
        text2 = Text("(Accelerometer)").set_color_by_gradient(BLUE,GREEN).set_height(0.2).add_updater(lambda x,: x.next_to(text,DOWN))
        arrow =Arrow(start=3*LEFT,end =2*RIGHT).next_to(MPU,DOWN)
        plane1=NumberPlane(x_range=[0,2*PI],y_range=[-1.5,1.5],x_length=PI,y_length=1.5).shift(2.25*UP,4*RIGHT)
        text3 = Text("(X-Accel)").set_height(0.4).next_to(arrow,DOWN,buff=0.1)
        sinGraph = plane1.plot(lambda x: sin(x),x_range=[0,2*PI,0.01],color=GOLD_C)
        text4=Text("(X-Accel component)").set_height(0.3).next_to(plane1,UP,buff=0.1)
        arrow2 = Arrow(start=3*DOWN,end=2*UP).next_to(MPU,LEFT)
        text5 =  Text("(Y-Accel)").set_height(0.4).next_to(arrow2,LEFT,buff=0.1)   
        plane2=NumberPlane(x_range=[0,2*PI],y_range=[-1.5,1.5],x_length=PI,y_length=1.5).shift(2.25*DOWN,4*RIGHT)
        sinGraph2 = plane2.plot(lambda x: sin(x),x_range=[0,2*PI,0.01],color=GOLD_C)
        text6=Text("(Y-Accel component)").set_height(0.3).next_to(plane2,UP,buff=0.1)

        self.play(LaggedStart(DrawBorderThenFill(plane),DrawBorderThenFill(MPU)),lag_ratio=0.2)
        self.play(LaggedStart(Write(text),Write(text2)),lag_ratio=0.2)
        self.play(Write(arrow),Write(text3),run_time=0.5)
        self.wait()
        for i in range(100):
            self.play(r.animate.set_value(sin(2*PI*i/100)),run_time=0.001*sin(2*PI/(i+1)))
        self.play(DrawBorderThenFill(plane1),Create(sinGraph),Write(text4),run_time=1)
        self.wait()
        self.play(LaggedStart(Unwrite(arrow),Unwrite(text3),Write(arrow2),Write(text5)),lag_ratio=0.2)
        self.wait()
        self.play(DrawBorderThenFill(plane2),Create(sinGraph2),Write(text6),run_time=1)
        self.wait()
        self.play(LaggedStart(Uncreate(plane2),Uncreate(plane1),Uncreate(sinGraph),Uncreate(sinGraph2),Unwrite(text6),Unwrite(text4),
                              Unwrite(text2),Unwrite(text),Uncreate(MPU),Unwrite(arrow2),Unwrite(text5),FadeOut(plane) ))
        self.wait()
       

       
        

        
       

