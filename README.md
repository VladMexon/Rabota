# Разработка системы контроля вляжности
## Цель
Создать систему состоящую из датчика влажности, увлажнителя воздуха, android-приложения для выставления желаемой и отлеживания текущей влажности

## Серверная часть
### Содержит состоит из 2 python скриптов:
1. server.py - файл скрипта управляющего системой. Предсталяет из себя web-сервер написанный с использованием python пакета flask. В нем содержится 4 api метода для записи и получения желаемой и текущей влажностей.
2. humiditySensorEmulator.py - в связи с отутствием модуля микрокомпьютера, было принято решение написать простой скрипт, который изменяет текущую влажность в зависимости от желаемой.
### Интеграция с systemd
Была произведена интеграция приложения с systemd путем написания файла humiditySensorServer. Данный файл был перемешен по пути "/etc/systemd/system/" и выполнена команда sudo systemctl start humiditySensorServer.service.
Это позволяет управлять процессом и просматривать его статус командами sytemctl. А ткже просматривать его логи командой journalctl -u humiditySensorServer.service.

## Мобильная часть
...