from vector import Vector

vec = Vector((1, 3))
vec2 = Vector([1.0, 2.0, 3.0])
vec3 = 3 * vec
vec4 = vec + vec2 + vec3
vec5 = vec2 / 3
print(vec)
print(vec2)
print(vec3)
print(vec4)
print(vec5)
print(repr(vec))
