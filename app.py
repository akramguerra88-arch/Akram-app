
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# البيانات
results = [12, 8, 8, 7, 7, 7, 4, 4, 6, 7,
           9, 11, 7, 4, 4, 9, 2, 5, 8, 8,
           4, 2, 6]

df = pd.DataFrame(results, columns=["Result"])

st.title("تحليل النتائج")

# عرض الجدول
st.subheader("📋 البيانات")
st.dataframe(df)

# عرض الاحصائيات
st.subheader("📊 إحصائيات")
st.write("المتوسط الحسابي:", round(df["Result"].mean(), 2))
st.write("الانحراف المعياري:", round(df["Result"].std(), 2))

# رسم بياني
st.subheader("📈 توزيع الأرقام")
fig, ax = plt.subplots()
df["Result"].value_counts().sort_index().plot(kind="bar", ax=ax)
st.pyplot(fig)
