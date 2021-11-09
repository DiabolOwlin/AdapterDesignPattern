from abc import abstractmethod
import math


class IVector:
    @abstractmethod
    def abs(self):
        pass

    @abstractmethod
    def cdot(self, vector):
        pass

    @abstractmethod
    def getComponents(self):
        pass

    @abstractmethod
    def getAngle(self):
        pass


class Vector2D(IVector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def abs(self):
        return round(math.sqrt(pow(self.x, 2) + pow(self.y, 2)), 2)

    def getComponents(self):
        return [self.x, self.y]

    def getAngle(self):
        x_axis = Vector2D(self.x, 0)
        abs_x_axis = x_axis.abs()

        cos = (self.x * x_axis.x + self.y * x_axis.y) / self.abs() * abs_x_axis
        angle = math.degrees(math.acos(cos))
        return round(angle, 2)

    def cdot(self, vector):
        dot_product = self.x * vector.x + self.y * vector.y
        return dot_product

    def from_polar_to_cartesian(self):
        x = self.abs() * math.cos(self.getAngle())
        y = self.abs() * math.sin(self.getAngle())
        return [x, y]


class Vector3D(IVector):
    def __init__(self, x, y, z):
        self.vector = Vector2D(x, y)
        self.z = z

    def abs(self):
        x, y = self.vector.getComponents()
        return round(math.sqrt(pow(x, 2) + pow(y, 2) + pow(self.z, 2)), 2)

    def getComponents(self):
        x, y = self.vector.getComponents()
        return [x, y, self.z]

    def getAngle(self):
        x, y = self.vector.getComponents()
        fi = math.atan(y / x)
        psi = math.atan(math.sqrt(pow(x, 2) + pow(y, 2)) / self.z)

        angle = [round(fi, 2), round(psi, 2)]
        return angle

    def cdot(self, vector):
        x, y = self.vector.getComponents()
        x_v, y_v, z_v = vector.getComponents()
        dot_multiplication = x * x_v + y * y_v + self.z * z_v
        return round(dot_multiplication, 2)


class Decorator(Vector3D):
    def cross_multiplication(self, vector):
        x, y, z = self.getComponents()
        x_2, y_2, z_2 = vector.getComponents()
        x_v = y * z_2 - (z * y_2)
        y_v = z * x_2 - (x * z_2)
        z_v = x * y_2 - (y * x_2)
        new_vector = Vector3D(x_v, y_v, z_v)
        return new_vector


class VectorAdapter2D:
    @abstractmethod
    def from_polar_to_cartesian(self):
        pass


class Adapter2D(VectorAdapter2D):
    def __init__(self, r, angle):
        self.r = r
        self.angle = angle

    def from_polar_to_cartesian(self):
        x = self.r * math.cos(math.radians(self.angle))
        y = self.r * math.sin(math.radians(self.angle))
        vector = Vector2D(round(x, 2), round(y, 2))
        return vector


class VectorAdapter3D:
    @abstractmethod
    def spherical_coordinate_to_polar(self):
        pass


class Adapter3D(VectorAdapter3D):
    def __init__(self, r, psi, fi):
        self.r = r
        self.psi = psi
        self.fi = fi

    def spherical_coordinate_to_polar(self):
        x = self.r * math.sin(math.radians(self.psi)) * math.cos(math.radians(self.fi))
        y = self.r * math.sin(math.radians(self.psi)) * math.sin(math.radians(self.fi))
        z = self.r * math.cos(math.radians(self.psi))

        vector = Vector3D(round(x, 2), round(y, 2), round(z, 2))
        return vector


def main():
    print("Aggregation\n\n")
    print("==================================================================================================================")
    print("two dimensional vectors\n")

    vector2d_1 = Vector2D(1, 2)
    vector2d_2 = Vector2D(1, 5)

    print("Components vector2d_1:   ", vector2d_1.getComponents(), " |   Components vector2d_2:   ", vector2d_2.getComponents())
    print("Abs vector2d_1:          ", vector2d_1.abs(), "   |   Abs vector2d_2:          ", vector2d_2.abs())
    print("Angle vector2d_1:        ", vector2d_1.getAngle(), "  |   Angle vector2d_2:        ", vector2d_2.getAngle())

    print("\nDot product of 'vector2d_1' and 'vector2d_2' vectors:", vector2d_1.cdot(vector2d_2))

    print("\n==================================================================================================================")
    print("three dimensional vectors\n")

    vector3d_1 = Vector3D(1, 1, 2)
    vector3d_2 = Vector3D(1, 4, 5)
    decorator = Decorator(1, 1, 2)

    print("Components vector3d_1:  ", vector3d_1.getComponents(), "     |   Components vector3d_2:  ", vector3d_2.getComponents())
    print("Abs vector3d_1:         ", vector3d_1.abs(), "          |   Abs vector3d_2:         ", vector3d_2.abs())
    print("Angle vector3d_1:       ", vector3d_1.getAngle(), "  |   Angle  vector3d_2:      ", vector3d_2.getAngle())

    print("\nDot product of vector3d_1, vector3d_2:", vector3d_1.cdot(vector3d_2))

    print("\nCross multiplication:", decorator.cross_multiplication(vector3d_2).getComponents())

    print("\n===================================================================================================================")
    print("Convert coordinates\n")

    adapter_2D = Adapter2D(3, 30)
    print("From polar to cartesian:    ", adapter_2D.from_polar_to_cartesian().getComponents())

    adapter_3D = Adapter3D(2, 30, 30)
    print("From spherical to cartesian:", adapter_3D.spherical_coordinate_to_polar().getComponents())


if __name__ == "__main__":
    main()