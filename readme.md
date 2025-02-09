## Паттерн Строитель
Строитель (Builder) — это порождающий паттерн проектирования, который позволяет создавать сложные объекты поэтапно. Этот паттерн разделяет процесс создания объекта и его представление, что позволяет использовать один и тот же процесс создания для получения различных представлений.
Цель паттерна

## Целью паттерна 
Строитель является упрощение создания объектов с множеством параметров и конфигураций. Он позволяет:

Избежать большого количества конструкторов с различными параметрами.
    Упростить процесс создания сложных объектов, разбив его на более мелкие шаги.
    Сделать код более читаемым и поддерживаемым.

## Проблема, которую решает паттерн
Проблема, которую решает паттерн Строитель, заключается в том, что создание сложных объектов может быть запутанным и трудоемким, особенно когда у объекта много параметров или когда некоторые параметры могут быть необязательными. Использование множества конструкторов или методов для настройки объекта может привести к путанице и усложнению кода.

## Когда использовать паттерн
    1. Паттерн Строитель рекомендуется использовать в следующих случаях:

    2.Когда необходимо создать объект с множеством параметров, особенно если некоторые из них являются необязательными.
    
    3.Когда объект должен быть создан поэтапно.
    
    4.Когда требуется создать разные представления одного и того же объекта.
