"""
MIT License
Copyright (c) 2017 Cyrille Rossant
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import numpy as np
import matplotlib.pyplot as plt

def normalize(x):
    x /= np.linalg.norm(x)
    return x


def intersect_triangle(O, D, T):

    v0, v1, v2 = map(np.array, T)
    v0v1 = v1 - v0
    v0v2 = v2 - v0
    pvec = np.cross(D, v0v2)
    det = v0v1.T.dot(pvec)

    if det < 0.000001:
        return np.inf

    invDet = 1.0 / det
    tvec = O - v0
    u = tvec.dot(pvec) * invDet

    if u < 0 or u > 1:
        return np.inf

    qvec = np.cross(tvec, v0v1)
    v = D.dot(qvec) * invDet

    if v < 0 or u + v > 1:
        return np.inf

    d = v0v2.dot(qvec) * invDet

    return d


def intersect_plane(O, D, P, N):
    # Return the distance from O to the intersection of the ray (O, D) with the
    # plane (P, N), or +inf if there is no intersection.
    # O and P are 3D points, D and N (normal) are normalized vectors.
    denom = np.dot(D, N)
    if np.abs(denom) < 1e-6:
        return np.inf
    d = np.dot(P - O, N) / denom
    if d < 0:
        return np.inf
    return d


def intersect_sphere(O, D, S, R):
    # Return the distance from O to the intersection of the ray (O, D) with the
    # sphere (S, R), or +inf if there is no intersection.
    # O and S are 3D points, D (direction) is a normalized vector, R is a scalar.
    a = np.dot(D, D)
    OS = O - S
    b = 2 * np.dot(D, OS)
    c = np.dot(OS, OS) - R * R
    disc = b * b - 4 * a * c
    if disc > 0:
        distSqrt = np.sqrt(disc)
        q = (-b - distSqrt) / 2.0 if b < 0 else (-b + distSqrt) / 2.0
        t0 = q / a
        t1 = c / q
        t0, t1 = min(t0, t1), max(t0, t1)
        if t1 >= 0:
            return t1 if t0 < 0 else t0
    return np.inf


def intersect(O, D, obj):
    if obj['type'] == 'triangle':
        return intersect_triangle(O, D, obj['position'])
    elif obj['type'] == 'sphere':
        return intersect_sphere(O, D, obj['position'], obj['radius'])
    elif obj['type'] == 'plane':
        return intersect_plane(O, D, obj['position'], obj['normal'])


def get_normal(obj, M):
    # Find normal.
    if obj['type'] == 'sphere':
        N = normalize(M - obj['position'])
    elif obj['type'] == 'plane':
        N = obj['normal']
    elif obj['type'] == 'triangle':
        v0, v1, v2 = map(np.array, obj['position'])
        u = v1 - v0
        v = v2 - v0
        N = np.cross(u, v)
    return N


def get_color(obj, M):
    color = obj['color']
    if not hasattr(color, '__len__'):
        color = color(M)
    return color


def trace_ray(rayO, rayD):
    # Find first point of intersection with the scene.
    t = np.inf
    for i, obj in enumerate(scene):
        t_obj = intersect(rayO, rayD, obj)
        if t_obj < t:
            t, obj_idx = t_obj, i
    # Return None if the ray does not intersect any object.
    if t == np.inf:
        return
    # Find the object.
    obj = scene[obj_idx]
    # Find the point of intersection on the object.
    M = rayO + rayD * t
    # Find properties of the object.
    N = get_normal(obj, M)
    color = get_color(obj, M)
    for L in lights:
        # Start computing the color.
        col_ray = ambient
        toL = normalize(L - M)
        toO = normalize(O - M)
        # Shadow: find if the point is shadowed or not.
        l = [intersect(M + N * .0001, toL, obj_sh)
             for k, obj_sh in enumerate(scene) if k != obj_idx]
        if l and min(l) < np.inf:
            return
        # Lambert shading (diffuse).
        col_ray += obj.get('diffuse_c', diffuse_c) * max(np.dot(N, toL), 0) * color
        # Blinn-Phong shading (specular).
        col_ray += obj.get('specular_c', specular_c) * \
                max(np.dot(N, normalize(toL + toO)), 0) ** specular_k * color_light

    return obj, M, N, col_ray

def add_triangle(v0, v1, v2, color):
    return dict(type='triangle',
                position=(v0, v1, v2),
                color=np.array(color), reflection=.3)

def add_sphere(position, radius, color):
    return dict(type='sphere', position=np.array(position),
                radius=np.array(radius), color=np.array(color), reflection=.5)


def add_plane(position, normal):
    return dict(type='plane', position=np.array(position),
                normal=np.array(normal),
                color=color_plane0,
                diffuse_c=.75, specular_c=.5, reflection=.5)

def add_floor(position, normal):
    return dict(type='plane', position=np.array(position),
                normal=np.array(normal),
                color=lambda M: (color_plane0
                                 if (int(M[0] * 2) % 2) == (int(M[2] * 2) % 2) else color_plane1),
                diffuse_c=.75, specular_c=.5, reflection=.1)

w = 256
h = 256


# List of objects.
color_plane0 = 1. * np.ones(3)
color_plane1 = 0. * np.ones(3)
scene = [
    add_plane([0., 0., 5.], [0., 0., -1.]),
    add_floor([0., -.5, 0.], [0., 1., 0.]),
    add_triangle([-2, 1, 2], [-2, 2, 2], [-1, 1, 2], [1., 0., 0.2]),
    add_sphere([-.5, .1, 2], .8, [.9, 0.5, .1]),
    add_sphere([0.3, .1, 0.3], .3, [0.2, 1., .35]),
    add_sphere([1.75, .1, 3], .8, [0.2, .0, 1.]),
]

# Light position and color.
L1 = np.array([5., 5., -2])
L2 = np.array([-5., 5., -2])

lights = [L1]

color_light = np.ones(3)  / len(lights)

# Default light and material parameters.
ambient = .05
diffuse_c = 1.
specular_c = 1.
specular_k = 50

depth_max = 10  # Maximum number of light reflections.
col = np.zeros(3)  # Current color.
O = np.array([0., 0.35, -1.])  # Camera.
Q = np.array([0., 0., 0.])  # Camera pointing to.
img = np.zeros((h, w, 3))

r = float(w) / h
# Screen coordinates: x0, y0, x1, y1.
S = (-1., -1. / r + .25, 1., 1. / r + .25)

# Loop through all pixels.
for i, x in enumerate(np.linspace(S[0], S[2], w)):
    if i % 10 == 0:
        print(i / float(w) * 100, "%")
    for j, y in enumerate(np.linspace(S[1], S[3], h)):
        col[:] = 0
        Q[:2] = (x, y)
        D = normalize(Q - O)
        depth = 0
        rayO, rayD = O, D
        reflection = 1.
        # Loop through initial and secondary rays.
        while depth < depth_max:
            traced = trace_ray(rayO, rayD)
            if not traced:
                break
            obj, M, N, col_ray = traced
            # Reflection: create a new ray.
            rayO, rayD = M + \
                N * .0001, normalize(rayD - 2 * np.dot(rayD, N) * N)
            depth += 1
            col += reflection * col_ray
            reflection *= obj.get('reflection', 1.)
        img[h - j - 1, i, :] = np.clip(col, 0, 1)

plt.imsave('fig.png', img)
