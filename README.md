# HA Log Healer (طبيب سيرفر Home Assistant) 🩺🤖

![HA Log Healer](https://img.shields.io/badge/Home_Assistant-Custom_Component-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)

A unique Home Assistant custom integration that automatically reads your `home-assistant.log`, detects errors and warnings, and uses AI (Groq, OpenRouter, DeepSeek, OpenAI) to analyze the traceback and provide a human-readable solution in Arabic (or English).

إضافة حصرية لـ Home Assistant تقوم بقراءة ملف الأخطاء (Logs) الخاص بالسيرفر، وتستخدم الذكاء الاصطناعي (مثل Groq السريع أو DeepSeek) لتحليل الأكواد المكسورة وتقديم الحل المناسب باللغة العربية البسيطة.

## 🚀 المميزات (Features)
- 📝 **قراءة تلقائية:** يسحب آخر 200 سطر من ملف الـ log ويبحث عن `ERROR` أو `WARNING`.
- 🧠 **تحليل بالذكاء الاصطناعي:** يرسل الأخطاء لأي واجهة متوافقة مع OpenAI (مثل Groq لسرعة فائقة).
- 💡 **حلول مبسطة:** يترجم الأكواد المعقدة إلى خطوات حل واضحة ومباشرة.
- ⚙️ **إعداد من الواجهة (UI Config):** لا يتطلب كتابة YAML، يتم إدخال الـ API Key من واجهة Integrations مباشرة.

## 🛠️ التثبيت (Installation)

### عن طريق HACS (موصى به)
1. اذهب إلى **HACS** > **Integrations**.
2. اضغط على الـ 3 نقاط أعلى اليمين واختر **Custom repositories**.
3. أضف رابط هذا المستودع كـ `Integration`.
4. ابحث عن `HA Log Healer` وقم بتثبيته.
5. أعد تشغيل Home Assistant.

### يدوياً (Manual)
1. قم بتحميل المجلد `custom_components/ha_log_healer`.
2. ضعه داخل مجلد `custom_components` في سيرفرك.
3. أعد تشغيل Home Assistant.

## ⚙️ الإعدادات (Configuration)
1. اذهب إلى **Settings** > **Devices & Services** > **Add Integration**.
2. ابحث عن **HA Log Healer**.
3. أدخل الـ API Key (مثلاً الخاص بـ Groq أو OpenRouter).
4. اضغط Submit.

## 🖱️ كيفية الاستخدام
الإضافة توفر خدمة (Service) باسم `ha_log_healer.analyze_logs`.
بمجرد استدعاء هذه الخدمة، ستقوم بقراءة الأخطاء وتحليلها، ثم حفظ الحل في الكيان (Entity) الخاص بها: `sensor.ha_log_healer_analysis`.
