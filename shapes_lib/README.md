# shapes-lib

Расширяемая библиотека для работы с геометрическими фигурами.
Поддерживает:
- площадь круга;
- площадь треугольника по трём сторонам;
- проверку «треугольник прямоугольный?»;
- «площадь без знания типа в compile-time» через словарь-спецификацию и реестр;
- расширение новыми фигурами.

## Требования
- Python 3.11+

## Установка (dev / editable)
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
pip install pytest
```

## Быстрый старт
```bash
from shapes_lib import Circle, Triangle, compute_area, is_right_triangle

print(compute_area(Circle(2)))                      # 12.566370614359172
print(compute_area({"type":"triangle","a":3,"b":4,"c":5}))  # 6.0
print(is_right_triangle(3, 4, 5))                   # True
```

## Публичный API

- `compute_area(shape_or_spec: Shape | dict) -> float`

- `is_right_triangle(a: float, b: float, c: float, *, eps: float = 1e-9) -> bool`

- `register_shape(name: str, from_dict_callable: Callable[[dict], Shape]) -> None`

## Формат словаря
Обязателен ключ `"type"`.

Поддерживаемые варианты:

- **Круг**
```python
  {"type": "circle", "radius": <r>}
```
или
```python
    {"type": "circle", "r": <r>}
```

- **Треугольник:**
```python
    {"type": "triangle", "a": <a>, "b": <b>, "c": <c>}.
```

## Валидация
- Все числовые параметры должны быть конечными и строго больше `0`.
- Для треугольника дополнительно проверяется неравенство треугольника.

### Исключения
- **`ValidationError`** — ошибка валидации или неверного формата спецификации.
- **`UnknownShapeError`** — указан неизвестный `"type"`.

## Расширение новыми фигурами
Пример: добавить прямоугольник Rectangle (без изменений существующего кода).
```bash
from shapes_lib import register_shape, compute_area, ValidationError

class Rectangle:
    def __init__(self, width: float, height: float):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise ValidationError("width/height must be positive finite number")
        if width <= 0 or height <= 0:
            raise ValidationError("width/height must be positive finite number")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    @classmethod
    def from_dict(cls, data: dict) -> "Rectangle":
        return cls(data["width"], data["height"])

register_shape("rectangle", Rectangle.from_dict)

# использование «без знания типа»
print(compute_area({"type": "rectangle", "width": 3, "height": 5}))  # 15.0
```

Рекомендация: если фигура постоянная, вынести её в отдельный модуль и вызывать register_shape при импорте.

## Запуск тестов
```bash
pytest -q
```
