from manim import *

class TusiCouple(Scene):
    def construct(self):
        main_circle_radius = 3
        origin_point = np.array([0,0,0])
        period = 4
        rev = 2*PI

        # rotating_dot
        phase = ValueTracker(0*DEGREES)
        rotating_dot = always_redraw(lambda: Dot(point=[main_circle_radius*np.cos(phase.get_value()),main_circle_radius*np.sin(phase.get_value()),0], color=YELLOW))
        rotating_dot_vect_length = np.sqrt((rotating_dot.get_center()[0] - origin_point[0])**2 + (rotating_dot.get_center()[1] - origin_point[1])**2)

        # Background Circle
        main_circle = Circle(radius=main_circle_radius, color=BLUE, stroke_opacity=0.8 , stroke_width=3).move_to(origin_point)
        imaginary_circle = Circle(radius=main_circle_radius/2, color=GREEN).shift(RIGHT*1.5)
        imaginary_circle_path = Circle(radius=main_circle_radius/2)
        # Creating paths that dots follow
        path_angles = np.arange(0*DEGREES, 180*DEGREES, 22.5*DEGREES)
        paths = VGroup()
        for angle in path_angles:
            paths.add(Line(start=[main_circle_radius,0,0], end=[-main_circle_radius,0,0], stroke_opacity=0.3).rotate_about_origin(angle).move_to(origin_point))
        # By projecting rotating_dot on every path will create S.H.M.
        def SHM_on_path0():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[0])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[0])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot0 = always_redraw(SHM_on_path0)

        def SHM_on_path1():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[1])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[1])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot1 = always_redraw(SHM_on_path1)

        def SHM_on_path2():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[2])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[2])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot2 = always_redraw(SHM_on_path2)

        def SHM_on_path3():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[3])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[3])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot3 = always_redraw(SHM_on_path3)

        def SHM_on_path4():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[4])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[4])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot4 = always_redraw(SHM_on_path4)

        def SHM_on_path5():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[5])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[5])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot5 = always_redraw(SHM_on_path5)

        def SHM_on_path6():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[6])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[6])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot6 = always_redraw(SHM_on_path6)

        def SHM_on_path7():
            unit_vect = Vector(RIGHT).rotate_about_origin(path_angles[7])
            scalar = rotating_dot_vect_length*np.cos(phase.get_value()-path_angles[7])
            hodot_vect = Arrow(start=origin_point, end=origin_point+unit_vect.get_end()*scalar, buff=0)
            return Dot(point=hodot_vect.get_end())
        dot7 = always_redraw(SHM_on_path7)

        dots = [dot0,dot1,dot2,dot3,dot4,dot5,dot6,dot7]
        # Show the projection of rotating_dot on every path
        projection0 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot0.get_center(), color=RED, stroke_opacity=0.5))
        projection1 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot1.get_center(), color=RED, stroke_opacity=0.5))
        projection2 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot2.get_center(), color=RED, stroke_opacity=0.5))
        projection3 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot3.get_center(), color=RED, stroke_opacity=0.5))
        projection4 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot4.get_center(), color=RED, stroke_opacity=0.5))
        projection5 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot5.get_center(), color=RED, stroke_opacity=0.5))
        projection6 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot6.get_center(), color=RED, stroke_opacity=0.5))
        projection7 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot7.get_center(), color=RED, stroke_opacity=0.5))

        projections = VGroup(projection0, projection1, projection2, projection3, projection4, projection5, projection6, projection7)
        
        # Intro text
        intro_text = Text("Tusi Couple simulation")
        sec_text = Text("Who is Tusi? , What is this couple? , Huh?")
        third_text = Text("His name is Nasir al-Din al-Tusi")
        fourth_text= Text("He was a well published author")
        fifth_text = Text("He wrote on subjects of math")
        text_array = [third_text,fourth_text,fifth_text,Text("engineering, prose,..."), Text("And mysticism.")]
        # intro_screen
        self.play(AnimationGroup(Write(intro_text), Create(paths) , lag_ratio= 0.5), run_time=3)
        self.wait()
        self.play(AnimationGroup(intro_text.animate.set_color(GREEN), FadeOut(paths), lag_ratio=0.15), run_time=2)
        self.wait()
        self.play(intro_text.animate.to_edge(UP))
        self.play(intro_text.animate.scale(0.9))
        self.wait()
        self.play(Write(sec_text))
        self.wait(2)
        self.play(AnimationGroup(FadeOut(intro_text), sec_text.animate.scale(0.8),sec_text.animate.to_edge(UP)) , run_time=2)
        rect= Rectangle(color=BLUE, width=14, height=14)
        for index_t in range(len(text_array)):
            if index_t == 0:
                self.play(*[FadeOut(o) for o in self.mobjects])
                self.play(Write(text_array[index_t]))
                self.play(text_array[index_t].animate.set_color(BLUE))
            elif index_t == len(text_array)-1:
                self.play(ReplacementTransform(text_array[index_t-1],text_array[index_t]))
                self.play(text_array[index_t].animate.set_color(YELLOW))
                break
            self.play(Create(rect), run_time=2)
            self.play(ReplacementTransform(text_array[index_t], text_array[index_t+1]))
            self.wait()
        self.play(*[FadeOut(o) for o in self.mobjects])
        
        # Simulation text
        simu_text = Text("Now, let's Jump right in into the simulation!")
        self.play(Write(simu_text) ,run_time =2 )
        self.play(simu_text.animate.scale(1.1))
        self.play(simu_text.animate.set_color(GREEN))
        self.wait()
        # Simulation start
        
        self.play(ReplacementTransform(simu_text, main_circle), run_time=2)
        self.wait()
        self.play(Create(paths[0]), Create(dot0), Create(projection0))
        self.play(phase.animate.increment_value(3*rev), run_time=3*period, rate_func=linear)
        self.play(*[FadeOut(o) for o in self.mobjects if o !=main_circle])
        SHM_text = Text("Simple harmonic motion \nprojected on these paths!", font_size=28).to_corner(UL)
        self.play(Write(SHM_text))
        self.play(Create(paths[4]), Create(dot4), Create(projection4))
        self.play(phase.animate.increment_value(3*rev), run_time=3*period, rate_func=linear)
        self.play(*[FadeOut(o) for o in self.mobjects if o !=main_circle])
        # Scene 2
        more= Text("Let's Add more paths!",font_size=28).to_corner(UL)
        self.play(Create(more))
        for  index in range(len(paths)):
            self.play(FadeIn(paths[index]), FadeIn(dots[index]))
            self.play(phase.animate.increment_value(3*rev), run_time=1*period, rate_func=linear)
        # scene 3
        self.play(FadeOut(more))
        circle_txt= Text("Seems Like a circle , Huh?",font_size=28).to_corner(UL)
        self.play(Write(circle_txt))
        self.play(FadeIn(imaginary_circle))
        self.play(
            MoveAlongPath(imaginary_circle, imaginary_circle_path),
            phase.animate.increment_value(rev),
            run_time=2*period,
            rate_func=linear,
        )
        # scene 4
        tusi_txt= Text("And Here we got Tusi couple!",font_size=28).to_corner(UL)
        self.play(FadeOut(circle_txt))
        self.play(Write(tusi_txt))
        self.play(*[FadeIn(p) for p in projections])
        self.play(FadeIn(rotating_dot))
        self.play(phase.animate.increment_value(rev), MoveAlongPath(imaginary_circle,imaginary_circle_path), run_time=3*period, rate_func=linear)
        self.wait(2)
        self.play(*[FadeOut(o) for o in self.mobjects if o!=main_circle])
        # outro
        dot = Dot(ORIGIN)
        self.play(ReplacementTransform(main_circle,dot))
        created_by = Text("Developed by A. El Sayed")
        linee = Line(LEFT, RIGHT)
        self.play(ReplacementTransform(dot,linee))
        self.wait()
        self.play(ReplacementTransform(linee,created_by))
        self.play(Indicate(created_by))
        self.play(FadeOut(created_by))



