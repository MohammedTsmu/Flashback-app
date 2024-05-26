import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta
import sqlite3

# إنشاء الاتصال بقاعدة البيانات
conn = sqlite3.connect('subjects.db')
c = conn.cursor()

# إنشاء جدول المواضيع إذا لم يكن موجودًا
c.execute('''CREATE TABLE IF NOT EXISTS subjects
             (id INTEGER PRIMARY KEY, name TEXT, desc TEXT, day1 TEXT, day3 TEXT, day6 TEXT, day10 TEXT, notified1 INTEGER, notified3 INTEGER, notified6 INTEGER, notified10 INTEGER)''')
conn.commit()

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("FlashBack")
root.geometry("600x600")  # تعيين حجم النافذة

# إنشاء إطار لاحتواء الأدوات
frame = tk.Frame(root)
frame.pack(pady=20)

# إنشاء ملصق لعرض اسم الموضوع
lbl_subject = tk.Label(frame, text="Subject Name:", font=('TkDefaultFont', 14))
lbl_subject.grid(row=0, column=0, padx=10)

# إنشاء حقل إدخال لاسم الموضوع
entry_subject = tk.Entry(frame, width=50, font=('TkDefaultFont', 12))
entry_subject.grid(row=0, column=1, padx=10)

# إنشاء ملصق لعرض الوصف
lbl_desc = tk.Label(frame, text="Description:", font=('TkDefaultFont', 14))
lbl_desc.grid(row=1, column=0, padx=10)

# إنشاء حقل نص للوصف
entry_desc = tk.Text(frame, height=5, width=50, font=('TkDefaultFont', 12))
entry_desc.grid(row=1, column=1, padx=10)

# وظيفة لإضافة موضوع
def add_subject():
    subject = entry_subject.get()
    desc = entry_desc.get("1.0", tk.END).strip()

    if subject:
        current_date = datetime.now()
        dates = [
            current_date + timedelta(days=1),
            current_date + timedelta(days=3),
            current_date + timedelta(days=6),
            current_date + timedelta(days=10)
        ]

        c.execute("INSERT INTO subjects (name, desc, day1, day3, day6, day10, notified1, notified3, notified6, notified10) VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (subject, desc, dates[0].strftime("%d-%m-%Y"), dates[1].strftime("%d-%m-%Y"),
                   dates[2].strftime("%d-%m-%Y"), dates[3].strftime("%d-%m-%Y"), 0, 0, 0, 0))
        conn.commit()

        entry_subject.delete(0, tk.END)
        entry_desc.delete("1.0", tk.END)

        load_subjects()
    else:
        messagebox.showwarning("Warning", "Please enter a subject name")

# وظيفة لتحميل المواضيع وعرضها في البطاقات
def load_subjects():
    # مسح البطاقات الموجودة
    for card in cards_frame.winfo_children():
        card.destroy()

    # استرجاع المواضيع من قاعدة البيانات
    c.execute("SELECT * FROM subjects")
    subjects = c.fetchall()

    # إنشاء بطاقة لكل موضوع
    for subject in subjects:
        card = tk.Frame(cards_frame, borderwidth=2, relief="solid")
        card.pack(side="top", padx=10, pady=10, fill="x")

        lbl_status = tk.Label(card, text="Still Studying", font=('TkDefaultFont', 12), fg="red")
        lbl_status.pack(anchor="n", pady=5)

        lbl_subject_name = tk.Label(card, text=f"{subject[1]}", font=('TkDefaultFont', 14))
        lbl_subject_name.pack(pady=5)

        lbl_description = tk.Label(card, text=f"{subject[2]}", font=('TkDefaultFont', 12))
        lbl_description.pack(pady=5)

        dates = [
            ("Day 1", subject[3], subject[7]),
            ("Day 3", subject[4], subject[8]),
            ("Day 6", subject[5], subject[9]),
            ("Day 10", subject[6], subject[10])
        ]

        for date_label, date, notified in dates:
            lbl_date = tk.Label(card, text=f"{date_label}: {date}", font=('TkDefaultFont', 12))
            lbl_date.pack(pady=5)

            date_obj = datetime.strptime(date, "%d-%m-%Y")
            if datetime.now() > date_obj:
                lbl_date.config(fg="red")

        last_date = datetime.strptime(subject[6], "%d-%m-%Y")
        now = datetime.now()
        countdown_label = tk.Label(card, text="", font=('TkDefaultFont', 12))
        countdown_label.pack(pady=5)

        if now < last_date:
            delete_text = "Delete button will be enabled in:"
            btn_delete_state = tk.DISABLED
        else:
            delete_text = "Delete button is enabled."
            btn_delete_state = tk.NORMAL
            lbl_status.config(text="Subject well known", fg="green")

        lbl_delete_info = tk.Label(card, text=delete_text, font=('TkDefaultFont', 12))
        lbl_delete_info.pack(pady=5)

        btn_edit_card = tk.Button(card, text="Edit", command=lambda s=subject: edit_subject_card(s), font=('TkDefaultFont', 10))
        btn_edit_card.pack(side="left", padx=5)

        btn_delete_card = tk.Button(card, text="Delete", command=lambda s=subject: delete_subject_card(s), font=('TkDefaultFont', 10), state=btn_delete_state)
        btn_delete_card.pack(side="left", padx=5)

        update_countdown(last_date, countdown_label, btn_delete_card, lbl_status)

