import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from manim import *

# data 
X = np.linspace(-4,4,7)
errors = np.array([-1,1,-2,0,1,-2,2])
y = ((X - 3.5) * X * (X + 3.5) + errors)/40
# y = np.zeros_like(X)

def poly_model(n):
    poly_tr = PolynomialFeatures(degree=n)
    X_tr = poly_tr.fit_transform(X.reshape(-1,1))
    model = LinearRegression()
    model.fit(X_tr, y)
    def poly_func(x):
        x_2darray = np.array(x).reshape(-1,1)
        X_trans = poly_tr.transform(x_2darray)
        return model.predict(X_trans)[0]
    return poly_func

class Overfitting(Scene):
    def construct(self):
        ax = Axes(x_range=[-4.5, 4.5], 
                  y_range=[-20,20.1,5], 
                  x_length=9,
                  y_length=40).add_coordinates()
        dots = VGroup(*[Dot([a, b, 0]) for a, b in zip(X, y)])
        
        graph1 = ax.plot(lambda x: poly_model(1)(x)).set_color(GREEN)
        graph3 = ax.plot(lambda x: poly_model(3)(x)).set_color(RED)
        graph5 = ax.plot(lambda x: poly_model(5)(x)).set_color(PINK)
        graph9 = ax.plot(lambda x: poly_model(9)(x)).set_color(PURPLE)
        graph13 = ax.plot(lambda x: poly_model(13)(x)).set_color(RED)
        graph17 = ax.plot(lambda x: poly_model(17)(x)).set_color(YELLOW)

        self.add(ax)
        self.add(dots)
        self.play(Transform(graph1, graph3, run_time=3))
        self.remove(graph1)
        self.play(Transform(graph3, graph5, run_time=3))
        self.remove(graph3)
        self.play(Transform(graph5, graph9, run_time=3))
        self.remove(graph5)
        self.play(Transform(graph9, graph13, run_time=3))
        self.remove(graph9)
        self.play(Transform(graph13, graph17, run_time=3))
        self.remove(graph13)
        self.wait(1)

