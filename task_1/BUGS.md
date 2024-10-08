| <!-- -->           | <!-- -->        
|:-------------      |:---------------
| **ID**             | **1**           
| Title              | В результатах поиска по категориям помимо искомой марки автомобиля в подборку попадают другие автомобили 
| Expected result    | В результатах поиска должны отображаться автомобили только выбранной марки                
| Actual result      | В результатах поиска помимо автомобилей выбранной марки и модели также отображаются другие автомобили, не имеющие отношения к запросу
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
| Priority           | ${\color{red}Высокий}$
|                    | Необходимо исправить данную проблему как можно скорее, так как данная ошибка ухудшает пользовательский опыт и затрудняет поиск по сайту
|                    |
|                    |
| **ID**             | **2**           
| Title              | Ошибка в названии фильтра "Поколение" в левой колонке  
| Expected result    | У фильтра для выбора поколения автомобиля заголовок "Поколение"                 
| Actual result      | В название фильтра допущена ошибка - "Покление", вместо "Поколение"
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Проскроллить вниз до фильтра выбора поколения автомобиля 
| Priority           | ${\color{green}Низкий}$
|                    | Данная ошибка не оказывает существенного влияния на репутацию компании и сайта, находится не на главной странице, не бросается в глаза и ее можно очень быстро исправить
|                    |
|                    |
| **ID**             | **3**           
| Title              | Попадание товара из другой категории в подборку автомобилей 
| Expected result    | В подборке должны отображаться только автомобили выбранной марки и модели                
| Actual result      | При поиске определенной марки и модели автомобиля на сайте по категориям попадал товар из другой категории, а именно лобовое стекло 
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
| Priority           | ${\color{red}Высокий}$
|                    | Данная ошибка мешает пользователем эффективно находить нужные автомобили и ухудшает пользовательский опыт
|                    |
|                    |
| **ID**             | **4**           
| Title              | При фильтрации поиска автомобиля по годам выпуска попадают автомобили за пределами выбранного диапозона
| Expected result    | В подборке должны отображаться только автомобили выбранных годов выпуска                
| Actual result      | При поиске автомобилей по годам выпуска (2021-2024) попадают автомобили не из указанного диапазона (2019) 
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
|                    | 6. Проскорллить вниз до фильтра "Год выпуска"
|                    | 7. Выбрать диапазон 2021-2024
| Priority           | ${\color{red}Высокий}$
|                    | Данная ошибка мешает пользователем эффективно находить нужные автомобили и ухудшает пользовательский опыт
|                    |
|                    |
| **ID**             | **5**           
| Title              | Неверный формат отображения года в поле фильтрации по году выпуска
| Expected result    | В поле ввода года значение должно отображаться в формате "2024"                
| Actual result      | В поле ввода года значение отображается в неверном формате "2 024"
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
|                    | 6. Проскорллить вниз до фильтра "Год выпуска"
|                    | 7. Выбрать любой диапазон, например, 2021-2024
| Priority           | ${\color{green}Низкий}$
|                    | Данную ошибку можно быстро исправить, она не портит впечатление от сайта и компании, но для пользователя это непривычный формат отображения даты
|                    |
|                    |
| **ID**             | **6**           
| Title              | Частичное отображение фотографии товара при плиточном виде сортировки товаров на сайте 
| Expected result    | Фотография товара должна отображаться полностью              
| Actual result      | Фотография отображается только наполовину, остальная половина заполнена серым фоном
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
|                    | 6. Применить Плиточный вид сортировки
| Priority           | ${\color{yellow}Средний}$
|                    | Данный баг следует исправить в порядке общей очередности, так как он несущественно влияет на репутацию сайта, но доставляет определенные неудобства пользователям 
|                    |
|                    |
| **ID**             | **7**           
| Title              | Не отображается изображение товара при плиточном виде сортировки товаров на сайте
| Expected result    | Фотография товара должна отображаться               
| Actual result      | Изображение товара не отображается, в место, где должнабыть фотография товара дублируется название товара
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
|                    | 6. Применить Плиточный вид сортировки
| Priority           | ${\color{yellow}Средний}$
|                    | Данный баг следует исправить в порядке общей очередности, так как он несущественно влияет на репутацию сайта, но доставляет определенные неудобства пользователям
|                    |
|                    |
| **ID**             | **8**           
| Title              | Съехала иконка "добавить в избранное" при плиточном виде сортировки товаров на сайте
| Expected result    | Иконка "Добавить в избранное" находится на одной строке с наименованием товара               
| Actual result      | Иконка "Добавить в избранное" съехала на изображение товара
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Перейти в категорию транспорт 
|                    | 3. Перейти в категорию автомобили 
|                    | 4. Выбрать марку машины, например, BMW 
|                    | 5. Выбрать модель машины, например, X6
|                    | 6. Применить Плиточный вид сортировки
| Priority           | ${\color{yellow}Средний}$ 
|                    | Данный баг следует исправить в порядке общей очередности, так как он несущественно влияет на репутацию сайта, но доставляет определенные неудобства пользователям и является функциональной частью работы сайта
|                    |
|                    |
| **ID**             | **9**           
| Title              | В подборку автомобилей в выбранном городе попадают автомобили из других городов
| Expected result    | В подборку попадают только автомобили из выбранного для поиска города              
| Actual result      | В подборку также попадют автомобили из других городов
| Environments       | Windows 11, Google Chrome 128.0.0.0 (WebKit 537.36)
| Steps to reproduce | 1. Открыть главную страницу сайта
|                    | 2. Выбрать город для поиска
|                    | 3. Перейти в категорию транспорт 
|                    | 4. Перейти в категорию автомобили 
|                    | 5. Выбрать марку машины, например, BMW 
|                    | 6. Выбрать модель машины, например, X6
| Priority           | ${\color{red}Высокий}$
|                    | Необходимо исправить данную проблему как можно скорее, так как данная ошибка ухудшает пользовательский опыт и затрудняет поиск по сайту