# وظيفة لتحديث العد التنازلي
def update_countdown(end_time, countdown_label, delete_button, status_label):
    now = datetime.now()
    remaining_time = end_time - now

    if remaining_time.total_seconds() > 0:
        days, remainder = divmod(remaining_time.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_label.config(text=f"Time remaining: {int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s")
        countdown_label.after(1000, update_countdown, end_time, countdown_label, delete_button, status_label)
    else:
        countdown_label.config(text="Time is up!")
        delete_button.config(state=tk.NORMAL)
        status_label.config(text="Subject well known", fg="green")

# وظيفة لتحرير موضوع في بطاقة
def edit_subject_card(subject):
    entry_subject.delete(0, tk.END)
    entry_desc.delete("1.0", tk.END)

    entry_subject.insert(0, subject[1])
    entry_desc.insert("1.0", subject[2])

    def update_subject():
        new_subject = entry_subject.get()
        new_desc = entry_desc.get("1.0", tk.END).strip()

        if new_subject:
            current_date = datetime.now()
            dates = [
                current_date + timedelta(days=1),
                current_date + timedelta(days=3),
                current_date + timedelta(days=6),
                current_date + timedelta(days=10)
            ]

            c.execute("UPDATE subjects SET name=?, desc=?, day1=?, day3=?, day6=?, day10=? WHERE id=?",
                      (new_subject, new_desc, dates[0].strftime("%d-%m-%Y"), dates[1].strftime("%d-%m-%Y"),
                       dates[2].strftime("%d-%m-%Y"), dates[3].strftime("%d-%m-%Y"), subject[0]))
            conn.commit()

            entry_subject.delete(0, tk.END)
            entry_desc.delete("1.0", tk.END)
            btn_add.config(command=add_subject, text="Add Subject")

            load_subjects()
        else:
            messagebox.showwarning("Warning", "Please enter a new subject name")

    btn_add.config(command=update_subject, text="Update Subject")

# وظيفة لحذف موضوع في بطاقة
def delete_subject_card(subject):
    subject_id = subject[0]

    c.execute("DELETE FROM subjects WHERE id=?", (subject_id,))
    conn.commit()

    load_subjects()

# إنشاء أزرار لإضافة وتحرير وحذف المواضيع
btn_add = tk.Button(frame, text="Add Subject", command=add_subject, font=('TkDefaultFont', 14))
btn_add.grid(row=2, column=0, padx=10)

# إنشاء إطار لاحتواء البطاقات
cards_frame_container = tk.Frame(root)
cards_frame_container.pack(pady=20, fill="both", expand=True)

# إضافة شريط تمرير
canvas = tk.Canvas(cards_frame_container)
scrollbar = tk.Scrollbar(cards_frame_container, orient="vertical", command=canvas.yview)
cards_frame = tk.Frame(canvas)

cards_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=cards_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# وظيفة لفحص التواريخ وتحديث الإشعارات
def check_dates():
    c.execute("SELECT * FROM subjects")
    subjects = c.fetchall()

    if not subjects:  # Check if there are no subjects
        return

    notification_columns = {
        "Day 1": "notified1",
        "Day 3": "notified3",
        "Day 6": "notified6",
        "Day 10": "notified10"
    }

    for subject in subjects:
        dates = [
            ("Day 1", subject[3], subject[7]),
            ("Day 3", subject[4], subject[8]),
            ("Day 6", subject[5], subject[9]),
            ("Day 10", subject[6], subject[10])
        ]

        for day_label, date, notified in dates:
            date_obj = datetime.strptime(date, "%d-%m-%Y")
            notification_column = notification_columns[day_label]
            if datetime.now() > date_obj and not notified:
                messagebox.showinfo("Notification", f"Time to review: {subject[1]} on {day_label}")
                c.execute(f"UPDATE subjects SET {notification_column}=? WHERE id=?", (1, subject[0]))
                conn.commit()

    load_subjects()
    root.after(60000, check_dates)  # إعادة الفحص كل دقيقة

# تحميل المواضيع وعرضها في البطاقات
load_subjects()

# بدء فحص التواريخ
check_dates()

# بدء الحلقة الرئيسية للأحداث
root.mainloop()

# إغلاق الاتصال بقاعدة البيانات
conn.close()
