![image](https://github.com/VsevolodYatsuk/devops-kt3/assets/130091517/6a969638-6466-431e-a94c-30c3dac6d091)![image](https://github.com/VsevolodYatsuk/devops-kt3/assets/130091517/7a32bee6-6c0d-4cd9-a8bf-bab4cf7fb43b)# README

## Изменения в файле Python

1. Добавлены импорты `threading` и `time`.
2. Добавлена новая метрика `COUNTER` для периодических задач.
3. Добавлена функция `periodic_task`, которая увеличивает `COUNTER` каждые 30 секунд.
4. Создан и запущен поток для выполнения `periodic_task` параллельно с основным сервером.
5. Добавлен метод `log_message` для логирования запросов.

## Работа Docker и docker-compose.yml

### Dockerfile

1. Создает образ на основе Python.
2. Копирует файл `gauge1.py` в контейнер.
3. Устанавливает зависимости.
4. Запускает Python скрипт.

### docker-compose.yml

1. Создает сеть для взаимодействия контейнеров.
2. Описывает сервисы:
   - `prometheus`: собирает метрики.
   - `grafana`: отображает метрики.
   - `app`: запускает Python приложение для сбора пользовательских метрик.

### Скриншоты
1. ![image](https://github.com/VsevolodYatsuk/devops-kt3/assets/130091517/284e98d0-d56b-4010-8523-c8480b3f0435)
2. Метрики: ![image](https://github.com/VsevolodYatsuk/devops-kt3/assets/130091517/464e44d2-22ac-4155-a49c-ddc308b467c7)
3. График: ![image](https://github.com/VsevolodYatsuk/devops-kt3/assets/130091517/da4b157c-1536-4b85-bdb1-34a09135b325)

### Пояснение почему изменил код и почему только одно задание.
Изменил код потому что я не мог сделать нормальный график (возможно я просто тупой и не вижу простых путей). <br>
А не сделал еще 3 задания, так как по факту это было бы переписывание кода, где я меняю значения в Dockerfile и чуть-чуть меняю код в py файле. <br>



