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
<p align="center">
  <![image](https://raw.githubusercontent.com/VladMexon/Rabota/Server/Server/Screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-01-16%20212027.png)>
</p>
<p align="center">
<![image](https://raw.githubusercontent.com/VladMexon/Rabota/Server/Server/Screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-01-16%20212214.png)>
</p>
## Мобильная часть
...