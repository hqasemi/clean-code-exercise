from typing import List, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Point:
    x: float
    y: float

    @classmethod
    def from_tuple(cls, item: Tuple[float, float]) -> "Point":
        # TODO: add validation that tuple has exactly two elements which are float
        return cls(item[0], item[1])


class PearsonCorrelationCoefficientCalculator:
    def __init__(self, points: List[Point]) -> None:
        self.__points = points
        self.__sample_size: int = len(points)
        self.__sample_mean_x: float = self.__calculate_sample_mean_x()
        self.__sample_mean_y: float = self.__calculate_sample_mean_y()
        self.__c_num: float = self.__calculate_c_num()
        self.__d_den_x: float = self.__calculate_d_den_x()
        self.__e_den_y: float = self.__calculate_e_den_y()
        self.__d: float = self.__calculate_d()


    def result(self):
        d = self.__d
        if d == 0:
            return 0
        
        return self.__c_num/ ((self.__d_den_x* self.__e_den_y) ** 0.5)

    def __calculate_sample_mean_x(self)-> float:
        """ calculates sample mean for x of all sample points """
        summation_of_x_axis : float = 0
        for point in self.__points:
            summation_of_x_axis += point.x
        
        return summation_of_x_axis/self.__sample_size
    
    def __calculate_sample_mean_y(self)-> float:
        """ calculates sample mean for y of all sample points """
        summation_of_y_axis : float = 0
        for point in self.__points:
            summation_of_y_axis += point.y
        
        return summation_of_y_axis/self.__sample_size

    def __calculate_c_num(self) -> float:
        c_num: float = 0
        for point in self.__points:
            c_num += (point.x - self.__sample_mean_x) * (point.y - self.__sample_mean_y)

        return c_num
    
    def __calculate_d_den_x(self) -> float:
        d_den_x: float = 0
        for point in self.__points:
            d_den_x += (point.x - self.__sample_mean_x) ** 2

        return d_den_x

    def __calculate_e_den_y(self) -> float:
        e_den_y: float = 0
        for point in self.__points:
            e_den_y += (point.y - self.__sample_mean_y) ** 2

        return e_den_y
    
    def __calculate_d(self) -> float:
        return ((self.__d_den_x* self.__e_den_y) ** 0.5)
    

def read_from_file(file_path: Path) -> List[str]:
    """ reads a file and return list of lines """
    # TODO: add error handling
    with open(file_path, 'r') as f:
        return f.readlines()
 
def convert_list_of_string_to_list_of_points(input_list: List[str]) -> List[Point]:
    output: List[Point] = []
    for line in input_list:
        parts: Tuple[str, str] =line.strip().split(',')
        parts_float: Tuple[float, float] =  tuple(map(float, parts))
        point: Point = Point.from_tuple(parts_float)
        output.append(point)
    return output


if __name__ == "__main__":
    lines = read_from_file(file_path=Path("1.pearson_correlation_coefficient\sample.csv"))
    points : List[Point] = convert_list_of_string_to_list_of_points(input_list=lines)
    result = PearsonCorrelationCoefficientCalculator(points).result()
    print(result)
