#!/usr/bin/env python

import sys, signal
import math
import os
import argparse

sys.path.append("/usr/lib/freecad/lib")
import FreeCAD, Part

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed

class CADAnalyzer():
    def __init__(self, _debug_print=False):
        self.shape = Part.Shape()
        self.debug_print = _debug_print
        self.epsilon = 1e-04

    def error(self):
        print("[Error] Error has occurred.")
        sys.exit(0)

    def is_epsilon(self, val):
        if abs(val) < self.epsilon:
            return True
        else:
            return False

    def sgn(self, val):
        return val / abs(val)

    def read_file(self, file_name):
        self.shape.read(file_name)
        print("[Info] reading STEP file of {}".format(file_name))
        if self.debug_print:
            print("[Debug] num of edges : {}.".format(len(self.shape.Edges)))
            print("[Debug] num of Wires : {}".format(len(self.shape.Wires)))
            print("[Debug] num of Vertexes : {}".format(len(self.shape.Vertexes)))
            print("[Debug] num of Shells : {}".format(len(self.shape.Shells)))

    def is_circular_edge(self, edge):
        try:
            edge.Curve.Center
            return True
        except:
            return False

    def plot_vertex(self, shell_indexes=None, vertex_indexes=None, with_all=False):
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        # vertexes of all
        if with_all:
            x_all = []
            y_all = []
            z_all = []
            for vertex in self.shape.Vertexes:
                x_all.append(vertex.Point[0])
                y_all.append(vertex.Point[1])
                z_all.append(vertex.Point[2])

            ax.scatter(x_all, y_all, z_all, color="#0000ff")

        # vertexes of indexes
        x = []
        y = []
        z = []
        for shell_index in range(len(self.shape.Shells)):
            if shell_indexes != None and shell_index not in shell_indexes:
                continue
            for vertex_index in range(len(self.shape.Shells[shell_index].Vertexes)):
                if vertex_indexes != None and vertex_index not in vertex_indexes[shell_indexes.index(shell_index)]:
                    continue
                vertex = self.shape.Shells[shell_index].Vertexes[vertex_index]
                x.append(vertex.Point[0])
                y.append(vertex.Point[1])
                z.append(vertex.Point[2])
        ax.scatter(x, y, z, color="#ff0000")

        plt.show()

    def plot_edge(self, shell_indexes=None, edge_indexes=None, with_all=False):
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        # edge of all
        if with_all:
            x_all = []
            y_all = []
            z_all = []
            for edge in self.shape.Edges:
                if self.is_circular_edge(edge):
                    xs = []
                    ys = []
                    zs = []
                    for i in range(21):
                        p = edge.valueAt(edge.FirstParameter + (edge.LastParameter - edge.FirstParameter) * i * 1.0 / 20.0)
                        xs.append(p[0])
                        ys.append(p[1])
                        zs.append(p[2])
                    ax.plot(xs, ys, zs, color="#0000ff")
                else:
                    p0 = edge.Vertexes[0].Point
                    p1 = edge.Vertexes[1].Point
                    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], [p0[2], p1[2]], color="#0000ff")

        # edge of indexes
        for shell_index in range(len(self.shape.Shells)):
            if shell_indexes != None and shell_index not in shell_indexes:
                continue
            for edge_index in range(len(self.shape.Shells[shell_index].Edges)):
                if edge_indexes != None and edge_index not in edge_indexes[shell_indexes.index(shell_index)]:
                    continue
                edge = self.shape.Shells[shell_index].Edges[edge_index]
                if self.is_circular_edge(edge):
                    xs = []
                    ys = []
                    zs = []
                    for i in range(21):
                        p = edge.valueAt(edge.FirstParameter + (edge.LastParameter - edge.FirstParameter) * i * 1.0 / 20.0)
                        xs.append(p[0])
                        ys.append(p[1])
                        zs.append(p[2])
                    ax.plot(xs, ys, zs, color="#ff0000")
                else:
                    p0 = edge.Vertexes[0].Point
                    p1 = edge.Vertexes[1].Point
                    ax.plot([p0[0], p1[0]], [p0[1], p1[1]], [p0[2], p1[2]], color="#ff0000")
        plt.show()

def main(model_path, ipython, debug_print):
    # set sigint handler
    signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))

    # init cad_analyzer and read CAD model
    ca = CADAnalyzer(debug_print)
    ca.read_file(model_path)

    # execute ipython
    if ipython:
        embed()

if __name__ == "__main__":
    # parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model-path")
    parser.add_argument("-i", "--ipython", action='store_true')
    parser.add_argument("-d", "--debug-print", action='store_true')
    args = parser.parse_args()

    # execute main function
    main(model_path=os.getcwd()+"/"+args.model_path, ipython=args.ipython, debug_print=args.debug_print)
