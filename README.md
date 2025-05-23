# Магазин электроники

Проект представляет собой реализацию системы управления магазином электроники с использованием объектно-ориентированного программирования в Python.

## Функциональность

- Абстрактный базовый класс `BaseProduct` для продуктов
- Класс `Product` для базовых продуктов
- Специализированные классы `Smartphone` и `LawnGrass`
- Класс `Category` для управления категориями товаров
- Миксин `CreationLoggerMixin` для логирования создания объектов

## Структура проекта

- `models.py` - основные классы и их реализация
- `main.py` - пример использования классов
- `test_models.py` - тесты для проверки функциональности

## Запуск

Для запуска основного кода:
```bash
python main.py
```

Для запуска тестов:
```bash
pytest test_models.py
```

## Требования

- Python 3.7+
- pytest (для запуска тестов) 