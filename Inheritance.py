from abc import abstractmethod
import math


class IVector:
    @abstractmethod
    def abs(self):       # oblicza modul wektora
        pass

    @abstractmethod
    def cdot(self, vector):     # oblicza iloczyn skalarnz miedzy dwoma wektorami
        pass

    @abstractmethod
    def getComponents(self):      # zwraca skladowe wektora
        pass

    @abstractmethod
    def getAngle(self):         # zwraca kąt pomiędzy wektorem, a osią OX
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
        return round(dot_product, 2)


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        Vector2D.__init__(self, x, y)
        self.z = z

    def abs(self):
        x, y = super().getComponents()
        return round(math.sqrt(pow(x, 2) + pow(y, 2) + pow(self.z, 2)), 2)

    def getComponents(self):
        x, y = super().getComponents()
        return [x, y, self.z]

    def getAngle(self):
        x, y = super().getComponents()

        fi = math.atan(y / x)
        psi = math.atan(math.sqrt(pow(x, 2) + pow(y, 2)) / self.z)

        angle = [round(fi, 2), round(psi, 2)]
        return angle

    def cdot(self, vector):
        x, y = super().getComponents()
        x_vector, y_vector, z_vector = vector.getComponents()
        dot_product = x * x_vector + y * y_vector + self.z * z_vector
        return round(dot_product, 2)

    def cross_multiplication(self, vector):
        x_vector, y_vector, z_vector = vector.getComponents()
        x, y = super().getComponents()

        x_product = y * z_vector - (self.z * y_vector)
        y_product = self.z * x_vector - (x * z_vector)
        z_product = x * y_vector - (y * x_vector)

        new_vector = Vector3D(round(x_product, 2), round(y_product, 2), round(z_product, 2))

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
    print("Inheritance\n\n")
    print("==================================================================================================================")
    print("two dimensional vectors\n")

    vector2d_1 = Vector2D(1, 2)
    vector2d_2 = Vector2D(1, 5)

    print("Components vector2d_1:   ", vector2d_1.getComponents(), " |   Components vector2d_2:   ",
          vector2d_2.getComponents())
    print("Abs vector2d_1:          ", vector2d_1.abs(), "   |   Abs vector2d_2:          ", vector2d_2.abs())
    print("Angle vector2d_1:        ", vector2d_1.getAngle(), "  |   Angle vector2d_2:        ", vector2d_2.getAngle())

    print("\nDot product of 'vector2d_1' and 'vector2d_2' vectors:", vector2d_1.cdot(vector2d_2))

    print("\n==================================================================================================================")
    print("three dimensional vectors\n")

    vector3d_1 = Vector3D(1, 1, 2)
    vector3d_2 = Vector3D(1, 4, 5)

    print("Components vector3d_1:  ", vector3d_1.getComponents(), "     |   Components vector3d_2:  ", vector3d_2.getComponents())
    print("Abs vector3d_1:         ", vector3d_1.abs(), "          |   Abs vector3d_2:         ", vector3d_2.abs())
    print("Angle vector3d_1:       ", vector3d_1.getAngle(), "  |   Angle  vector3d_2:      ", vector3d_2.getAngle())

    print("\nDot product of vector3d_1, vector3d_2:", vector3d_1.cdot(vector3d_2))

    print("\nCross multiplication:", vector3d_1.cross_multiplication(vector3d_2).getComponents())

    print("\n===================================================================================================================")
    print("Convert coordinates\n")

    adapter_2D = Adapter2D(3, 30)
    print("From polar to cartesian:    ", adapter_2D.from_polar_to_cartesian().getComponents())

    adapter_3D = Adapter3D(2, 30, 30)
    print("From spherical to cartesian:", adapter_3D.spherical_coordinate_to_polar().getComponents())


if __name__ == "__main__":
    main()
