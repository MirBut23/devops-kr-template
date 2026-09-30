# DevOps ПР4 / Контрольная работа 1

Бутенко А.Д., ЭФБО-14-24. Учебный валидатор email, телефона и СНИЛС.
Импорт исходной Git-истории https://gitverse.ru/dgimatdinov/devops-kr-template.
Основной репозиторий: https://github.com/MirBut23/devops-kr-template
Зеркало: https://github.com/MirBut23/devops-kr-mirror

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Windows: `.venv\Scripts\activate`, затем те же команды python.
Результат: 19 passed. Это набор функций, не интерактивная программа.

## Выполненные этапы

1. Импорт шаблона в GitHub с сохранением истории; master переименована в main.
2. Настроены origin, upstream, mirror и два pushurl для origin.
3. В feature/add-phone-validation созданы четыре коммита: feat, test, wip, fix.
4. Выполнен git rebase -i HEAD~4: pick, fixup, fixup, drop.
   Функция validate_inn удалена вместе с WIP, исправление опечатки сохранено.
5. Реально воспроизведён конфликт с upstream/feature/instructor-change
   в validator.py и test/test_validator.py; сохранены три функции и все группы
   тестов. СНИЛС из исходного теста 001-001-999 32 имеет неверную контрольную
   сумму: 1*7 + 1*4 + 9*3 + 9*2 + 9*1 = 65. Добавлены корректный пример 65
   и отрицательная проверка 32. В исходных тестах также отсутствовали импорты.
6. Финальный этап выполняется через Pull Request и Squash and merge.

## Особенности относительно PDF

Шаблон имеет master и каталог test/, поэтому сохранён реальный путь test/,
а ветка в импортированном репозитории названа main. Использован HTTPS с
существующей авторизацией вместо SSH. По выбору автора зеркало находится
на GitHub, а не GitLab/Gitverse. Это импорт, а не GitHub-native fork Gitverse.
Чтобы git push origin отправлял в оба репозитория, заданы оба pushurl:

```bash
git remote set-url --add --push origin https://github.com/MirBut23/devops-kr-template.git
git remote set-url --add --push origin https://github.com/MirBut23/devops-kr-mirror.git
```

Простое добавление только mirror в pushurl переключило бы отправку лишь
на зеркало. Настройки remote локальные и не передаются обычным клонированием.

SNILS/email реализованы по учебному шаблону. Это не проверка существования
документа или адреса в реестре; алгоритм не заявлен как промышленный валидатор.
