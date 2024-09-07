
| <!-- -->        | <!-- -->        
|:-------------   |:---------------
| **ID**          | **1**           
| Title           | Проверка отображения выбранной категории в фильтрах
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/              
| Steps           | 1. Нажать на выпадающий список любого фильтра, например, "Filter by platform"
|                 | 2. Выбрать любую категорию
| Expected result | В поле с выпадающем окном отображается выбранная пользователем категория                
| Status          | ${\color{green}Passed}$            
|                 |
| **ID**          | **2**
| Title           | Закрытие выпадающего окна при выборе категории повторным тапом
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список любого фильтра, например, "Filter by platform"
|                 | 2. Не выбирая категории, повторно нажать на выпадающий список
| Expected result | Выпадающий список заркылся
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **3**
| Title           | Проверка сохранения выбранных категорий после перезагрузки страницы
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Выбрать любые категории в каждом из трех фильтров
|                 | 2. Перезагрузить страницу
| Expected result | После перезагрузки страницы в фильтрах отображаются все выбранные категории
| Status          | ${\color{red}Fail}$
|                 | 
| **ID**          | **4**
| Title           | Проверка выделения цветом при выборе категории
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/ 
| Steps           | 1. Нажать на выпадающий список под любым фильтром, например, "Filter by category"
|                 | 2. Навести курсор на любую категорию
| Expected result | Выбранная категория пользователем выделяется цветом на фоне остальных
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **5**
| Title           | Переход в другую вкладку с открытым выпадающим списком
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
|                 | В браузере дополнительно открыта любая другая вкладка
| Steps           | 1. Нажать на выпадающий список под любым из трех фильтров
|                 | 2. Перейти во вторую вкладку
|                 | 3. Вернуться на вкладку с главной страницей
| Expected result | Выбранный пользователем выпадающий список остался открытым
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **6**
| Title           | Проверка фильтра "Sort By" 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под фильтром "Sort by"
|                 | 2. Выбрать любой способ сортировки, например, "Alphabetical"
| Expected result | Карточки игр отсортировались в соответствии с выбранным параметром
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **7**
| Title           | Проверка сохранения сортировки карточек игр
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
|                 | Выбран любой способ сортировки "Sort by", например, "Popularity"
| Steps           | 1. Нажать на любую карточку игры с первой страницы
|                 | 2. Дождаться, пока карточка полностью загрузится
|                 | 3. Перейти назад с помощью стрелки браузера или клавиши Backspace
| Expected result | Попадаем на предыдущую страницу, карточки товаров также рассортированы по раннее выбраному параметру
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **8**
| Title           | Проверка смены категории на "not chosen"
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на любой выпадающий список фильтра, например, "Filter by category"
|                 | 2. Выбрать любую категорию, например, "sports"
|                 | 3. Дождаться загрузки страницы
|                 | 4. Сменить предыдущий выбранный параметр на "not chosen"
| Expected result | Примененный ранее фильтр отменился, карточки товаров отображаются без привяки к категории
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **8**
| Title           | Проверка работы трех фильтров одновременно
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список фильтра "Filter by platform"
|                 | 2. Выбрать любую платформу, например, "PC"
|                 | 3. Нажать на выпадающий список фильтра "Filter by category"
|                 | 4. Выбрать любую категорию, например, "sports"
|                 | 5. Нажать на выпадающий список фильтра "Sort by"
|                 | 6. Выбрать любой параметр, например, "Release date"
| Expected result | Все выбранные фильтры применились, на странице отобраэаются карточки соответствующие всем трем фильтрам одновременно
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **9**
| Title           | Проверка смены категорий
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на любой выпадающий список фильтра, например, "Filter by category"
|                 | 2. Выбрать любую категорию, например, "social"
|                 | 3. Дождаться загрузки страницы
|                 | 4. Изменить только что примененную категорию на любую другую, например "moba"
| Expected result | Отображаются карточки товара только в соответствии с новой выбранной категорией
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **9**
| Title           | Выбор категории при помощи клавиатуры
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под любым фильтром, например, "Filter by category"
|                 | 2. С помощью стрелок на клавиатуре выбрать любую категорию, например, "social"
|                 | 3. Нажать на клавиатуре Enter
| Expected result | Выбранный фильтр успешно применился
| Status          | ${\color{green}Passed}$
|                 |
|                 |
| **ID**          | **10**
|                 |

