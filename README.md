# AlQFILA Core Execution

المستودع التنفيذي الأساسي لمشروع القافلة. سيحتوي على خدمات Python، والبنية التحتية ككود، وإعدادات التشغيل والنشر. تبقى الرسومات والقواعد الحاكمة والتوثيق المعماري في مستودع [`qafila-systems-architecture`](https://github.com/wissamblue69-dotcom/qafila-systems-architecture).

## النطاق الحالي

الهيكل الأولي يستهدف Python 3.10+ وخدمة FastAPI، مع Redis للتخزين المؤقت وApache Kafka لمسارات البيانات. يوفر Docker Compose بيئة محلية أولية، بينما يحتوي مجلد Terraform على تعريف اختياري لشبكة VPC على Google Cloud Platform. لا تُنشأ موارد سحابية افتراضيًا؛ يجب تفعيلها ومراجعة متغيراتها صراحةً.

## البنية

- `app/`: كود الخدمة التنفيذي.
- `infrastructure/docker/`: صورة الخدمة وبيئة Docker Compose المحلية.
- `infrastructure/terraform/`: تعريفات Google Cloud والبنية التحتية ككود.
- `requirements.txt`: التبعيات الأولية القابلة للتثبيت.

## التشغيل المحلي

بعد تثبيت Docker، شغّل:

```bash
docker compose -f infrastructure/docker/docker-compose.yml up --build
```

ثم افحص الخدمة عبر `http://localhost:8000/health`.

## ملاحظات تشغيلية

هذا الهيكل تأسيسي وليس إعلانًا عن جاهزية الإنتاج. يجب إضافة اختبارات، وإدارة أسرار، ومراقبة، وسياسات وصول، ومسار نشر بعد مراجعة المتطلبات التشغيلية.
