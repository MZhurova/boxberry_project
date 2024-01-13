<h1> Проект по тестированию логистического веб-сервиса <a target="_blank" href="https://boxberry.ru/">"Boxberry"</a> </h1>

![This is an image](design/images/logo-boxberry.png)

----
## *UI-тесты*
### Список проверок, реализованных для главной страницы
#### Auto Tests
- [x] *Установка города. Проверка, что установился выбранный город*
- [x] *Редирект на страницу логина для интернет-магазинов из списка по кнопке "Личный кабинет"*
- [x] *Переход на странцу восстановления пароля*
- [x] *Поиск посылки по трек-номеру. Проверка, открытия страницы с информацией по отслеживаемой посылке*
### Список проверок, реализованных для страницы "Отправить посылку"
#### Auto Tests
- [x] *Переход к калькулятору расчета посылок для частных клиентов по кнопке "Рассчитать"*
- [x] *Расчет стоимости доставки, в зависимости от маршрута, габаритов послыки и выбранной упаковки*
- [x] *Открытие страницы с информацией "Как получить посылку" по кнопке*
### Список проверок, реализованных для страницы "Бизнесу"
#### Auto Tests
- [x] *Переход к калькулятору расчета посылок для интернет-магазинов по кнопке "Рассчитать"*
- [x] *Расчет стоимости доставки, в зависимости от маршрута и габаритов послыки*
- [x] *Переход к калькулятору расчета посылок для интернет-магазинов по кнопке "Показать отделения"*
- [x] *Поиск отделений в указанном городе*
- [x] *Корректность сообщения о ненахождении заказа, при поиске по несуществующему трек-номеру*
#### Manual Tests
- [x] *Поиск отделений, где доступен "Экспресс-прием"*
- [x] *Поиск отделений, где доступен "Прием на терминале"*

## *API-тесты*
### Список проверок, реализованных для методов
- [x] *Получение успешных статус кодов и валидация ответов по схемам*
- [x] *Полное сравнение ответа с эталонным файлами*
- [x] *Запросы с несколькими параметрами*
- [x] *Параметризованные тесты с несколькими аргументами*
- [x] *Получение пустого массива*
- [x] *Получение ошибки при неверном запросе*
- [x] *Проверка полученных массивов на длину*



![This is an image](design/images/man.png)

----
### Проект реализован с использованием:
<p  align="center">
    <code><img src="design/icons/python-original.svg" width="50" title="Python"></code>
    <code><img src="design/icons/pytest.png" width="50" title="Pytest"></code> 
    <code><img src="design/icons/github.svg" width="50" title="GitHub"></code> 
    <code><img src="design/icons/intellij_pycharm.png" width="50" title="PyCharm"></code>
    <code><img src="design/icons/selene.png" width="50" title="Selene"></code>
    <code><img src="design/icons/selenium.png" width="50" title="Selenium"></code>
    <code><img src="design/icons/requests.png" width="40" title="Requests"></code>
    <code><img src="design/icons/selenoid.png" width="50" title="Selenoid"></code>
    <code><img src="design/icons/jenkins.png" width="50" title="Jenkins"></code>
    <code><img src="design/icons/allure_report.png" width="50" title="Allure Report"></code>
    <code><img src="design/icons/allure_testops.png" width="50" title="Allure TestOps"></code>
    <code><img src="design/icons/telegram.png" width="50" title="Telegram"></code>
    <code><img src="design/icons/jira.svg" width="50" title="Jira"></code>
</p>

----

### Локальный запуск автотестов

#### Выполнить в cmd:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----


### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/boxberry_project/">Ссылка на проект</a>

#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/boxberry_project/">проект</a>

![jenkins project main page](design/images/jenkins.jpg)

2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке ENVIRONMENT

![jenkins_build](design/images/jenkins_build.jpg)

4. Указать комментарий в поле COMMENT
5. Нажать кнопку `Build`

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](design/images/allure_report.jpg)

#### Результаты прохождения теста
![allure_reports_behaviors](design/images/allure_suites.jpg)

#### Графики

![allure_reports_graphs](design/images/graphics.jpg)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3862/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](design/images/dashboards.jpg)

#### История запуска тестовых наборов

![allure_testops_launches](design/images/launches.jpg)

#### Manual и Auto тест-кейсы

![allure_testops_suites](design/images/suites.jpg)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-992">Ссылка на проект</a>

![jira_project](design/images/jira_992.jpg)

----

### Оповещения в Telegram
![telegram_allert](design/images/tg.jpg)

----

### Видео прохождения автотеста

#### Рассчет стоимости доставки послыки для частных клипентов 

![Рассчет стоиомсти доставки посылки для частных клиентов](design/images/video.gif)

----
