import streamlit as st
import math

st.title("Калькулятор для расчета количества обоев")
Swindow = 0
Sdoor = 0
lengthRoomSM = st.number_input("Введите длину комнаты в сантиметрах: ", min_value= 0)
widthRoomSM = st.number_input("Введите ширину комнаты в сантиметрах: ", min_value= 0)
heightRoomSM = st.number_input("Введите высоту комнаты в сантиметрах: ", min_value= 0)
lengthRoll = st.number_input("Введите длину рулона обоев в метрах: ")
widthRoll = st.number_input("Введите ширину рулона обоев в метрах: ")
# преобразуем см в м
lengthRoom = lengthRoomSM / 100
widthRoom = widthRoomSM / 100
heightRoom = heightRoomSM / 100
rapport = st.selectbox("Есть ли раппорт (повтор рисунка)?", ["Выберите вариант", "Да", "Нет"])
if rapport.lower() == 'да':
    measurement = st.selectbox("В каких единицах измерений указан раппорт?", ["Выберите вариант", "Метрах", "Сантиметрах"])
    if measurement.lower() == 'сантиметрах':
        valueRapportSM = st.number_input("Введите значение раппорта в сантиметрах:", min_value= 0)
        valueRapport = valueRapportSM / 100
    elif measurement.lower() == 'метрах':
        valueRapportM = st.number_input("Введите значение раппорта в метрах:")
        valueRapport = valueRapportM
window = st.selectbox("Есть окна?", ["Выберите вариант", "Да", "Нет"])
if window.lower() == "да":
    heightWindowSM = st.number_input("Введите высоту окна в сантиметрах: ", min_value= 0)
    lengthWindowSM = st.number_input("Введите ширину окна в сантиметрах: ", min_value= 0)
    heightWindow = heightWindowSM / 100
    lengthWindow = lengthWindowSM / 100
    Swindow = (lengthWindow * heightWindow)
    st.write(f'Площадь окна {round(Swindow, 2)} м²')
door = st.selectbox("Есть двери?", ["Выберите вариант", "Да", "Нет"])
if door.lower() == "да":
    heightDoorSM = st.number_input("Введите высоту двери в сантиметрах: ", min_value= 0)
    lengthDoorSM = st.number_input("Введите ширину двери в сантиметрах: ", min_value= 0)
    heightDoor = heightDoorSM / 100
    lengthDoor = lengthDoorSM / 100
    countDoor = int(st.number_input("Сколько дверей?", min_value= 1, step= 1))
    if countDoor > 1:
        Sdoor = (lengthDoor * heightDoor) * countDoor
        st.write(f'Суммарная площадь всех дверей {round(Sdoor, 2)} м²')
    else:
        Sdoor = lengthDoor * heightDoor
        st.write(f'Площадь двери {round(Sdoor, 2)} м²')
if st.button("Рассчитать"):
    # Периметр стен (в метрах)
    P = 2 * (lengthRoom + widthRoom)
    # Площадь комнаты под поклейку
    S = (P * heightRoom) - Swindow - Sdoor
    # Площадь рулона
    Sroll = (lengthRoll * widthRoll)
    if rapport.lower() == 'да':
        stripLength = math.ceil((heightRoom / valueRapport) * valueRapport)
        st.write(f'Длина одной полосы равна: {stripLength} м')
        countStrip = math.floor(lengthRoll / stripLength)
        st.write(f'Количество полос из рулона равна: {countStrip}')
        if countStrip == 0:
            countStrip = 1
        totalQuantityStrip = math.ceil(P / widthRoll)
        st.write(f'Общее количество полос: {totalQuantityStrip}')
        N = math.ceil(totalQuantityStrip / countStrip)
    else:
        N = math.ceil(S / Sroll)
    st.write(f'Периметр стен {P:.2f} м')
    st.write(f'Площадь стен {S:.2f} м²')
    st.write(f'Площадь рулона {Sroll:.2f} м²')
    st.write(f'Количество рулонов обоев {N} шт.')