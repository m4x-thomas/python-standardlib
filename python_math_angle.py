
import math
print '{:^7} {:^7} {:^7}'.format('Degrees', 'Radians', 'Expected')
print '{:-^7} {:-^7} {:-^7}'.format('', '', '')
#幅度与角度转换操作 rad = deg * π / 180.
for deg, expected in [ ( 0, 0),
	( 30, math.pi/6),
	( 45, math.pi/4),
	( 60, math.pi/3),
	( 90, math.pi/2),
	(180, math.pi),
	(270, 3/2.0 * math.pi),
	(360,2 * math.pi),
	]:
	print '{:7d} {:7.2f} {:7.2f}'.format(deg,
	math.radians(deg),
	expected,
	)
	
#(sin A = opposite/hypotenuse).
#(cos A = adjacent/hypotenuse
#tan A = opposite/adjacent).
print 'Degrees Radians Sine Cosine Tangent'
print '------- ------- ------- -------- -------'
fmt = ' '.join(['%7.2f'] * 5)
for deg in range(0, 361, 30):
	rad = math.radians(deg)
	if deg in (90, 270):
		t = float('inf')
	else:
		t = math.tan(rad)
	print fmt % (deg, rad, math.sin(rad), math.cos(rad), t)
	
#(x**2 + y**2) ** 1/2,
#使用
print '{:^7} {:^7} {:^10}'.format('X', 'Y', 'Hypotenuse')
print '{:-^7} {:-^7} {:-^10}'.format('', '', '')
for x, y in [ # simple points
	(1, 1),
	(-1, -1),
	(math.sqrt(2), math.sqrt(2)),
	(3, 4), # 3-4-5 triangle
	# on the circle
	(math.sqrt(2)/2, math.sqrt(2)/2), # pi/4 rads
	(0.5, math.sqrt(3)/2), # pi/3 rads
	]:
	h = math.hypot(x, y)
	print '{:7.2f} {:7.2f} {:7.2f}'.format(x, y, h)
	
for r in [ 0, 0.5, 1 ]:
	print 'arcsine(%.1f) = %5.2f' % (r, math.asin(r))
	print 'arccosine(%.1f) = %5.2f' % (r, math.acos(r))
	print 'arctangent(%.1f) = %5.2f' % (r, math.atan(r))
print
#双曲线方法
print '{:^6} {:^6} {:^6} {:^6}'.format(
'X', 'sinh', 'cosh', 'tanh',
)
print '{:-^6} {:-^6} {:-^6} {:-^6}'.format('', '', '', '')
fmt = ' '.join(['{:6.4f}'] * 4)
for i in range(0, 11, 2):
	x = i/10.0
	print fmt.format(x, math.sinh(x), math.cosh(x), math.tanh(x))
	
#特殊方法
#高斯误差函数erf(-x) == -erf(x).
print '{:^5} {:7}'.format('x', 'erf(x)')
print '{:-^5} {:-^7}'.format('', '')
for x in [ -3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3 ]:
	print '{:5.2f} {:7.4f}'.format(x, math.erf(x))
#使用erfc方法，避免很小的数的精度误差
print '{:^5} {:7}'.format('x', 'erfc(x)')
print '{:-^5} {:-^7}'.format('', '')
for x in [ -3, -2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2, 3 ]:
	print '{:5.2f} {:7.4f}'.format(x, math.erfc(x))
	
"""
See Also:
math (http://docs.python.org/library/math.html) The standard library documentation
for this module.
IEEE floating-point arithmetic in Python
(http://www.johndcook.com/blog/2009/07/21/ieee-arithmetic-python/) Blog
post by John Cook about how special values arise and are dealt with when doing
math in Python.
SciPy (http://scipy.org/) Open source libraries for scientific and mathematical calculations
in Python.
"""
