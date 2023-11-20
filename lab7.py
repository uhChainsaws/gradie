from manim import *
import math

from numpy import ndarray
z_stretch = 0.3

def v2_to_v3(p, z):
    return np.array([p[0], p[1], z])

def f(p):
    x = p[0]
    y = p[1]
    return (x**3) * (y**2) * (4. - x - y)

def f_prime(p):
    x = p[0]
    y = p[1]
    v = np.array([-(x**2) * (y**2) * (4*x + 3*(y-4)), (x**3)* y * (-2*x-3*y+8)])
    return v/np.linalg.norm(v)

def a(n):
    # return 1
    # return 0.01
    return 1./(n+100)
    # return 1./math.log(n+100)

def can_we_stop_please(point: ndarray, k, a_k = 0, epsilon = 0, delta = 0):
    # infinity check
    if np.linalg.norm(point, ord=1) > 2000:
        return True
    # k stop
    if k>=1336:
        return True
    
    # a_k stop
    # if a<0.001:
    #     return True

    # epsilon stop
    if epsilon<0.0001:
        return True
    
    # delta stop
    # if delta<0.005:
    #     return True
    
    return False

    

class LAB7(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=135 * DEGREES)

        def param_f(x, y):
            z = f(np.array([x,y]))
            return np.array([x, y, z])

        planne = Surface(
            param_f,
            resolution=50,
            v_range=[-5., 5.],
            u_range=[-5., 5.]
        )
        planne.set_style(fill_opacity=0.5,stroke_color=GREEN)
        planne.set_fill_by_checkerboard(0xffa800, 0xffa800, opacity=0.9)
        planne.stretch_about_point(z_stretch, 2, ORIGIN)

        (x_0, y_0) = (0.4, 0.4)
        p_0 = np.array([x_0, y_0])
        
        k = 0
        points = [p_0]

        while True:
            a_k = a(k)
            p_pre = points[k]
            p = p_pre + a_k * f_prime(p_pre)
            epsilon = abs(f(p) - f(p_pre))
            delta = np.linalg.norm((p - p_pre))
            points.append(p)
            k += 1

            if can_we_stop_please(p, k, a_k, epsilon, delta):
                break
        print(len(points))

        # self.begin_ambient_camera_rotation(rate=0.1)
        self.add(planne)
        manim_point = Dot3D(point=v2_to_v3(points[0], f(points[0])*z_stretch), color=BLACK) 
        path_tracce = TracedPath(manim_point.get_center, dissipating_time=1, stroke_opacity=[1, 0], stroke_color=BLACK)
        self.add(manim_point, path_tracce)

        points_3d = []
        for i in range(len(points)): 
            p = v2_to_v3(points[i], f(points[i])*z_stretch)
            points_3d.append(p)
        print(points[-1], f(points[-1]))
        print(2, 4./3., f(np.array([2,4./3.])))

        path = VMobject()
        path.set_points_smoothly(points_3d)

        # self.play(MoveAlongPath(manim_point, path).set_run_time(4), rate_func=smooth)
        # self.wait(2)
        # self.stop_ambient_camera_rotation()