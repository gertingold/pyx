#!/usr/bin/env python
import sys; sys.path[:0] = ["../.."]
from pyx import *

#####  helpers  ##############################################################

def bboxrect(cmd):
   bbox=cmd.bbox()
   return path.rect("%f t pt" % bbox.llx,            "%f t pt" % bbox.lly,
               "%f t pt" % (bbox.urx-bbox.llx), "%f t pt" % (bbox.ury-bbox.lly))

def dotest(c, x, y, test):
   c2 = c.insert(canvas.canvas(trafo.translate(x, y)))
   eval("%s(c2)" % test)
   c.stroke(bboxrect(c2))

def drawpathwbbox(c, p):
    c.stroke(p, [color.rgb.red])
    np=normpath(p)
    c.stroke(np, [color.rgb.green, style.linestyle.dashed])
    c.stroke(bboxrect(p))

#####  tests  ################################################################

def testwriggle(c):
    p = path.line(0, 0, 3, 0)
    c.stroke(p, [color.rgb.red])
    c.stroke(p, [color.rgb.green, deco.wriggle()])

    p = path.curve(5, 0, 8, 0, 6, 4, 9, 4)
    c.stroke(p, [color.rgb.red])
    c.stroke(p, [color.rgb.green, deco.wriggle(), deco.earrow.LARge([deco.stroked.clear])])
    c.stroke(p, [color.rgb.blue, deco.wriggle(), deco.wriggle(loops=250, radius=0.1)])


def testcurvecorners(c):
    p = path.path(path.moveto(0,0), path.lineto(3,0), path.lineto(5,7),
    path.curveto(0,10, -2,8, 0,6),
    path.lineto(0,4), path.lineto(-5,4), path.lineto(-5,2), path.lineto(-0.2,0.2),
    path.closepath())

    c.stroke(path.normpath(p), [color.gray(0.8), style.linewidth.THIck])
    c.stroke(p, [color.rgb.blue, deco.curvecorners(radius=1, softness=0.1)])
    c.stroke(p, [color.rgb.red, deco.curvecorners(radius=1, softness=1)])
    c.stroke(path.circle(0,0,2), [deco.curvecorners(radius=6)])

c=canvas.canvas()
dotest(c, 0, 0, "testwriggle")
dotest(c, 15, 0, "testcurvecorners")
c.writeEPSfile("test_deco", paperformat="a4", rotated=0, fittosize=1)

