from math import sqrt, sin, cos, tan, acos, degrees, radians


def circumference_area(edge_a, edge_b, edge_c):
    half_circumference = (edge_a + edge_b + edge_c) / 2
    return half_circumference * 2, sqrt(half_circumference * (
            half_circumference - edge_a
        ) * (
            half_circumference - edge_b
        ) * (
            half_circumference - edge_c
        )
    )


def sss(edge_a, edge_b, edge_c):
    if edge_a + edge_b <= edge_c or \
       edge_a + edge_c <= edge_b or \
       edge_b + edge_c <= edge_a:
        raise ValueError
    circumference, area = circumference_area(edge_a, edge_b, edge_c)
    cos_a = (edge_b ** 2 + edge_c ** 2 - edge_a ** 2) / (2 * edge_b * edge_c)
    cos_b = (edge_a ** 2 + edge_c ** 2 - edge_b ** 2) / (2 * edge_a * edge_c)
    cos_c = (edge_a ** 2 + edge_b ** 2 - edge_c ** 2) / (2 * edge_a * edge_b)
    rad_a = acos(cos_a)
    rad_b = acos(cos_b)
    rad_c = acos(cos_c)
    sin_a = sin(rad_a)
    return f"""∠A = {degrees(rad_a)}°.
∠B = {degrees(rad_b)}°.
∠C = {degrees(rad_c)}°.
S = {area}.
C = {circumference}.
rI = {2 * area / circumference}.
rO = {edge_a / sin_a / 2}.
sinA = {sin_a}.
sinB = {sin(rad_b)}.
sinC = {sin(rad_c)}.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = {cos_c}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}."""


def sas(edge_a, angle_c, edge_b):
    if angle_c >= 180:  # The angle of a triangle is never bigger than 180°.
        raise ValueError
    rad_c = radians(angle_c)
    cos_c = cos(rad_c)
    edge_c = sqrt(edge_a ** 2 + edge_b ** 2 - 2 * edge_a * edge_b * cos(rad_c))
    cos_a = (edge_b ** 2 + edge_c ** 2 - edge_a ** 2) / (2 * edge_b * edge_c)
    cos_b = (edge_a ** 2 + edge_c ** 2 - edge_b ** 2) / (2 * edge_a * edge_c)
    rad_a = acos(cos_a)
    rad_b = acos(cos_b)
    sin_c = sin(rad_c)
    return f"""c = {edge_c}.
∠A = {degrees(rad_a)}°.
∠B = {degrees(rad_b)}°.
S = {edge_a * edge_b * sin_c / 2}.
C = {edge_a + edge_b + edge_c}.
rI = {2 * area / circumference}.
rO = {edge_a / sin_a / 2}.
sinA = {sin(rad_a)}.
sinB = {sin(rad_b)}.
sinC = {sin_c}.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = {cos_c}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}."""


def aas(angle_a, angle_b, edge_a):
    if angle_a + angle_b >= 180:
        raise ValueError
    rad_a = radians(angle_a)
    rad_b = radians(angle_b)
    angle_c = 180 - angle_a - angle_b
    sin_a = sin(rad_a)
    d = edge_a / sin_a
    rad_c = radians(angle_c)
    sin_b = sin(rad_b)
    sin_c = sin(rad_c)
    edge_b = sin_b * d
    edge_c = sin_c * d
    circumference, area = circumference_area(edge_a, edge_b, edge_c)
    return f"""b = {edge_b}.
c = {edge_c}.
∠C = {angle_c}°.
S = {area}.
C = {circumference}.
rI = {2 * area / circumference}.
rO = {d / 2}.
sinA = {sin_a}.
sinB = {sin_b}.
sinC = {sin_c}.
cosA = {cos(rad_a)}.
cosB = {cos(rad_b)}.
cosC = {cos(rad_c)}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}."""


def asa(angle_b, edge_a, angle_c):
    if angle_b + angle_c >= 180:
        raise ValueError
    angle_a = 180 - angle_b - angle_c
    rad_a = radians(angle_a)
    rad_b = radians(angle_b)
    angle_c = 180 - angle_a - angle_b
    sin_a = sin(rad_a)
    d = edge_a / sin_a
    rad_c = radians(angle_c)
    sin_b = sin(rad_b)
    sin_c = sin(rad_c)
    edge_b = sin_b * d
    edge_c = sin_c * d
    circumference, area = circumference_area(edge_a, edge_b, edge_c)
    return f"""b = {edge_b}.
c = {edge_c}.
∠A = {angle_a}°.
S = {area}.
C = {circumference}.
rI = {2 * area / circumference}.
rO = {d / 2}.
sinA = {sin_a}.
sinB = {sin_b}.
sinC = {sin_c}.
cosA = {cos(rad_a)}.
cosB = {cos(rad_b)}.
cosC = {cos(rad_c)}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}."""


def hl(edge_a, edge_c):
    edge_b = sqrt(edge_c**2 - edge_a**2)
    if edge_a + edge_b <= edge_c:
        raise ValueError
    area = edge_a * edge_b / 2
    circumference = edge_a + edge_b + edge_c
    sin_a = edge_a / edge_c
    sin_b = edge_b / edge_c
    cos_a = sin_b
    cos_b = sin_a
    angle_b = degrees(acos(cos_b))
    return f"""b = {edge_b}.
∠A = {90 - angle_b}°.
∠B = {angle_b}°.
S = {area}.
C = {circumference}.
rI = {edge_a + edge_b - edge_c / 2}.
rO = {edge_c / 2}.
sinA = {sin_a}.
sinB = {sin_b}.
sinC = 1.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = 0.
tanA = {edge_a / edge_b}.
tanB = {edge_b / edge_a}.
tanC = +∞."""
