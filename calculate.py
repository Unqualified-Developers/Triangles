from math import pi, sqrt, sin, cos, tan, acos


def p_sss(edge_a, edge_b, edge_c):
    if edge_a + edge_b <= edge_c or edge_a + edge_c <= edge_b or edge_b + edge_c <= edge_a:
        raise ValueError
    half_circumference = (edge_a + edge_b + edge_c) / 2
    area = sqrt(half_circumference * (
            half_circumference - edge_a
        ) * (
            half_circumference - edge_b
        ) * (
            half_circumference - edge_c
        )
    )
    circumference = 2 * half_circumference
    cos_a = (edge_b ** 2 + edge_c ** 2 - edge_a ** 2) / (2 * edge_b * edge_c)
    cos_b = (edge_a ** 2 + edge_c ** 2 - edge_b ** 2) / (2 * edge_a * edge_c)
    cos_c = (edge_a ** 2 + edge_b ** 2 - edge_c ** 2) / (2 * edge_a * edge_b)
    rad_a = acos(cos_a)
    rad_b = acos(cos_b)
    rad_c = acos(cos_c)
    return f"""S = {area}.
C = {circumference}.
rI = {2 * area / circumference}.
∠A = {rad_a / pi * 180}°.
∠B = {rad_b / pi * 180}°.
∠C = {rad_c / pi * 180}°.
sinA = {sin(rad_a)}.
sinB = {sin(rad_b)}.
sinC = {sin(rad_c)}.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = {cos_c}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}."""


def p_sas(edge_a, angle_c, edge_b):
    if angle_c >= 180:  # The angle of a triangle is never bigger than 180°.
        raise ValueError
    rad_c = angle_c * pi / 180
    cos_c = cos(rad_c)
    edge_c = sqrt(edge_a ** 2 + edge_b ** 2 - 2 * edge_a * edge_b * cos(rad_c))
    cos_a = (edge_b ** 2 + edge_c ** 2 - edge_a ** 2) / (2 * edge_b * edge_c)
    cos_b = (edge_a ** 2 + edge_c ** 2 - edge_b ** 2) / (2 * edge_a * edge_c)
    rad_a = acos(cos_a)
    rad_b = acos(cos_b)
    half_circumference = (edge_a + edge_b + edge_c) / 2
    area = sqrt(half_circumference * (
            half_circumference - edge_a
        ) * (
            half_circumference - edge_b
        ) * (
            half_circumference - edge_c
        )
    )
    circumference = 2 * half_circumference
    return f"""S = {area}.
C = {circumference}.
rI = {2 * area / circumference}.
c = {edge_c}.
∠A = {rad_a / pi * 180}°.
∠B = {rad_b / pi * 180}°.
sinA = {sin(rad_a)}.
sinB = {sin(rad_b)}.
sinC = {sin(rad_c)}.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = {cos_c}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}."""
