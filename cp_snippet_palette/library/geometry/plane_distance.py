"""3次元の点と平面の距離。出典: yuki_0132.py。PyPy/Codonのfloat向け。
3点が共線ならValueError。丸め誤差と中間積の範囲は入力に応じて評価する。
"""

from math import sqrt


def point_plane_distance(point, a, b, c):
    ux, uy, uz = b[0] - a[0], b[1] - a[1], b[2] - a[2]
    vx, vy, vz = c[0] - a[0], c[1] - a[1], c[2] - a[2]
    nx, ny, nz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
    norm = sqrt(nx * nx + ny * ny + nz * nz)
    if norm == 0:
        raise ValueError("three points do not define a plane")
    return (
        abs(nx * (point[0] - a[0]) + ny * (point[1] - a[1]) + nz * (point[2] - a[2]))
        / norm
    )
