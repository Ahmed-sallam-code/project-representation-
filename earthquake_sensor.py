from manim import * 
from numpy import sin 
class earth_quake(Scene):
    def construct(self):
      
        mass1 = Rectangle(width=3,height=4,fill_color=BLUE_C,color=PINK,fill_opacity=0.5)
        mass2 = Rectangle(width=3,height=4,fill_color=GREEN_C,color=PINK,fill_opacity=0.5)
        mass3 = Rectangle(width=3,height=4,fill_color=RED_C,color=PINK,fill_opacity=0.5)
        text1 = Text("M").set_color_by_gradient(RED_B,GOLD_B).set_height(1).move_to(mass1.get_center())
        text1.add_updater(lambda x,:x.move_to(mass1.get_center()))
        earth=Line(stroke_color=GREEN_C, stroke_width=5).set_width(10).next_to(mass1,DOWN,buff=0.1)
        earthtext=Text("Earth").set_color_by_gradient(BLUE,PINK).set_height(1)
        earthtext.add_updater(lambda x,:x.next_to(earth,DOWN))
        
        
        self.play(DrawBorderThenFill(mass1),Create(earth),run_time=1.5)
        self.play(Write(text1),Write(earthtext),run_time=1)
        self.wait()

        self.play(mass1.animate.shift((2)*RIGHT),earth.animate.shift((2)*RIGHT),run_time=1)
        self.wait()
        self.play(mass1.animate.shift((4)*LEFT),earth.animate.shift((4)*LEFT),run_time=2)
        self.wait()
        self.play(mass1.animate.shift((2)*RIGHT),earth.animate.shift((2)*RIGHT),run_time=1)
        self.wait()
        self.play(mass1.animate.move_to(mass2.get_center()))
        self.play(mass1.animate.set_height(1.4),text1.animate.set_height(0.25),runtime=1)
        self.play(DrawBorderThenFill(mass2),DrawBorderThenFill(mass3),run_time=1)
        self.play(mass2.animate.set_height(1.4).shift(1.4*DOWN),mass3.animate.set_height(1.4).shift(1.4*UP))
        text2 = Text("M").set_color_by_gradient(RED_B,GOLD_B).set_height(0.25).move_to(mass2.get_center())
        text3 = Text("M").set_color_by_gradient(RED_B,GOLD_B).set_height(0.25).move_to(mass3.get_center())
        text2.add_updater(lambda x,:x.move_to(mass2.get_center()))
        text3.add_updater(lambda x,:x.move_to(mass3.get_center()))
        self.play(Write(text2),Write(text3))
        self.wait()
        self.play(LaggedStart(earth.animate.shift((2)*RIGHT),mass2.animate.shift((2)*RIGHT),mass1.animate.shift(2*RIGHT),
                              mass3.animate.shift(2*RIGHT),lag_ratio=0.10,run_time=2))
        self.wait()
        self.play(LaggedStart(earth.animate.shift((4)*LEFT),mass2.animate.shift((4)*LEFT),mass1.animate.shift(4*LEFT),
                              mass3.animate.shift(4*LEFT),lag_ratio=0.10,run_time=3))
        self.wait
        self.play(LaggedStart(earth.animate.shift((2)*RIGHT),mass2.animate.shift((2)*RIGHT),mass1.animate.shift(2*RIGHT),
                              mass3.animate.shift(2*RIGHT),lag_ratio=0.10,run_time=2))
        self.wait()
        self.play(Unwrite(text1),Unwrite(text2),Unwrite(text3),Unwrite(earthtext))
        self.play(Uncreate(earth),Uncreate(mass1),Uncreate(mass2),Uncreate(mass3))
        self.wait()




