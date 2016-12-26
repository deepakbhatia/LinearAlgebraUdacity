import operator
import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
    def scalar(self,c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    def is_orthogonal(self,v,tolerance=1e-10):
        return math.abs(self.dot(v)) < tolerance
    def is_parallel(self,v):
        return(self.is_zero_vector() or
            v.is_zero_vector() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi)
    def is_zero_vector(self,tolerance=1e-10):
        return self.magnitude() < tolerance;

    def component_parallel_to(self,basis):
        try:
            u = basis.normalized()#Unit vector
            weight = self.dot_product(u)#magnitude of self parallel 
            return u.scalar(weight)
        except Exception as e:    
            raise e
    def component_orthogonal(self,basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            raise e
    def cross(self,v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                                -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2*y_1]
            return Vector(new_coordinates)
        except ValueError as e:
            raise e
    def area_parallel(self,v):
        try:
            new_coordinates = self.cross(v)
            return magnitude(new_coordinates)
        except ValueError as e:
            raise e
    def area_triangle(self,v):
        try:
            return 0.5*self.area_parallel(v)
        except Exception as e:
            raise e
    def dot_product(self,v):
        sum_coords=0;
        sum_coords  = sum(x*y for x,y in zip(self.coordinates,v.coordinates))
        return sum_coords
    def angle_with(self,v,in_degrees):
        try:
            a1 = self.normalize()
            a2 =  v.normalize()
            angle_in_radians = math.acos(a1.dot(a2))
            if in_degrees:
                degrees_per_radian = 180./pi 
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians
        except Exception as e:
            raise e

    def add(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]

        return Vector(new_coordinates)
    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    
my_vector = Vector([8.218,-9.341])
ur_vector = Vector([-1.129,2.111])
v = Vector([1.996, 3.108, -4.554])
#print add(my_vector,ur_vector)
#print minus(my_vector,ur_vector)
#print scalar(my_vector,4)
#print magnitude(my_vector)
v = Vector([-9.88,-3.264,-8.159])
w = Vector([-2.155,-9.353,-9.473])
#print v.dot_product(w)
print v.component_orthogonal(w)

