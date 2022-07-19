"""Общие функции для всех файлов сервера"""
__author__ = 'RetteraDev'

import os


def get_absolute_path(relative_dir: str) -> str:
    """Метод получает абсолютный путь до файла относительно места вызова
    Args:
        relative_dir - Относительный путь
    Returns:
        path: str - Абсолютный путь
    """
    return os.path.join(os.path.dirname(__file__), relative_dir)
