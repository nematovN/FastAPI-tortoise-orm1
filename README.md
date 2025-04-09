# 🐢 Tortoise ORM & ⚙️ Aerich Bilan Ishlash

Bu hujjat `Tortoise ORM` va uning migratsiya vositasi `Aerich` bilan qanday ishlashni bosqichma-bosqich tushuntiradi.

---

## 📦 1. Virtual muhit (venv) yaratish

**MacOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 📥 2. Zaruriy kutubxonalarni o‘rnatish

```bash
pip install tortoise-orm aerich
```

---

## ⚙️ 3. Aerich konfiguratsiyasini boshlash

```bash
aerich init -t db.DB_CONFIG
```

> `db.DB_CONFIG` — bu sizning `Tortoise` konfiguratsiyangiz joylashgan modul yo‘li (masalan: `myapp.settings.TORTOISE_ORM`).

---

## 🛠️ 4. Dastlabki ma'lumotlar bazasini yaratish

```bash
aerich init-db
```

---

## ✍️ 5. Modelga o‘zgarish kiritilgach

**Migratsiya faylini yaratish:**
```bash
aerich migrate
```

**Migratsiyani bazaga qo‘llash:**
```bash
aerich upgrade
```

---

## ✅ Tayyor!
