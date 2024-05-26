# FlashBack App

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
4. [Running the Application](#running-the-application)
5. [How to Use](#how-to-use)
6. [Instructions in Arabic](#instructions-in-arabic)

## Introduction
FlashBack is a reminder application designed to help you keep track of subjects and their review dates. The app allows you to add subjects, set descriptions and review dates, and receive notifications when it's time to review.

## Requirements
- Python 3.10 or later
- SQLite3 (usually comes pre-installed with Python)

## Setup Instructions
1. **Install Python**:
    - Download and install the latest version of Python from the [official website](https://www.python.org/).

2. **Clone or Download the Repository**:
    - Clone the repository using `git clone <repository-url>` or download the zip file and extract it.

3. **Navigate to the Project Directory**:
    - Open a terminal or command prompt.
    - Navigate to the directory where you cloned or extracted the project files.

4. **Install Required Packages**:
    - Install the necessary packages using the following command:
      ```sh
      pip install tkinter
      ```

## Running the Application
1. **Run the Application**:
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Run the application with the following command:
      ```sh
      python flashback.py
      ```

2. **Using the Application**:
    - The application window will open.
    - You can now add subjects, descriptions, and review dates.

## How to Use
1. **Add a Subject**:
    - Enter the subject name in the "Subject Name" field.
    - Enter the description in the "Description" field.
    - Click "Add Subject" to save the subject.

2. **Edit a Subject**:
    - Click the "Edit" button on the card of the subject you want to edit.
    - Make your changes in the fields and click "Update Subject".

3. **Delete a Subject**:
    - The delete button will be enabled when the last review date is passed.
    - Click the "Delete" button to remove the subject.

4. **Review Dates**:
    - Review dates are automatically set for 1, 3, 6, and 10 days from the creation date.
    - Notifications will appear when it's time to review a subject.

---

# تطبيق FlashBack

## جدول المحتويات
1. [مقدمة](#مقدمة)
2. [المتطلبات](#المتطلبات)
3. [إرشادات الإعداد](#إرشادات-الإعداد)
4. [تشغيل التطبيق](#تشغيل-التطبيق)
5. [كيفية الاستخدام](#كيفية-الاستخدام)
6. [الإرشادات باللغة العربية](#الإرشادات-باللغة-العربية)

## مقدمة
FlashBack هو تطبيق تذكير مصمم لمساعدتك على تتبع المواضيع ومواعيد مراجعتها. يتيح لك التطبيق إضافة مواضيع ووصف وتواريخ مراجعة، وتلقي إشعارات عندما يحين وقت المراجعة.

## المتطلبات
- Python 3.10 أو أحدث
- SQLite3 (عادةً ما تكون مثبتة مسبقًا مع Python)

## إرشادات الإعداد
1. **تثبيت Python**:
    - قم بتنزيل وتثبيت أحدث إصدار من Python من [الموقع الرسمي](https://www.python.org/).

2. **استنساخ أو تنزيل المستودع**:
    - استنسخ المستودع باستخدام `git clone <repository-url>` أو قم بتنزيل ملف zip واستخراجه.

3. **الانتقال إلى دليل المشروع**:
    - افتح محطة الأوامر أو موجه الأوامر.
    - انتقل إلى الدليل حيث قمت باستنساخ أو استخراج ملفات المشروع.

4. **تثبيت الحزم المطلوبة**:
    - قم بتثبيت الحزم الضرورية باستخدام الأمر التالي:
      ```sh
      pip install tkinter
      ```

## تشغيل التطبيق
1. **تشغيل التطبيق**:
    - افتح محطة الأوامر أو موجه الأوامر.
    - انتقل إلى دليل المشروع.
    - قم بتشغيل التطبيق باستخدام الأمر التالي:
      ```sh
      python flashback.py
      ```

2. **استخدام التطبيق**:
    - ستفتح نافذة التطبيق.
    - يمكنك الآن إضافة مواضيع وأوصاف وتواريخ مراجعة.

## كيفية الاستخدام
1. **إضافة موضوع**:
    - أدخل اسم الموضوع في حقل "Subject Name".
    - أدخل الوصف في حقل "Description".
    - انقر فوق "Add Subject" لحفظ الموضوع.

2. **تحرير موضوع**:
    - انقر فوق زر "Edit" في بطاقة الموضوع الذي تريد تحريره.
    - قم بإجراء التغييرات في الحقول وانقر فوق "Update Subject".

3. **حذف موضوع**:
    - سيتم تفعيل زر الحذف عندما تمر آخر تاريخ مراجعة.
    - انقر فوق زر "Delete" لإزالة الموضوع.

4. **تواريخ المراجعة**:
    - يتم تعيين تواريخ المراجعة تلقائيًا بعد 1 و 3 و 6 و 10 أيام من تاريخ الإنشاء.
    - ستظهر الإشعارات عندما يحين وقت مراجعة الموضوع.
