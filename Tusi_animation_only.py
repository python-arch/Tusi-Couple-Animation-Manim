from manim import *


class Tusi_animation(Scene):
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
        projection0 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot0.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection1 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot1.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection2 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot2.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection3 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot3.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection4 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot4.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection5 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot5.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection6 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot6.get_center(), color=ORANGE, stroke_opacity=0.5))
        projection7 = always_redraw(lambda: DashedLine(start=rotating_dot.get_center(), end=dot7.get_center(), color=ORANGE, stroke_opacity=0.5))

        projections = VGroup(projection0, projection1, projection2, projection3, projection4, projection5, projection6, projection7)
        
                # Simulation start
        self.play(Create(main_circle))
        self.play(Create(paths[0]), Create(dot0), Create(projection0))
        self.play(phase.animate.increment_value(3*rev), run_time=3*period, rate_func=linear)
        self.play(*[FadeOut(o) for o in self.mobjects if o !=main_circle])
        self.play(Create(paths[4]), Create(dot4), Create(projection4))
        self.play(phase.animate.increment_value(3*rev), run_time=3*period, rate_func=linear)
        self.play(*[FadeOut(o) for o in self.mobjects if o !=main_circle])
        # Scene 2
        for  index in range(len(paths)):
            self.play(FadeIn(paths[index]), FadeIn(dots[index]))
            self.play(phase.animate.increment_value(3*rev), run_time=1*period, rate_func=linear)
        # scene 3
        self.play(FadeIn(imaginary_circle))
        self.play(
            MoveAlongPath(imaginary_circle, imaginary_circle_path),
            phase.animate.increment_value(rev),
            run_time=2*period,
            rate_func=linear,
        )
        # scene 4
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
        return super().construct()