import streamlit as st

# ==========================================================
# 📊 МЕТАТЕГИ И НАСТРОЙКА СТРАНИЦЫ (SEO)
# ==========================================================
st.set_page_config(
    page_title="Автоматизация Excel и PDF | Нижнекамск, Челны",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": """
        ### Автоматизация ОПП и макросы Excel
        Разработка алгоритмов для инженеров, сметчиков и проектировщиков в Нижнекамске.
        Перенос из PDF в Excel, автоматизация актов, ГПР и отчетов.
        """
    },
)

# ==========================================================
# 🎨 СТИЛИЗАЦИЯ И ЦЕНТРИРОВАНИЕ КНОПОК (CSS)
# ==========================================================
st.markdown(
    """
    <style>
    /* Центрируем сами колонки и ограничиваем их общую ширину */
    div[data-testid="stHorizontalBlock"] {
        justify-content: center !important;
        align-items: center !important;
        gap: 15px !important;
        max-width: 600px !important;
        margin: 0 auto !important;
    }
    
    /* Центрируем содержимое внутри каждой отдельной колонки */
    div[data-testid="column"] {
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Делаем контейнеры кнопок адаптивными */
    div[data-testid="stBaseButton-link"] {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Задаем кнопкам одинаковую ширину и высоту */
    div[data-testid="stBaseButton-link"] button {
        width: 100% !important;
        max-width: 180px !important;
        height: 52px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        padding: 0px !important;
        text-align: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# 🚀 1. ГЛАВНЫЙ ЭКРАН (ОФФЕР) — ВСЁ ПО ЦЕНТРУ
# ==========================================================
st.markdown(
    "<h1 style='text-align: center;'>Автоматизация и разработка макросов в Excel</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>Нижнекамск / Набережные Челны / Удаленно</h3>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align: center; font-size: 1.1rem; margin-bottom: 20px;'>
        Ускоряю рутинную работу инженеров, проектировщиков и сметчиков <b>в 5 раз</b> с помощью умных алгоритмов Python и Excel.<br>
        <i>Без расширения штата и переплат.</i>
    </div>
    """,
    unsafe_allow_html=True
)

# Выводим идеально ровные кнопки связи
col_phone, col_tg, col_max = st.columns(3)
with col_phone:
    st.link_button("📞 Позвонить", "tel:+79375990332")
with col_tg:
    st.link_button("💬 Telegram", "https://t.me")
with col_max:
    st.link_button("💻 Макс", "https://max.ru")

st.write("---")

# ==========================================================
# 🛠️ 2. БЛОК «ЧТО Я ДЕЛАЮ» (УСЛУГИ)
# ==========================================================
st.header("🛠️ Чем я могу помочь вашему бизнесу")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 📄 Из PDF в Excel")
    st.write("Мгновенный автоматический перенос спецификаций, чертежей ТХ/КМ и физобъемов в редактируемые таблицы за пару минут.")
with col2:
    st.markdown("### ⚙️ Умные макросы")
    st.write("Автозаполнение актов, ведомостей, общих журналов работ и форм отчетности в один клик без опечаток.")
with col3:
    st.markdown("### 📊 Связка данных")
    st.write("Автоматическое построение графиков производства работ (ГПР), лимитно-заборных карт и сверка объемов (Проект / Смета / Факт).")

st.write("---")

# ==========================================================
# 👷 3. БЛОК ДОВЕРИЯ
# ==========================================================
st.header("👷 Почему именно я?")
st.info(
    "Вам не придется писать длинные инструкции для программиста. Я сам работаю инженером в Нижнекамске и знаю изнанку этой профессии. Я сразу понимаю, где в таблицах возникают затыки, поэтому мы быстро найдем общее решение без лишней бюрократии."
)

st.write("---")

# ==========================================================
# 🔥 4. ПРИЗЫВ К ДЕЙСТВИЮ И ТЕСТ-ДРАЙВ
# ==========================================================
st.header("🔥 Бесплатный тест-драйв")
st.warning(
    "У вас есть сложная таблица или горящий объект? **Пришлите тестовый PDF-файл (до 5 страниц) мне в ЛС.** "
    "Я бесплатно перенесу его в Excel, чтобы вы оценили скорость и качество работы алгоритма еще до оплаты!"
)

st.markdown("### 📱 Контакты для связи:")
st.markdown("**Телефон:** +7 937 599 0332")
st.markdown("**Email:** [mb0332@mail.ru](mailto:mb0332@mail.ru)")
st.markdown("**Telegram / Макс / WhatsApp:** по номеру телефона или кнопкам выше.")

# ==========================================================
# 🔍 5. ТЕГИ И КЛЮЧЕВЫЕ СЛОВА ДЛЯ ПОИСКОВИКОВ (SEO) — СКРЫТЫЕ
# ==========================================================
st.write("---")
st.markdown(
    """
    <div style="display: none;">
        #автоматизация_excel #макросы_на_заказ #заказать_макрос #из_pdf_в_excel #vba_скрипты #python_скрипты 
        #парсинг_pdf #конвертация_таблиц #связка_данных #сверка_объемов #автозаполнение_актов #составление_гпр 
        #анализ_данных_эксель #шаблоны_excel #написание_макросов #ускорение_расчетов
        #инженер_опп #инженер_пто #для_сметчиков #для_проектировщиков #расчет_физобъемов #строительный_контроль 
        #аналитика_для_бизнеса #учет_материалов #лимитно_заборная_карта #автоматизация_производства
        #microsoft_excel #vba #python #pandas #openpyxl #pdfplumber #excel_macros #макросы_vba
        #нижнекамск #набережные_челны #татарстан #казань #альметьевск #удаленно #фриланс_эксель
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# 📈 УЛЬТРАБЫСТРЫЙ СЧЕТЧИК ЯНДЕКС МЕТРИКИ (ФИНАЛЬНЫЙ)
# ==========================================================
st.components.v1.html(
    """
    <script type="text/javascript">
       (function(m,e,t,r,i,k,a){
           m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
           m[i].l=1*new Date();
           k=e.createElement(t);
           a=e.getElementsByTagName("html")[0]; /* Добавлен индекс [0] для стабильности */
           k.async=1;
           k.src=r;
           a.appendChild(k);
       })(window, document, "script", "https://yandex.ru", "ym");

       ym(114050636, "init", {
            clickmap:true,
            trackLinks:true,
            accurateTrackBounce:true,
            webvisor:true
       });
    </script>
    <noscript><div><img src="https://yandex.ru" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    """,
    height=0,
)
