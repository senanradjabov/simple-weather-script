# Simple Weather Script ☀️🌧

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Typing](https://img.shields.io/badge/Typing-100%25-blueviolet)](#)
[![Status](https://img.shields.io/badge/Project-educational-success)](#)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)
[![Course](https://img.shields.io/badge/Course-%D0%A2%D0%B8%D0%BF%D0%B8%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9%20Python-lightgrey)](https://to.digital/typed-python/)

---

## Русская версия

### 📌 Описание

Это простой скрипт для получения информации о текущей погоде на основе вашего IP.

### 🔍 Как это работает

1. **`coordinates.py`** — использует библиотеку `requests` для получения текущих координат пользователя через сервис [ipinfo.io](https://ipinfo.io/json).
2. **`weather_api_service.py`** — с помощью координат получает данные о погоде из [OpenWeatherMap](https://openweathermap.org/).
3. **`weather_formatter.py`** — форматирует полученную информацию о погоде в удобный для чтения вид.
4. **Типизация** — проект полностью типизирован с использованием стандартных инструментов: `typing`, `dataclasses`, `Protocol`.
5. **`config.py`** — файл конфигурации.
6. **`history.py`** — реализован `Protocol` для хранения истории погоды, а также два способа сохранения:
   - в `.txt` файл
   - в `.json` файл

### 🚀 Как запустить

1. Клонируйте репозиторий:

```bash
git clone <ссылка на репозиторий>
cd <имя-папки-проекта>
```

2. Создайте файл `.env`, скопировав `.env.example`:

```bash
cp .env.example .env
```

3. Укажите API ключ от OpenWeather в `.env`:

```
OPENWEATHER_API=ваш_ключ
```

4. Установите зависимости и запустите:

```bash
uv sync
uv run --env-file ".env" .\main.py
```

### 📦 Зависимости

- `requests`
- `uv` — менеджер запуска

### ✅ Пример вывода

```
Погода в Moscow, RU:
Температура: 15°C
Описание: Облачно
Влажность: 72%
```

### 🧩 Структура проекта

```
.
├── coordinates.py
├── weather_api_service.py
├── weather_formatter.py
├── config.py
├── history.py
├── main.py
├── .env.example
└── README.md
```

### 📘 Об обучении

Код написан в процессе прохождения курса **«Типизированный Python для профессиональной разработки»** от **Алексея Голобурдина**, команда **Диджитализируй!**.

---

## English Version

### 📌 Description

A simple script to get the current weather based on your IP address.

### 🔍 How it works

1. **`coordinates.py`** — uses `requests` to get the user's current coordinates via [ipinfo.io](https://ipinfo.io/json).
2. **`weather_api_service.py`** — gets weather data from [OpenWeatherMap](https://openweathermap.org/) using the coordinates.
3. **`weather_formatter.py`** — formats the weather data into a readable output.
4. **Typing** — the entire project is strictly typed using built-in tools like `typing`, `dataclasses`, and `Protocol`.
5. **`config.py`** — config file.
6. **`history.py`** — defines a `Protocol` for storing weather history, with two implementations:
   - Save to `.txt` file
   - Save to `.json` file

### 🚀 How to run

1. Clone the repository:

```bash
git clone <repository-link>
cd <project-folder>
```

2. Create a `.env` file based on the example:

```bash
cp .env.example .env
```

3. Add your OpenWeather API key to `.env`:

```
OPENWEATHER_API=your_key
```

4. Install dependencies and run the script:

```bash
uv sync
uv run --env-file ".env" .\main.py
```

### 📦 Dependencies

- `requests`
- `uv` — project runner

### ✅ Example Output

```
Weather in Moscow, RU:
Temperature: 15°C
Description: Cloudy
Humidity: 72%
```

### 🧩 Project Structure

```
.
├── coordinates.py
├── weather_api_service.py
├── weather_formatter.py
├── config.py
├── history.py
├── main.py
├── .env.example
└── README.md
```

### 📘 About the Course

This code was written during the course **“Typed Python for Professional Development”** by **Alexey Goloburdin**, team **Digitaliziruy!**
