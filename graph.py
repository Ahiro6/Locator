import pandas as pd
import xlrd
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row, column
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import curdoc
import datetime


class LocGraph:
    def __init__(self, name, graph_name):
    
        self.f = figure(width=1500, height=600, x_axis_type="datetime", y_axis_type="datetime")

        self.f.title.text=f"{}"
        self.f.title.text_color="Black"
        self.f.title.text_font="times"
        self.f.title.text_font_style="bold"
        self.f.xaxis.minor_tick_line_color=None
        self.f.yaxis.minor_tick_line_color=None
        self.f.xaxis.axis_label="Time (Seconds)"

        hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string"), ("Duration", "@Times_string")])
        self.f.add_tools(hover)

    def graph_quad(self):
        self.f.yaxis[0].ticker.desired_num_ticks = 1
        self.f.quad(left="", right="", top=1, bottom=0, color="blue", alpha=0.5)

    def graph_line(self):
        self.f.line(x="", y="", color="blue", alpha=0.5)

    def graph_triangle(self):
        self.f.triangle(x="", y="", color="blue", alpha=0.5)

    def graph_circle(self):
        self.f.circle(x="", y="", color="blue", alpha=0.5)

    def graph_vbar(self):
        self.f.vbar(x="", top="", width=4, bottom=0, color="blue", alpha=0.5)


output_file(f"{graph_name}.html")

move = TimeGraph("Times_movement.csv", "Motion Graph")


move.graph_line()


show(column(move.f))
