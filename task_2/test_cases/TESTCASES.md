
| <!-- -->        | <!-- -->        
|:-------------   |:---------------
| **ID**          | **1**           
| Title           | Проверка отображения выбранной категории в фильтрах
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/              
| Steps           | 1. Нажать на выпадающий список под "Filter by platform"
|                 | 2. Выбрать любую категорию
| Expected result | В поле с выпадающем окном отображается выбранная пользователем категория                
| Status          | Passed            
|                 |
| **ID**          | **2**
| Title           | Проверка закрытия выпадающего окна при выборе категории
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под "Filter by platform"
|                 | 2. Не выбирая категории, повторно нажать на выпадающий список
| Expected result | Выпадающий список заркылся
| Status          | Passed
|                 |
| **ID**          | **3**
| Title           | Проверка сохранения выбранных категорий после перезагрузки страницы
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Выбрать любые категории в каждом из трех фильтров
|                 | 2. Перезагрузить страницу
| Expected result | После перезагрузки страницы в фильтрах отображаются все выбранные категории
| Status          | $${\color{red}Fail}$$
