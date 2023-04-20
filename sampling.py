from manim import *
from numpy import sin
from numpy.fft import fft 

class sampling(Scene):
    def construct(self):
        t = np.arange(0,2*PI,0.01)
        sr = len(t)
        x=[]
        for i in range(len(t)):
            x.append(sin(t[i]))
        X = fft(x)
        N = len(X)
        n = np.arange(N)
        T = N/sr
        freq = n/T
        li = np.abs(X/N)

        plane2 = NumberPlane(x_range=[-2,10],y_range=[-1,1],x_length=4,y_length=6).add_coordinates()
        dots2=[]
        for i in range(len(li)):
            dot = Dot(color=PINK, radius=0.05, stroke_width=0).move_to(plane2.c2p(freq[i],li[i]))
            dots2.append(dot)

        plane = NumberPlane(x_range=[-2*PI,2*PI],y_range=[-2,2],x_length=4*PI,y_length=6).add_coordinates()
        plane_graph = plane.plot(lambda x: sin(x),x_range=[-2*PI,2*PI,0.01],color=GOLD_C)
        area = plane.get_riemann_rectangles(graph=plane_graph,x_range=[-2*PI,2*PI],dx=0.5*PI,color=[GREEN,BLUE],fill_opacity=1)
        area2 = plane.get_riemann_rectangles(graph=plane_graph,x_range=[-2*PI,2*PI],dx=0.1*0.5*PI,color=[GREEN,BLUE],fill_opacity=1)
        area3 = plane.get_riemann_rectangles(graph=plane_graph,x_range=[-2*PI,2*PI],dx=0.01*0.5*PI,color=[GREEN,BLUE],fill_opacity=1)
        label=Text("Sampling").set_color_by_gradient(BLUE,GREEN).set_height(0.75).move_to(plane,UP)
        #horz_line = Line(start=plane.c2p(3/4,plane_graph.underlying_function(3/4)),end=plane.c2p(3,plane_graph.underlying_function(3)),stroke_color=GREEN,stroke_width=3)
        label2=Text("Sampling with Nyquist frequency").set_color_by_gradient(BLUE,GREEN).set_height(0.5).move_to(plane,DOWN)
        label3=Text("Sampling with 10 times the Nyquist frequency").set_color_by_gradient(BLUE,GREEN).set_height(0.5).move_to(plane,DOWN)
        label4=Text("Sampling frequency tends to infinty").set_color_by_gradient(BLUE,GREEN).set_height(0.5).move_to(plane,DOWN)
        area2.save_state()
        dots =[]
        for i in range(40):
            dot = Dot(color=RED, radius=0.05, stroke_width=0).move_to(plane.c2p((i*2*PI)/(40), plane_graph.underlying_function((i*2*PI)/(40))))
            dots.append(dot)
        list_box = Rectangle(width=3, height=2,fill_color=BLUE,fill_opacity=0.6,color=GREEN).shift(4*LEFT)
        list_label=Text("List").set_color_by_gradient(RED,PURPLE).set_height(0.5)
        list_label.add_updater(lambda x,: x.move_to(list_box.get_center()))
        fft_box = Rectangle(width=3, height=2,fill_color=PURPLE_C,fill_opacity=0.6,color=GOLD_C).shift(4*RIGHT)
        fft_label=Text("FFT").set_color_by_gradient(RED,PURPLE).set_height(0.5).add_updater(lambda x,: x.move_to(fft_box.get_center()))
        arrow = Arrow(start=3*LEFT,end =2*RIGHT)
        arrow.next_to(list_box,RIGHT)
        spectrum_box=Rectangle(width=3, height=2,fill_color=PURPLE_C,fill_opacity=0.6,color=GOLD_C).shift(4*RIGHT)
        spectrum_label=Text("List Spectrum").set_color_by_gradient(RED,PURPLE).set_height(0.4).add_updater(lambda x,: x.move_to(spectrum_box.get_center()))
        arrow2 = Arrow(start=3*LEFT,end =2*RIGHT)
        arrow2.next_to(spectrum_box,LEFT)



        self.play(DrawBorderThenFill(plane))
        self.play(Create(plane_graph),run_time=3)
        self.wait()
        self.play(FadeIn(area),Write(label),Write(label2))
        self.wait()
        self.play(ReplacementTransform(area,area2),ReplacementTransform(label2,label3))
        self.wait()
        self.play(ReplacementTransform(area2,area3),ReplacementTransform(label3,label4))
        self.wait()
        self.play(Restore(area2),Unwrite(label4))
        self.wait()
        for i in range(40):
            self.play(Write(dots[i]),run_time=0.1)
        
        self.wait()    
        self.play(Uncreate(plane),Uncreate(plane_graph),Uncreate(plane),Uncreate(area2),Uncreate(area3),Unwrite(label))
        self.wait()
        self.play(DrawBorderThenFill(list_box))
        self.wait()
        for i in range(40):
            self.play(dots[-i].animate.next_to(list_box,RIGHT),run_time=0.15)
            self.play(dots[-i].animate.shift(2*LEFT),run_time=0.15)
            self.play(Unwrite(dots[-i]),run_time=0.1)
        self.play(Write(list_label))
        self.wait()
        self.play(LaggedStart(Create(arrow),DrawBorderThenFill(fft_box),Write(fft_label)),lag_ratio=0.1,run_time=3)
        self.wait()   
        self.wait()
        self.play(LaggedStart(Uncreate(list_box),Unwrite(list_label),Uncreate(arrow),fft_box.animate.shift(8*LEFT),DrawBorderThenFill(spectrum_box),Write(spectrum_label)),lag_ratio=0.1,run_time=4)
        self.wait()
        self.play(Create(arrow2))
        self.wait()
        self.play(LaggedStart(Uncreate(fft_box),Unwrite(fft_label),Uncreate(arrow2),spectrum_box.animate.shift(8*LEFT)),lag_ratio=0.1,run_time=4)
        self.wait()
        self.play(DrawBorderThenFill(plane2))
        for i in range(10):
            self.play(Write(dots2[i]),run_time=0.1)
        self.wait()    
        for i in range(10):
            self.play(Unwrite(dots2[i]),run_time=0.1)
        self.play(LaggedStart(Unwrite(spectrum_label),Uncreate(spectrum_box),Uncreate(plane2)),lag_ratio=0.1)
        self.wait()


        #self.play(Create(horz_line))
        #self.wait()
