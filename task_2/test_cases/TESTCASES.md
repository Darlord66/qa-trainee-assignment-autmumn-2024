
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
| Title           | Сортировка игр по выбранной категории с помощью фильтра "Filter by category"
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под фильтром "Filter by category"
|                 | 2. Выбрать любую категорию, например, "mmorpg"
| Expected result | Показываются игры только выбранной пользователем категории
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **7**
| Title           | Сортировка игр по заданному параметру с помощью фильтра "Sort By" 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под фильтром "Sort by"
|                 | 2. Выбрать любой способ сортировки, например, "Alphabetical"
| Expected result | Карточки игр отсортировались в соответствии с выбранным параметром
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **8**
| Title           | Проверка сохранения сортировки карточек игр
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
|                 | Выбран любой способ сортировки "Sort by", например, "Popularity"
| Steps           | 1. Нажать на любую карточку игры с первой страницы
|                 | 2. Дождаться, пока карточка полностью загрузится
|                 | 3. Перейти назад с помощью стрелки браузера или клавиши Backspace
| Expected result | Пользователь попадает на предыдущую страницу, карточки товаров также рассортированы по раннее выбраному параметру
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **9**
| Title           | Проверка смены категории на "not chosen"
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на любой выпадающий список фильтра, например, "Filter by category"
|                 | 2. Выбрать любую категорию, например, "sports"
|                 | 3. Дождаться загрузки страницы
|                 | 4. Сменить предыдущий выбранный параметр на "not chosen"
| Expected result | Примененный ранее фильтр отменился, карточки товаров отображаются без привязки к категории
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **10**
| Title           | Проверка работы трех фильтров одновременно
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список фильтра "Filter by platform"
|                 | 2. Выбрать любую платформу, например, "PC"
|                 | 3. Нажать на выпадающий список фильтра "Filter by category"
|                 | 4. Выбрать любую категорию, например, "sports"
|                 | 5. Нажать на выпадающий список фильтра "Sort by"
|                 | 6. Выбрать любой параметр, например, "Release date"
| Expected result | Все выбранные фильтры применились, на странице отображаются карточки соответствующие всем трем фильтрам одновременно
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **11**
| Title           | Проверка смены категорий
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на любой выпадающий список фильтра, например, "Filter by category"
|                 | 2. Выбрать любую категорию, например, "social"
|                 | 3. Дождаться загрузки страницы
|                 | 4. Изменить только что примененную категорию на любую другую, например "moba"
| Expected result | Список игр обновился в соответствии с новой выбранной категорией
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **12**
| Title           | Выбор категории при помощи клавиатуры
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под любым фильтром, например, "Filter by category"
|                 | 2. С помощью стрелок на клавиатуре выбрать любую категорию, например, "social"
|                 | 3. Нажать на клавиатуре Enter
| Expected result | Выбранный фильтр успешно применился
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **13**
| Title           | Сохранение фильтров после перехода в карточку товара
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на выпадающий список под "Filter by category"
|                 | 2. Выбрать любую категорию, например, "sports"
|                 | 3. Перейти в любую карточку игры
|                 | 4. Проскроллить вниз
|                 | 5. Нажать на кнопку "Back to main"
| Expected result | Выбранный раннее фильтр отображается в поле выбора
| Status          | ${\color{red}Fail}$
|                 |
|                 |
|                 |
| **ID**          | **14**
| Title           | Выделение цветом кнопки "Back to main" при наведении курсора
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Открыть любую карточку игры
|                 | 2. Проскроллить вниз
|                 | 3. Убедиться, что слева внизу присутствует кнопка "Back to main"
|                 | 4. Навести курсор 
| Expected result | Кнопка подсвечивается при наведении курсора
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **15**
| Title           | Возвращение на главную страницу из карточки товара с помощью кнопки "Back to main"
| Precondition    | Открыта главная, первая страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Открыть любую карточку игры с первой страницы
|                 | 2. Проскроллить вниз
|                 | 3. Нажать на кнопку "Back to main"
| Expected result | Пользователь вернулся на первую страницу, кнопка работает
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **16**
| Title           | Возвращение на предыдущую выбранную страницу из карточки товара с помощью кнопки "Back to main"
| Precondition    | Открыта любая страница сайта, например, 4 - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Перейти в любую карточку игры на выбранной странице (кроме первой страницы)
|                 | 2. Проскроллить вниз
|                 | 3. Нажать на кнопку "Back to main"
| Expected result | Открывается страница, с которой была открыта карточка игры
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **17**
| Title           | Открытие главной страницы в новой вкладке с помощью кнопки "Back to main"
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Нажать на любую карточку игры
|                 | 2. Проскроллить вниз
|                 | 3. Нажать на кнопку "Back to main" помощью колесика мыши / сочетанием ЛКМ + Ctrl
| Expected result | В новой вкладке браузера открылась главная страница сайта
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **18**
| Title           | Открытие главной страницы в новой вкладке по контекстному меню кнопки "Back to main"
| Precondition    | Открыта любая карточка игры, например, - https://makarovartem.github.io/frontend-avito-tech-test-assignment/game/540
| Steps           | 1. Проскроллить вниз
|                 | 2. Найти кнопку "Back to main"
|                 | 3. Нажать по ней ПКМ для вызова контекстного меню
|                 | 4. Убедиться, что присутствует возможность "Открыть ссылку в новой вкладке"
|                 | 5. Нажать "Открыть ссылку в новой вкладке"
| Expected result | В новой вкладке браузера открылась главная страница сайта
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **19**
| Title           | Проверка кликабельности всей кнопки, не только текста "Back to main"
| Precondition    | Открыта любая карточка игры, например, - https://makarovartem.github.io/frontend-avito-tech-test-assignment/game/540
| Steps           | 1. Проскроллить вниз
|                 | 2. Найти кнопку "Back to main"
|                 | 3. Кликнуть по кнопке в любом месте, где нет текста кнопки
| Expected result | Вся площадь кнопки кликабельна
| Status          | ${\color{green}Passed}$
|                 |
|                 |
|                 |
| **ID**          | **20**
| Title           | Выбранная страница выделяется в списке номеров страниц 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Убедиться, что в списке номеров страниц выделена первая страница
|                 | 2. Перейти на любую другую страницу, например, пятую 
| Expected result | Пользователь попадает на страницу, выбранная страница выделена в списке номеров страниц
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **21**
| Title           | Переход на предыдущую страницу 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Перейти на любую страницу кроме первой, например, четвертую
|                 | 2. Нажать на стрелочку назад в списке номеров страниц ("Previous page")
| Expected result | Открылась предыдущая страница
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **22**
| Title           | Переход на следующую страницу
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Перейти на любую страницу кроме последней, например, вторую
|                 | 2. Нажать на стрелочку вперед в списке номеров страниц ("Next page")
| Expected result | Открылась следующая страница
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **23**
| Title           | Отсутствии возможности перехода на предыдущую страницу с первой
| Precondition    | Открыта первая страница сайта - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Навести курсор на стрелочку назад в списке номеров страниц ("Previous page")
| Expected result | Кнопка не кликабельна, отображается заглушка 
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **24**
| Title           | Отсутствии возможности перехода на следующую страницу с последней
| Precondition    | Открыта последняя страница сайта - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Навести курсор на стрелочку вперед в списке номеров страниц ("Next page")
| Expected result | Кнопка не кликабельна, отображается заглушка
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **25**
| Title           | Проверка смены количества отображения карточек на странице
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. В выпадающем списке выбрать новый лимит, например, 20 
| Expected result | Количество отображения капточек игр на странице изменилось в соответствии с новым выбранным лимитом
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **26**
| Title           | Проверка смены отображения количества карточек на странице с помощью ввода
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. В выпадающем списке ввести с клавиатуры один из лимитов, доступных в выпадающем списке, например, 20 
|                 | 4. Нажать Enter
| Expected result | Количество карточек игр на странице изменилось в соответствии с новым выбранным лимитом
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **27**
| Title           | Проверка смены количества отображения карточек с помощью ввода нестандартного значения в диапазоне возможных
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. В выпадающем списке ввести с клавиатуры один из лимитов, недоступным в выпадающем списке, но в диапазоне предложенных например, 12
|                 | 4. Нажать Enter
| Expected result | Количество карточек игр на странице не изменилось, пользователь видит заглушку 
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **28**
| Title           | Проверка отображения карточек на странице при выборе максимально возможного лимита
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. В выпадающем списке выбрать максимальный доступный лимит  
| Expected result | Количество карточек игр на странице изменилось в соответствии с новым выбранным лимитом
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **29**
| Title           | Проверка смены количества отображения карточек при вводе значения за максимальной границей диапазона
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. В выпадающем списке ввести с клавиатуры любое значение, которое больше максимальной границы диапазона, например, 110
|                 | 4. Нажать Enter
| Expected result | Количество карточек игр на странице не изменилось, пользователь видит заглушку 
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **30**
| Title           | Проверка смены количества отображения карточек при вводе значения за минимальной границей диапазона
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. В выпадающем списке ввести с клавиатуры любое значение, которое меньше минимальной границы диапазона, например, 6
|                 | 4. Нажать Enter
| Expected result | Количество карточек игр на странице не изменилось, пользователь видит заглушку 
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **31**
| Title           | Изменение количества страниц после смены лимита карточек на странице
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Найти возле списка страниц окошко для смены количества карточек на странице
|                 | 2. Нажать на него
|                 | 3. Изменить на любое допустимое значение
| Expected result | Количество страниц изменилось
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **32**
| Title           | Открытие страницы из блока пагинации в новой вкладке 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Навести курсор на любую страницу, кроме текущей 
|                 | 2. С помощью колесика мыши/ЛКМ + Ctrl/ПКМ и контекстного меню открыть выбранную страницу в новой вкладке
| Expected result | Выбранная страница открылась в новой вкладке
| Status          | ${\color{red}Fail}$
|                 |
| **ID**          | **33**
| Title           | Перелистывание на следующие 5 страниц с помощью кнопки "Next 5 pages" в блоке пагинации 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Открыть любую страницу из блока пагинации, например, 7
|                 | 2. Нажать на три точки "Next 5 pages"
| Expected result | В блоке пагинации пользователь видит следующие 5 страниц
| Status          | ${\color{green}Passed}$
|                 |
| **ID**          | **33**
| Title           | Перелистывание на предыдущие 5 страниц с помощью кнопки "Previous 5 pages" в блоке пагинации 
| Precondition    | Открыта главная страница - https://makarovartem.github.io/frontend-avito-tech-test-assignment/
| Steps           | 1. Открыть любую страницу из блока пагинации, например, 23
|                 | 2. Нажать на три точки "Previous 5 pages"
| Expected result | В блоке пагинации пользователь видит предыдущие 5 страниц
| Status          | ${\color{green}Passed}$













