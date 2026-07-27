from build123d import *
from math import cos, sin, pi

def gen_step():
    od = 80.0
    thickness = 10.0
    bore_d = 30.0
    bolt_hole_d = 6.0
    bcd = 60.0
    num_holes = 6
    fillet_r = 1.5

    with BuildPart() as p:
        Cylinder(radius=od / 2, height=thickness, align=(Align.CENTER, Align.CENTER, Align.MIN))

        Cylinder(radius=bore_d / 2, height=thickness,
                 align=(Align.CENTER, Align.CENTER, Align.MIN),
                 mode=Mode.SUBTRACT)

        for i in range(num_holes):
            angle = 2 * pi * i / num_holes
            x = (bcd / 2) * cos(angle)
            y = (bcd / 2) * sin(angle)
            with Locations((x, y, thickness / 2)):
                Cylinder(radius=bolt_hole_d / 2, height=thickness,
                         align=Align.CENTER, mode=Mode.SUBTRACT)

        outer_rim_edges = [
            e for e in p.edges().filter_by(GeomType.CIRCLE)
            if abs(e.radius - od / 2) < 0.01
        ]
        fillet(outer_rim_edges, radius=fillet_r)

    return p.part
