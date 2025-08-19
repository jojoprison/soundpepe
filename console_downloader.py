import subprocess
import os
import shutil
import sys


def check_tool_exists(tool_name):
    """
    Проверяет, установлен ли инструмент в системе.
    
    Args:
        tool_name (str): Имя инструмента для проверки
        
    Returns:
        bool: True если инструмент найден, иначе False
    """
    return shutil.which(tool_name) is not None


def install_required_tool():
    """
    Предлагает установить необходимые инструменты.
    """
    print("Требуемые инструменты не обнаружены в системе.")
    print("Для работы скрипта необходим один из следующих инструментов:")
    print("1. scdl - специализированный инструмент для SoundCloud")
    print("2. yt-dlp - универсальный инструмент для скачивания с разных платформ")
    
    print("\nВы можете установить их следующими командами:")
    print("Для scdl: pip install scdl")
    print("Для yt-dlp: pip install yt-dlp")
    
    choice = input("\nХотите установить один из инструментов сейчас? (y/n): ").lower()
    
    if choice == 'y':
        tool_choice = input("Какой инструмент установить? (1 для scdl, 2 для yt-dlp): ")
        
        if tool_choice == '1':
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "scdl"], check=True)
                print("scdl успешно установлен!")
                return "scdl"
            except subprocess.CalledProcessError:
                print("Не удалось установить scdl. Попробуйте установить вручную.")
                sys.exit(1)
        elif tool_choice == '2':
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp"], check=True)
                print("yt-dlp успешно установлен!")
                return "yt-dlp"
            except subprocess.CalledProcessError:
                print("Не удалось установить yt-dlp. Попробуйте установить вручную.")
                sys.exit(1)
        else:
            print("Некорректный выбор.")
            sys.exit(1)
    else:
        print("Установите один из инструментов вручную и запустите скрипт снова.")
        sys.exit(1)


def download_track_by_link(track_url, download_tool="auto"):
    """
    Скачивает трек по URL-адресу с помощью выбранного инструмента.
    
    Args:
        track_url (str): URL-адрес трека на SoundCloud
        download_tool (str): Инструмент для скачивания ('scdl', 'yt-dlp', или 'auto')
        
    Returns:
        bool: True если скачивание успешно, иначе False
    """
    try:
        # Определяем, какой инструмент использовать
        if download_tool == "auto":
            if check_tool_exists("scdl"):
                download_tool = "scdl"
            elif check_tool_exists("yt-dlp"):
                download_tool = "yt-dlp"
            else:
                download_tool = install_required_tool()
        
        # Извлекаем ID трека из URL
        track_id = track_url.rstrip('/').split('/')[-1]
        print(f"Track ID extracted: {track_id}")

        # Создаем директорию для сохранения, если её нет
        dir_name = 'jaszeq'
        if not os.path.exists(dir_name):
            print(f"Creating '{dir_name}' directory")
            os.makedirs(dir_name)
        else:
            print(f"'{dir_name}' directory already exists")

        # Формируем и запускаем команду в зависимости от выбранного инструмента
        if download_tool == "scdl":
            command = [
                "scdl",
                "-l", track_url,
                "--path", dir_name,
            ]
            print(f"Используем scdl для скачивания")
        elif download_tool == "yt-dlp":
            command = [
                "yt-dlp",
                "-x",  # Extract audio
                "--audio-format", "mp3",  # Convert to mp3
                "-o", f"{dir_name}/%(title)s.%(ext)s",  # Output pattern
                track_url
            ]
            print(f"Используем yt-dlp для скачивания")
        else:
            raise ValueError(f"Неизвестный инструмент скачивания: {download_tool}")

        print(f"Constructed command: {' '.join(command)}")
        print("Running command...")
        
        result = subprocess.run(command, capture_output=True, text=True)
        print("Command finished running")

        if result.returncode == 0:
            print(f"Successfully downloaded track from {track_url}")
            return True
        else:
            print(f"Failed to download track. Error: {result.stderr}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    """
    Основная функция, которая запрашивает URL в консоли и скачивает трек.
    Позволяет скачивать несколько треков подряд до ввода команды выхода.
    """
    print("=== Консольный загрузчик музыки с SoundCloud ===")
    
    # Проверка наличия инструментов
    tool_to_use = "auto"
    has_scdl = check_tool_exists("scdl")
    has_ytdlp = check_tool_exists("yt-dlp")
    
    if not has_scdl and not has_ytdlp:
        tool_to_use = install_required_tool()
    elif has_scdl:
        print("Обнаружен scdl, будет использован для скачивания.")
        tool_to_use = "scdl"
    elif has_ytdlp:
        print("Обнаружен yt-dlp, будет использован для скачивания.")
        tool_to_use = "yt-dlp"
    
    print("\nВведите URL-адрес трека с SoundCloud для скачивания")
    print("Для выхода введите 'q', 'quit' или 'exit'")
    
    while True:
        print("\nВведите URL (или команду выхода): ")
        user_input = input().strip()
        
        # Проверка на команду выхода
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("Выход из программы...")
            break
        
        # Проверка на пустой ввод
        if not user_input:
            print("Пустой URL. Пожалуйста, введите корректный адрес.")
            continue
        
        # Проверка на валидность URL (простая)
        if not user_input.startswith(('http://', 'https://')):
            print("Некорректный URL. Адрес должен начинаться с 'http://' или 'https://'")
            continue
            
        # Скачивание трека
        print(f"Начинаем скачивание с URL: {user_input}")
        download_track_by_link(user_input, tool_to_use)
        print("Готово к скачиванию следующего трека")


if __name__ == '__main__':
    main()
